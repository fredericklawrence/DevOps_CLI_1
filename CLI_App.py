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

def main():
    while True:
        print("\nOptions:")
        print("1. Create User")
        print("2. Delete User")
        print("3. Set Firewall Rule")
        print("4. Delete Firewall Rule")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            username = input("Enter the username to create: ")
            create_user(username)
        elif choice == "2":
            username = input("Enter the username to delete: ")
            delete_user(username)
        elif choice == "3":
            rule = input("Enter the firewall rule to set: ")
            set_firewall_rule(rule)
        elif choice == "4":
            rule = input("Enter the firewall rule to delete: ")
            delete_firewall_rule(rule)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
