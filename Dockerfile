# Use the official Python image as the base image
FROM python:3-slim

# Set the working directory
WORKDIR /bot

# Copy the entire app directory to the container
COPY ./requirements.txt .

# Install Python packages from requirements file
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./telegram_bot /bot

# run some command
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

# Specify the command to run when the container starts
CMD ["python", "telegramBot.py"]
