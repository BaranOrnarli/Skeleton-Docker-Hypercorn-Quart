# SkeletonDockerHypercornQuart
A Skeleton for a Python 3.7 asyncio based API with Quart, Hypercorn as a server to deliver HTTP/2, and Docker to tie it all together

***Note: Do not use a self-signed certificate as in this example in a production environment.***

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

