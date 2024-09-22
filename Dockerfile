
# Downloading the bas image from docker hub
FROM python:3.9-slim-buster

# Creating the working dir in the base OS
WORKDIR /flask-docker

# Updating the pip command in image 
RUN python3 -m pip install --upgrade pip

# copying all the requirement to the image
COPY requirements.txt requirements.txt

#Installing all the requirements in image OS
RUN pip3 install -r requirements.txt

# Copy all the code files to the image os

COPY . .

CMD ["python3","-m","flask","run","--host=0.0.0.0"]