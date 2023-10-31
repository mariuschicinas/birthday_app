# Use the official Python image as the base image
FROM python:3.8

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
#RUN pip install -r requirements.txt
RUN pip install -r requirements.txt python-dotenv

# Copy the Flask application code into the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
