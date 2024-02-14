# Use the official Python image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /bot

# Copy the entire app directory to the container
COPY ./requirements.txt .

# Install Python packages from requirements file
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./telegram_bot /bot

# Specify the command to run when the container starts
CMD ["python", "telegramBot.py"]
