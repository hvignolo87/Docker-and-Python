# Pull this image from Dockerhub
FROM python:3.8.13-slim

# Also you can pull directly the numpy image
# wich includes Python
# FROM clearlinux/numpy-mp:latest

# Stablish the directory name inside the container
WORKDIR /app

# Copy everything inside this folder to /app inside the container
COPY . .

# Install all dependencies listed in the txt file
RUN pip install -r requirements.txt

# Execute the script
CMD ["python", "/app/app.py"]