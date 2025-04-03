# Docker Learning Repository - Practical Examples & Contributions Welcome!

## Found this repository helpful? Give it a STAR 🌟

## What is a Container?

A container is a self-sufficient software package that includes all necessary dependencies, ensuring seamless execution across different environments. A Docker container image is a lightweight, standalone, and executable software unit that includes essential components such as application code, runtime, system tools, libraries, and configurations.

Simplified explanation:
A container encapsulates an application, its required libraries, and minimal system dependencies to ensure portability and consistency across diverse environments.

## Containers vs. Virtual Machines

Both containers and virtual machines enable application isolation, but they differ in key aspects:

1. **Resource Efficiency:** Containers share the host OS kernel, making them lightweight and faster than VMs, which require a dedicated OS and hypervisor, consuming more resources.
2. **Portability:** Containers are highly portable and can run on any system with a compatible host OS, whereas VMs require a suitable hypervisor.
3. **Security:** VMs provide stronger isolation as each VM has its own OS. Containers share the host OS, offering relatively less isolation.
4. **Management:** Containers are easier to manage due to their lightweight and modular design.

## Why are Containers Lightweight?

Containers leverage the host OS's kernel and essential libraries, eliminating the need for a full OS within each instance. This results in a significantly smaller footprint compared to virtual machines.

For example:
- An official Ubuntu container base image is about **22 MB**.
- A full-fledged Ubuntu VM image is approximately **2.3 GB**.

This means container images can be nearly **100 times smaller** than VM images!

## Understanding Files and Folders in Containers

### Common directories in container base images:
```
/bin: Essential binaries like ls, cp, and ps.
/sbin: System binaries such as init and shutdown.
/etc: Configuration files for system services.
/lib: Libraries used by binaries.
/usr: User-related files, utilities, and documentation.
/var: Variable data including logs and temp files.
/root: Home directory of the root user.
```

### Components containers utilize from the host OS:
```
- File System: Containers can access host files using bind mounts.
- Networking: Uses the host’s networking stack for connectivity.
- System Calls: The host OS kernel manages container requests.
- Namespaces: Ensures isolation of processes and resources.
- Control Groups (cgroups): Restricts resource usage like CPU and memory.
```

Despite sharing resources, containers remain isolated from the host system and other containers, ensuring stability and security.

## Introduction to Docker

### What is Docker?
Docker is a platform that simplifies containerization by allowing users to create, manage, and distribute containerized applications. Docker enables developers to:
- Build container images.
- Run containers from images.
- Push and pull container images from registries like DockerHub.

In simple terms:
**Containerization is the concept, and Docker is its implementation.**

### Docker Architecture

The **Docker Daemon** (dockerd) is the core of Docker. If the daemon stops, Docker ceases to function.

### Docker Lifecycle

1. **docker build** → Creates Docker images from a Dockerfile.
2. **docker run** → Runs a container from an image.
3. **docker push** → Uploads an image to a registry for sharing.

## Key Docker Components

### Docker Daemon
Manages Docker objects (containers, images, networks, and volumes) and listens for API requests.

### Docker Client
The primary interface through which users interact with Docker via CLI commands.

### Docker Desktop
An all-in-one Docker environment available for Windows, macOS, and Linux.

### Docker Registries
A repository for storing and sharing Docker images, with **Docker Hub** being the default public registry.

### Dockerfile
A script containing instructions to build Docker images.

### Docker Images
A read-only template used to create containers, consisting of application code and dependencies.

## Installing Docker

Official installation guide: [Docker Installation](https://docs.docker.com/get-docker/)

For Ubuntu:
```
sudo apt update
sudo apt install docker.io -y
```

### Starting Docker and Granting Access

Check Docker service status:
```
sudo systemctl status docker
```

Start Docker if not running:
```
sudo systemctl start docker
```

Grant user access to run Docker commands:
```
sudo usermod -aG docker $USER
```
**Note:** Logout and login again for the changes to take effect.

Verify installation:
```
docker run hello-world
```

## Getting Started with Docker

### Clone this Repository and Navigate to Examples Folder
```
git clone https://github.com/your-repo/Docker/
cd examples
```

### Login to Docker
```
docker login
```

### Build Your First Docker Image
Replace `your-docker-username` accordingly:
```
docker build -t your-docker-username/my-first-docker-image:latest .
```

### Verify Created Docker Image
```
docker images
```
Expected output:
```
REPOSITORY                          TAG       IMAGE ID       CREATED         SIZE
your-docker-username/first-docker-image   latest    abcdef123456   A few seconds ago   XYZMB
```

### Run Your First Docker Container
```
docker run -it your-docker-username/first-docker-image
```
Expected output:
```
Hello World
```

### Push the Image to DockerHub
```
docker push your-docker-username/first-docker-image
```

## Congratulations! 🎉 Start Exploring Docker Further 🚀

## Copyright
© 2025 @iamsandeeepg/Docker. All rights reserved.
