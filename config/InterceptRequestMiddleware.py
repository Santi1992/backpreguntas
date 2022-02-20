from datetime import datetime
from werkzeug.wrappers import Request, Response
import json
import uuid
from flask import g

class InterceptRequestMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app
    
    def unauthorized_response(self, environ, start_response):
        header = {}   
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = '*'
        header['Access-Control-Allow-Methods'] = '*'
        return Response('Authorization failed', mimetype='text/plain', status=401, headers=header)(environ, start_response)

    def __call__(self, environ, start_response):
        uid = uuid.uuid4()
        environ['HTTP_X_REQUEST_ID'] = uid
        environ['HTTP_DATE'] = datetime.now()
        request = Request(environ) # Method  y path 
        return self.wsgi_app(environ, start_response)
