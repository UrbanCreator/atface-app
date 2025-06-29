# Use official Python 3.11 slim image
FROM python:3.11-slim

# Install system dependencies for dlib and face_recognition
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    libboost-python-dev \
    libboost-thread-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy requirements first for cache optimization
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files into container
COPY . .

# Set environment variable for Python unbuffered output (good for logs)
ENV PYTHONUNBUFFERED=1

# Default command to run your app
CMD ["python", "main.py"]
