import argparse
import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )
        return result.stdout, result.stderr
    except Exception as e:
        return None, str(e)

def create_user(username):
    print(f"Creating user: {username}")
    command = f"sudo useradd {username}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def delete_user(username):
    print(f"Deleting user: {username}")
    command = f"sudo userdel {username}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def show_users():
    print("List of Users:")
    command = "sudo cat /etc/passwd | cut -d: -f1"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def show_groups():
    print("List of Groups:")
    command = "sudo cat /etc/group | cut -d: -f1"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def set_firewall_rule(rule):
    print(f"Setting firewall rule: {rule}")
    command = f"sudo ufw {rule}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def delete_firewall_rule(rule):
    print(f"Deleting firewall rule: {rule}")
    command = f"sudo ufw delete {rule}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def list_firewall_rules():
    print("List of Firewall Rules:")
    command = "sudo ufw status numbered"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def show_docker_status():
    print("Docker Status:")
    command = "sudo docker info"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def run_docker_container(image_name):
    print(f"Running Docker container with image: {image_name}")
    command = f"sudo docker run {image_name}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def delete_docker_container(container_id):
    print(f"Deleting Docker container with ID: {container_id}")
    command = f"sudo docker rm {container_id}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def list_docker_containers():
    print("List of Docker Containers:")
    command = "sudo docker ps -a"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

# Additional Docker functionalities (Stacks, Volumes, Networks, Images) can be added similarly

def main_menu():
    while True:
        print("\nMain Menu Options:")
        print("1. User Operations")
        print("2. Network")
        print("3. Docker")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            network_menu()
        elif choice == "3":
            docker_menu()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def user_menu():
    while True:
        print("\nUser Operations Menu:")
        print("1. Create User")
        print("2. Delete User")
        print("3. Show Users")
        print("4. Show Groups")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            username = input("Enter the username to create: ")
            create_user(username)
        elif choice == "2":
            username = input("Enter the username to delete: ")
            delete_user(username)
        elif choice == "3":
            show_users()
        elif choice == "4":
            show_groups()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def network_menu():
    while True:
        print("\nNetwork Menu:")
        print("1. Firewall")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            firewall_menu()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

def firewall_menu():
    while True:
        print("\nFirewall Menu:")
        print("1. New Rule")
        print("2. Delete Rule")
        print("3. List Rules")
        print("4. Back to Network Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            rule = input("Enter the firewall rule to set: ")
            set_firewall_rule(rule)
        elif choice == "2":
            rule = input("Enter the firewall rule to delete: ")
            delete_firewall_rule(rule)
        elif choice == "3":
            list_firewall_rules()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def docker_menu():
    while True:
        print("\nDocker Menu:")
        print("1. Status")
        print("2. Containers")
        # Add more options for additional Docker functionalities (Stacks, Volumes, Networks, Images)
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            show_docker_status()
        elif choice == "2":
            docker_container_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def docker_container_menu():
    while True:
        print("\nDocker Containers Menu:")
        print("1. New Container")
        print("2. Delete Container")
        print("3. List Containers")
        # Add more options for managing Docker containers
        print("4. Back to Docker Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            image_name = input("Enter the Docker image name: ")
            run_docker_container(image_name)
        elif choice == "2":
            container_id = input("Enter the Docker container ID to delete: ")
            delete_docker_container(container_id)
        elif choice == "3":
            list_docker_containers()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
