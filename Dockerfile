# syntax=docker/dockerfile:1

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  build-essential \
  libpq-dev \
  gcc \
  curl \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

# Copy project
COPY . .

# Expose port (default for gunicorn)
EXPOSE 8000

# Environment variables (documented for reference)
# These should be set at runtime (e.g., via docker-compose or docker run -e ...)
# DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
# AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME
# EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USE_TLS
# SECRET_KEY, DEBUG, DATABASE_URL, EMAIL_FROM_EMAIL

# No gunicorn-specific lines remain; daphne will be used via docker-compose command.
