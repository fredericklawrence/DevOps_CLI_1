# user_operations.py

import subprocess

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
