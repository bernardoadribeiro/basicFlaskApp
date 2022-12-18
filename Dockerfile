# syntax=docker/dockerfile:1

# Set the official Python docker image
FROM python:3.11-slim-buster

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all files of app to image
COPY . .

# Run flask app
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"] 