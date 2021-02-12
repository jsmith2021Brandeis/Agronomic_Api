# Use an official Python runtime as an image
FROM python:3.7

# The EXPOSE instruction indicates the ports on which a container
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5000

WORKDIR /bare-bones-api

VOLUME ["/bare-bones-api"]

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist

# Install any needed packages specified in requirements.txt
RUN pwd
RUN ls -aslh
COPY requirements.txt /bare-bones-api/
RUN pip install -r requirements.txt

# Run app.py when the container launches
##COPY app.py /app
CMD python /bare-bones-api/app.py
