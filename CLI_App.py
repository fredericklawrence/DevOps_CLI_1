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

def main():
    parser = argparse.ArgumentParser(description="DevOps CLI App")
    parser.add_argument("--create-user", help="Create a new user")
    parser.add_argument("--delete-user", help="Delete an existing user")
    
    args = parser.parse_args()

    if args.create_user:
        create_user(args.create_user)
    elif args.delete_user:
        delete_user(args.delete_user)
    else:
        print("No valid command provided. Use --help for usage information.")

if __name__ == "__main__":
    main()
