# Skeleton Docker Hypercorn Quart

A Skeleton or Boilerplate for a Python 3.7+ asynchronous Web App Microframework API with Quart, Hypercorn as a server to deliver HTTP/2, and Docker to tie it all together

# Hypercorn ASGI Server & Quart Python Microframework

ASGI (Asynchronous Server Gateway Interface) based web server that can transmit HTTP/2 (h2) packets that are encrypted with TLS and in a binary format making it faster than HTTP 1. Quart is a Python framework based upon Flask Python (and in competition with Starlette and FastAPI, although Quart more closely follows Flask).

***Note: Do not use self-signed certificate in this example in a production environment.***

*However, if it is firewalled off and only accessible internally between servers you own as a cluster, then self-signed certificates can be utilized as new keys are generated every time the docker is built*

# Installation

**Create a .env file in the root directory.**

Open Powershell or your favorite shell and use:

`docker-compose -p ProjectName build`

`docker-compose -p ProjectName up`

Then visit https://localhost:9000/

# Information

More information on Quart (an asynchronous enabled web microframework based off of Flask):

https://pgjones.gitlab.io/quart/

More information on Quart OpenAPI:

https://factset.github.io/quart-openapi/

