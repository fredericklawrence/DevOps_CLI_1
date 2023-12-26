# ssh_operations.py

import subprocess


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
