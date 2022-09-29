FROM python:3.10-alpine

# Example line to install pip packages
RUN pip install toml rich

WORKDIR /app

# Default command is to run python with the main script
CMD python /app/main.py

