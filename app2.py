from bottle import route, run, template


@route('/')
def index():
    msg = {"message1": "Hello, world!"}
    return dict(msg)

run(host='localhost', port=8080)