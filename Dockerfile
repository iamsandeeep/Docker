From ubuntu:latest

# set the working directory
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app 

# install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y python3 python3-pip
#RUN pip3 install --no-cache-dir -r requirements.txt

#set environment variables
ENV NAME World

# Run the application:
CMD ["python3", "app.py"]
