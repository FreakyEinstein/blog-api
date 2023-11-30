# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry and project dependencies
RUN pip install poetry
RUN pip install fastapi uvicorn
RUN poetry install

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run the application using uvicorn with the specified command and environment variables
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]