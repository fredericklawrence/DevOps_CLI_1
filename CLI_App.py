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

def run_docker_container(image_name):
    print(f"Running Docker container with image: {image_name}")
    command = f"sudo docker run {image_name}"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def show_docker_stats():
    print("Docker Status/Stats:")
    command = "sudo docker info"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def show_user_stats():
    print("User Status/Stats:")
    command = "sudo who"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def show_firewall_stats():
    print("Firewall Status/Stats:")
    command = "sudo ufw status"
    stdout, stderr = run_command(command)
    print(stdout)
    print(stderr)

def main_menu():
    while True:
        print("\nMain Menu Options:")
        print("1. User Operations")
        print("2. Firewall")
        print("3. Docker")
        print("4. Show User Stats")
        print("5. Show Firewall Stats")
        print("6. Show Docker Stats")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            firewall_menu()
        elif choice == "3":
            docker_menu()
        elif choice == "4":
            show_user_stats()
        elif choice == "5":
            show_firewall_stats()
        elif choice == "6":
            show_docker_stats()
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

def user_menu():
    while True:
        print("\nUser Operations Menu:")
        print("1. Create User")
        print("2. Delete User")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            username = input("Enter the username to create: ")
            create_user(username)
        elif choice == "2":
            username = input("Enter the username to delete: ")
            delete_user(username)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def firewall_menu():
    while True:
        print("\nFirewall Menu:")
        print("1. Set Firewall Rule")
        print("2. Delete Firewall Rule")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            rule = input("Enter the firewall rule to set: ")
            set_firewall_rule(rule)
        elif choice == "2":
            rule = input("Enter the firewall rule to delete: ")
            delete_firewall_rule(rule)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def docker_menu():
    while True:
        print("\nDocker Menu:")
        print("1. Run Docker Container")
        print("2. Back to Main Menu")

        choice = input("Enter your choice (1-2): ")

        if choice == "1":
            image_name = input("Enter the Docker image name: ")
            run_docker_container(image_name)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

if __name__ == "__main__":
    main_menu()
