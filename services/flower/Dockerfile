# Pull official base image
FROM python:3.7-slim-buster
# Set work directory
WORKDIR /usr/src/app
# Set envrionment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONBUFFERED 1
# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential libssl-dev libffi-dev python-dev

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# Copy project
COPY . /usr/src/app/
# # Run entrypoint
ENTRYPOINT ["flower"]