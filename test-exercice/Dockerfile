# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the main.py file into the container
COPY main.py /app/
COPY operations.py /app/
COPY __init__.py /app/


# Command to run the FastAPI application within the container
CMD ["python", "main.py"]