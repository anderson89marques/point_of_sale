# Dockerfile

# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy project
COPY . /code/

WORKDIR /code

RUN pip install -r point_of_sale/requirements/dev_requirements.txt

EXPOSE 8000

