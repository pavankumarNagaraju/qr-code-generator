# Reflection on Dockerizing the QR Code Generator Application

## Overview
This project focused on containerizing a Python-based QR Code Generator application using Docker to make it portable, secure, and easily deployable. I learned how to create a reliable Docker image, run it inside a container, and automate image deployment to DockerHub using GitHub Actions. 

The main goal was to ensure the application runs identically across any environment and follows best practices for container security.

---

## Security and Optimization Choices
I implemented several key Docker security measures:

- **Non-Root User:**  
  The Dockerfile creates and runs the application as a non-root user named `myuser`. This limits privileges and reduces risks in case of vulnerabilities inside the container.

- **Slim Base Image:**  
  I used the lightweight image `python:3.12-slim-bullseye`, which significantly reduces image size and minimizes attack surface by including only essential system libraries.

- **Ownership and Permissions:**  
  I explicitly created and set ownership for the `logs` and `qr_codes` directories. This ensures only the non-root user can write to these directories safely during runtime.

- **.dockerignore File:**  
  The `.dockerignore` file excludes unnecessary files like `.venv`, cache folders, and logs from being copied into the image. This keeps the final image small, clean, and efficient.

---

## Automation and Deployment
I configured a **GitHub Actions workflow** (`.github/workflows/docker-publish.yml`) that automatically:
1. Builds the Docker image on every push to the `main` branch.  
2. Logs into DockerHub using repository secrets (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`).  
3. Pushes the newly built image to my DockerHub repository (`pavankumarnagaraju/qr-code-generator-app`).

This continuous integration and deployment setup ensures the image in DockerHub is always up to date with the latest code changes.

---

## Testing and Functionality
I tested the container by:
- Running it locally using `docker run -d --name qr-generator qr-code-generator-app`.  
- Checking logs with `docker logs qr-generator` to confirm QR code generation.  
- Overriding the default URL using command-line arguments.  
- Mounting a host volume to `/app/qr_codes` to save generated QR images directly on my computer.

These steps verified that the container builds and runs correctly, accepts parameters, and produces the expected output.

---

## Challenges and Learnings
A few small challenges occurred during setup:
- **Windows Path Mounting:** I initially faced issues mapping local folders with Docker volumes. This was resolved by using PowerShell’s `${PWD}` syntax (`"${PWD}\qr_codes:/app/qr_codes"`).  
- **DockerHub Token Management:** I learned how to generate and securely store access tokens instead of passwords for GitHub Actions automation.  
- **Workflow Debugging:** Setting up correct secret names and ensuring the image tag matched my DockerHub username was crucial for successful CI/CD.

Through this project, I strengthened my understanding of Dockerfile best practices, container security, and automated deployment pipelines.

---

## Conclusion
This assignment gave me hands-on experience with containerization, security hardening, and automation in real-world development workflows. I can now confidently:
- Build secure, lightweight Docker images.
- Use CI/CD pipelines to automate image builds and deployments.
- Manage secrets securely across environments.  

Overall, this project deepened my understanding of how DevOps tools like Docker and GitHub Actions integrate to create efficient and secure software delivery pipelines.
