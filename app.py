from bottle import route, run, template
import json

@route('/')
def index():
    from bottle import response
    from json import dumps
    msg = [{"message1": "Hello, world!"}]
    response.content_type = 'application/json'
    return dumps(msg)

run(host='localhost', port=8080)
