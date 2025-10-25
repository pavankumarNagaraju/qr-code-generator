\# Reflection on Dockerizing the QR Code Generator



This project helped me understand how to securely containerize an application and automate deployment using Docker and GitHub Actions.



By creating a non-root user (`myuser`), I improved container security, ensuring the app runs with minimal privileges. The use of `python:3.12-slim-bullseye` reduced image size and vulnerability exposure. I also used `.dockerignore` to avoid including unnecessary files like virtual environments and logs.



Setting up GitHub Actions taught me how CI/CD pipelines automate image building and pushing to DockerHub. Handling secrets (`DOCKERHUB\_USERNAME`, `DOCKERHUB\_TOKEN`) securely was essential for this process.



The main challenge was configuring volume mounts on Windows; PowerShell path formatting (`${PWD}\\qr\_codes`) solved it. I also verified the container runs both locally and from DockerHub successfully.



Overall, this assignment gave me hands-on experience in secure Dockerization, automation, and reproducibility.



