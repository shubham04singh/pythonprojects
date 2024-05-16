import docker

# Connect to Docker daemon
client = docker.from_env()

# Define port mapping
ports = {'80/tcp': 8090}  # Map container port 80 to host port 8080

# Pull Docker image
client.images.pull('nginx:latest')

# Run Docker container with port mapping
container = client.containers.run('nginx:latest', detach=True, ports=ports)

# List running containers
print("Running containers:")
for container in client.containers.list():
    print(container.name)
