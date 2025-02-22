# Use a slim Python 3.10 base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \      
    cmake \                  
    ninja-build \            
    g++ \               
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Install ctransformers with no prebuilt binary
RUN pip install ctransformers

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 8000

# Set the default command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
