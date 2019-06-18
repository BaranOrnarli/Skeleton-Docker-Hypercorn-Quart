FROM python:3.7-alpine

# Create a user
RUN adduser -D quart
# Set working directory for the purpose of this Dockerfile
WORKDIR /home/quart

# Copy requirements to the app root
COPY quartapp/requirements.txt ./
RUN apk add --update openssl && \
    rm -rf /var/cache/apk/*
# Create a virtual environment and install the dependecies
RUN openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout key.pem -out cert.pem -subj "/C=US/ST=VA/L=DC/O=OrgName/OU=IT Department/CN=example.com"
RUN pip install --no-cache-dir -r requirements.txt --upgrade && \
  chown -R quart:quart ./

#RUN openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

# Copy the app into our user root
COPY quartapp/ /home/quart/
# Make our entrypoint executable


# Set the user
USER quart
# Set the entrypoint

#ENTRYPOINT ["sh", "./boot.sh"]
CMD ["hypercorn", "--keyfile", "key.pem", "--certfile", "cert.pem", "-b", "0.0.0.0:9000", "server:app"]
