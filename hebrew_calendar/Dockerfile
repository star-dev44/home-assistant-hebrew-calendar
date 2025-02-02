# Base image for Home Assistant Add-ons
ARG BUILD_FROM=ghcr.io/hassio-addons/base:latest
FROM $BUILD_FROM

# Set the shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Python and dependencies
RUN apk add --no-cache python3 py3-pip \
    && pip3 install hdate flask

# Copy our custom scripts into the container
COPY run.sh /run.sh
COPY hebrew_calendar.py /hebrew_calendar.py
COPY ui_override.js /ui_override.js

# Make the script executable
RUN chmod a+x /run.sh

# Set the entry point
CMD [ "/run.sh" ]
