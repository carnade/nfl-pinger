# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests

# Make the script executable
RUN chmod +x nfl-pinger.py

# Run the pinger script when the container launches
CMD ["python", "nfl-pinger.py"]

