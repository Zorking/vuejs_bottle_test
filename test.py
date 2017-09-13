import os
from bottle import route, run, template, static_file

@route('/')
def hello():
    return server_static('index.html')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.getcwd())

run(host='localhost', port=8000, debug=True)
