# Simple, reproducible Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (curl only for healthchecks / debug)
RUN apt-get update && apt-get install -y --no-install-recommends     curl  && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy app
COPY . /app

# Default command runs the pipeline once
CMD ["python", "-m", "src.pipeline"]
