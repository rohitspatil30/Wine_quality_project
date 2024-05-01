# End-to-end ML Project

This project demonstrates an end-to-end Machine Learning (ML) pipeline, including data processing, model training, and deployment using AWS services and GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD).

## Workflows

1. **update config.yaml**: Update the configuration file for the ML project.
2. **update schema.yaml**: Update the schema file for the ML project.
3. **update params.yaml**: Update the parameters file for the ML project.
4. **update the entity**: Update the entity classes for the ML project.
5. **update the configuration manager in src config**: Update the configuration manager in the source code configuration.
6. **update the components**: Update the components used in the ML project.
7. **update the pipeline**: Update the pipeline for the ML project.
8. **update the main.py**: Update the main Python script for the ML project.
9. **update the app.py**: Update the Flask application script for the ML project.

## How to Run?

Follow these steps to run the ML project:

1. Create a conda environment:
   ```bash
   conda create -n mlproj python=3.8 -y
   conda activate mlproj
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://0.0.0.0:8080` to access the application.

## AWS CI/CD Deployment with GitHub Actions

1. **Login to AWS console**: Log in to your AWS account.

2. **Create IAM user for deployment**:
   - Create a new IAM user with the necessary permissions for deployment.
   - Assign policies like `AmazonEC2ContainerRegistryFullAccess` and `AmazonEC2FullAccess` to the IAM user.

3. **EC2 access**: Set up an EC2 instance (virtual machine) to host your application.

4. **ECR**: Set up an Elastic Container Registry to store your Docker images in AWS.

5. **Description**:
   - This deployment process involves building a Docker image of your source code, pushing the image to ECR, launching an EC2 instance, pulling the image from ECR to the EC2 instance, and finally running the Docker image in the EC2 instance.

6. **Create ECR repo**:
   - Create an ECR repository to store your Docker image.
   - Save the ECR URI: `136566696263.dkr.ecr.us-east-1.amazonaws.com/mlproject`.

7. **Create EC2 machine (Ubuntu)**: Create an EC2 instance with Ubuntu as the operating system.

8. **Install Docker in EC2 Machine** (optional):
   ```bash
   sudo apt-get update -y
   sudo apt-get upgrade
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

9. **Configure EC2 as self-hosted runner**:
   - In the AWS console, navigate to `Setting > Actions > Runner > New Self-hosted Runner`.
   - Choose the operating system and follow the instructions to run the command on the EC2 instance.

10. **Setup GitHub secrets**:
    - Set up the following GitHub secrets in your repository:
      - `AWS_ACCESS_KEY_ID`
      - `AWS_SECRET_ACCESS_KEY`
      - `AWS_REGION`
      - `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com`)
      - `ECR_REPOSITORY_NAME` (e.g., `simple-app`)

11. **Deploy the Application**:
    - Update your CI/CD workflow to build and push the Docker image to ECR, and then deploy it to the EC2 instance.


