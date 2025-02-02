ARG BUILD_FROM=ghcr.io/hassio-addons/base:latest
FROM $BUILD_FROM

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install required packages
RUN apk add --no-cache python3 py3-pip bash curl \
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir hdate flask

# Copy files into the container
COPY run.sh /run.sh
COPY hebrew_calendar.py /hebrew_calendar.py
COPY ui_override.js /ui_override.js

# Make the script executable
RUN chmod +x /run.sh

# Set entrypoint
CMD [ "/run.sh" ]
