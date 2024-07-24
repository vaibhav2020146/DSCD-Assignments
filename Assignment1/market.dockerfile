# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 50051 available to the world outside this container
EXPOSE 50051

# Define environment variable
ENV NAME market_server

# Run market_server.py when the container launches
CMD ["python", "./market_server.py"]
