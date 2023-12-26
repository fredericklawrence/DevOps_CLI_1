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
    parser = argparse.ArgumentParser(description="DevOps CLI App")
    parser.add_argument("--create-user", help="Create a new user")
    parser.add_argument("--delete-user", help="Delete an existing user")
    parser.add_argument("--set-firewall-rule", help="Set a firewall rule with ufw")
    parser.add_argument("--delete-firewall-rule", help="Delete a firewall rule with ufw")

    args = parser.parse_args()

    if args.create_user:
        create_user(args.create_user)
    elif args.delete_user:
        delete_user(args.delete_user)
    elif args.set_firewall_rule:
        set_firewall_rule(args.set_firewall_rule)
    elif args.delete_firewall_rule:
        delete_firewall_rule(args.delete_firewall_rule)
    else:
        print("No valid command provided. Use --help for usage information.")

if __name__ == "__main__":
    main()
