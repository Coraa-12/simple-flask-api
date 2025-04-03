# Use an official lightweight Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Inform Docker that the container listens on port 5000 at runtime
EXPOSE 5000

# Command to run the application using gunicorn when the container starts
# Binds to 0.0.0.0 to be accessible from outside the container
# app:app tells gunicorn to look for the 'app' object inside the 'app.py' file
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]