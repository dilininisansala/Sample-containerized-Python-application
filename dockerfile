# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app   

# Step 3: Copy everything from the current directory to /app in the container
COPY . .

# Step 4: Run app.py when the container launches
CMD ["python", "app.py"]


