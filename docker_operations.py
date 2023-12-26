# docker_operations.py

import subprocess

from user_operations import run_command


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
