ARG BUILD_FROM=ghcr.io/hassio-addons/base:latest
FROM $BUILD_FROM

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install basic dependencies first
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Install dependencies one by one to isolate the issue
RUN apk add --no-cache curl
RUN apk add --no-cache build-base
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache musl-dev
RUN apk add --no-cache gcc
RUN apk add --no-cache python3-dev
RUN apk add --no-cache openssl-dev

# Upgrade pip and install Python packages with verbose output
RUN python3 -m ensurepip --upgrade \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -v wheel setuptools \
    && pip3 install --no-cache-dir -v hdate flask

# Copy your custom scripts into the container
COPY run.sh /run.sh
COPY hebrew_calendar.py /hebrew_calendar.py
COPY ui_override.js /ui_override.js

# Make the script executable
RUN chmod +x /run.sh

# Set entrypoint to run the script
CMD [ "/run.sh" ]
