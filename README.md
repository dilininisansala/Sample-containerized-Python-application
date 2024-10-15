# Sample-containerized-Python-application
Sample containerized Python application for demo purposes

# Repository structure
The main files in this repository are:
* dockerfile - Specifies how the application is built and packaged
* app.py - Python application
* .dockerignore - This file tells Docker which files or directories it should ignore when building the image.

# Step 1.	Create the Python Script
Write a simple Python script (e.g., app.py) that you want to containerize.

# Step 2. Create a Dockerfile
The Dockerfile tells Docker how to build and run your application in a container. Create a Dockerfile in the same directory as your Python script.

# Step 3. Build the Docker Image
Once your Dockerfile is ready, you can build your Docker image by running the following command in the terminal:

docker build -t my-dockerized-python .

![1](https://github.com/user-attachments/assets/4cdee44c-7b7e-40f4-b1a0-a1e6f1d81307)


# Step 4. Test the Docker Container Locally
After building the image, test it locally by running the following

docker run my-dockerized-python

Before building a Docker image through Visual Studio Code, you should launch Docker Desktop to ensure Docker is running properly. Make sure Docker Desktop is running.

# Step 5. Check the Build in Docker Desktop
After building, you can go to Docker Desktop and see the newly created image under the Images tab.

![2](https://github.com/user-attachments/assets/532ec4d7-0baa-4422-aea8-d6ccb401f83e)

Once you've built the Docker image, you can run the image to create and run a container.

![3](https://github.com/user-attachments/assets/53675f04-027e-481d-8d4e-937cf637f096)
