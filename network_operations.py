# network_operations.py

import subprocess


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
