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

def generate_ssh_key():
    print("Generating RSA key pair...")
    key_name = input("Enter a name for the key (e.g., my_key): ")
    key_path = f"{key_name}_rsa"

    # Run the ssh-keygen command to generate the key pair
    command = f"ssh-keygen -t rsa -b 2048 -f {key_path}"
    stdout, stderr = run_command(command)

    print("RSA key pair generated successfully:")
    print(f"Private key saved to: {key_path}")
    print(f"Public key saved to: {key_path}.pub")
    print(stdout)
    print(stderr)

def show_ssh_keys():
    print("Showing existing SSH keys:")
    command = "ls -l ~/.ssh/*.pub"
    stdout, stderr = run_command(command)

    if not stderr:
        print(stdout)
    else:
        print("Error occurred while listing SSH keys.")
        print(stderr)

def ssh_menu():
    while True:
        print("\nSSH Menu:")
        print("1. Generate RSA Key Pair")
        print("2. Show Existing SSH Keys")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            generate_ssh_key()
        elif choice == "2":
            show_ssh_keys()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def main_menu():
    while True:
        print("\nMain Menu Options:")
        print("1. User Operations")
        print("2. Network")
        print("3. Docker")
        print("4. SSH")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            network_menu()
        elif choice == "3":
            docker_menu()
        elif choice == "4":
            ssh_menu()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

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
        print("4. Inspect Container")
        print("5. Start Container")
        print("6. Stop Container")
        print("7. Restart Container")
        print("8. Show Container Logs")
        print("9. Back to Docker Menu")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            image_name = input("Enter the Docker image name: ")
            run_docker_container(image_name)
        elif choice == "2":
            container_id = input("Enter the Docker container ID to delete: ")
            delete_docker_container(container_id)
        elif choice == "3":
            list_docker_containers()
        elif choice == "4":
            container_id = input("Enter the Docker container ID to inspect: ")
            inspect_docker_container(container_id)
        elif choice == "5":
            container_id = input("Enter the Docker container ID to start: ")
            start_docker_container(container_id)
        elif choice == "6":
            container_id = input("Enter the Docker container ID to stop: ")
            stop_docker_container(container_id)
        elif choice == "7":
            container_id = input("Enter the Docker container ID to restart: ")
            restart_docker_container(container_id)
        elif choice == "8":
            container_id = input("Enter the Docker container ID to show logs: ")
            show_docker_container_logs(container_id)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main_menu()
