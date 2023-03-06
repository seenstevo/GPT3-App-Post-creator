# Use an official Python runtime as a parent image
FROM python:3.7.4-slim-buster

# We need to pass the AWS log in details during the Docker image build
ARG DB_HOST
ARG DB_PORT
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_DATABASE

# Set the environment variables
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_USERNAME=$DB_USERNAME
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_DATABASE=$DB_DATABASE

# Set the working directory to /app
WORKDIR /gpt3app

# Copy the current directory contents into the container at /app
COPY /gpt3app /gpt3app
COPY requirements.txt /gpt3app


# Install any things relating to the database
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]