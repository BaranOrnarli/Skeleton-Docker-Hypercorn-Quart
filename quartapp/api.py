from quart_openapi import Pint, Resource
from quart import jsonify, request

app = Pint(__name__, title='Spectacular Hypercorn Quart Application Skeleton')

expected = app.create_validator('sample_request', {
  'type': 'object',
  'properties': {
    'foobar': {
      'type': 'string'
    },
    'baz': {
      'oneOf': [
        { 'type': 'integer' },
        { 'type': 'number', 'format': 'float' }
      ]
    }
  }
})

@app.route('/')
class Root(Resource):
  async def get(self):
    '''Note Route

    This docstring will show up as the description and short-description
    for the openapi docs for this route.
    '''
    return jsonify({"Note": "There exists a localhost:9000/openapi.json that can be helpful here"})
  @app.expect(expected)
  async def post(self): 
    '''Post Hello Route

    Data should be sent through postman (but postman does not have HTTP/2, for that you need `curl --http2`) with HTTPS POST "1": { "foobar": "super", "baz": 5.56 }
    '''
    data = await request.get_json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='localhost', 
        port=8080, 
        certfile='cert.pem', 
        keyfile='key.pem')
