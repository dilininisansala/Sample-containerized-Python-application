# Sample-containerized-Python-application
Sample containerized Python application for demo purposes

# Step 1.	Create the Python Script
Write a simple Python script (e.g., app.py) that you want to containerize.

# Step 2. Create a Dockerfile
The Dockerfile tells Docker how to build and run your application in a container. Create a Dockerfile in the same directory as your Python script.

# Step 3. Build the Docker Image
Once your Dockerfile is ready, you can build your Docker image by running the following command in the terminal:

docker build -t my-dockerized-python .

# Step 4. Test the Docker Container Locally
After building the image, test it locally by running the following

docker run my-dockerized-python

# Repository structure
The main files in this repository are:
dockerfile - Specifies how the application is built and packaged
app.py - Python application
.dockerignore - This file tells Docker which files or directories it should ignore when building the image.
