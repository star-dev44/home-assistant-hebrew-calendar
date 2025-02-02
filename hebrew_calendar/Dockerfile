ARG BUILD_FROM=ghcr.io/hassio-addons/base:latest
FROM $BUILD_FROM

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install only essential dependencies first
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    bash \
    curl \
    build-base \
    libffi-dev \
    musl-dev \
    gcc \
    python3-dev \
    openssl-dev

# Upgrade pip and install Python packages
RUN python3 -m ensurepip --upgrade \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir wheel setuptools \
    && pip3 install --no-cache-dir hdate flask

# Copy your custom scripts into the container
COPY run.sh /run.sh
COPY hebrew_calendar.py /hebrew_calendar.py
COPY ui_override.js /ui_override.js

# Make the script executable
RUN chmod +x /run.sh

# Set the entrypoint to run the script
CMD [ "/run.sh" ]
