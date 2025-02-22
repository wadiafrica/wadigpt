# Use a slim Python 3.10 base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for building Python packages and Nginx
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    ninja-build \
    g++ \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install ctransformers with no prebuilt binary
RUN pip install ctransformers

# Copy the rest of the application code into the container
COPY . .

# Copy Nginx configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the ports for HTTP (80) and HTTPS (443)
EXPOSE 80 443

# Start Nginx and FastAPI app using Uvicorn
CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port 8000
