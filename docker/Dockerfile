FROM ubuntu:20.04

LABEL mainteiner = "Andrea Juárez Munguia"
LABEL version = "v1"
LABEL description = "Save, Load and Copy"

RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y sqlite3

# Define ENV files
ENV requirements docker/requirements.txt

# Copy requirements file
COPY requirements.txt ${requirements}

# Install python packages
RUN pip3 install -r docker/requirements.txt
