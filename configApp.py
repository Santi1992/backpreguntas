from datetime import datetime
from nacl.public import PrivateKey, SealedBox
import nacl.encoding
from flask import Flask, jsonify, request, g
from domain.entities.InputSaveLog import InputSaveLog
from dotenv import load_dotenv
from config.errorHandler import register_error_handlers
from config.exceptions import RequestException
from config.InterceptRequestMiddleware import InterceptRequestMiddleware
from flask_cors import CORS
import os
import sys

from services.MsEntornoService import MsEntornoService

#entorno = None

ENVS = {
    "local":".env",
    "dev": "dev.env",
    "homo": "homo.env",
    "prod": "prod.env",
}

def gunicorn_execution(env):
    if env not in ENVS:
        exit("Please specify a valid environment : local, dev, homo, prod")
    load_dotenv(ENVS[env])
        
def python_execution():
    if len(sys.argv) == 2 and sys.argv[1] in ENVS:
        load_dotenv(ENVS[sys.argv[1]])
    else:
        exit("Please specify a valid environment : local, dev, homo, prod")


def create_app(env=None):

    entorno = None

    if env==None:
        python_execution()
    else:
        gunicorn_execution(env)
    
    if env != None:
        entorno = env
    else:
        entorno = sys.argv[1]
    
    from register import api
    from services.MsLogService import MsLogService
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # msEntornoService:MsEntornoService = MsEntornoService(entorno=entorno)
    # envsToLoad = msEntornoService.obtain_credentials("local", "SQL_ITSHOP")
    # load_envs_from_credenitals(envsToLoad)

    app.wsgi_app = InterceptRequestMiddleware(app.wsgi_app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    api.init_app(app)
    app.url_map.strict_slashes = False

    @app.before_request
    def before_request():

        if request.method == "OPTIONS":
            return jsonify({"message":"ok"})

        apiKey = request.headers.get("X-API-KEY", None)
        if apiKey != "sdgkjkhs23576@23892v":
            return jsonify({"Access":"No autorizado"}),401

        log_service: MsLogService = MsLogService(entorno=entorno)
        g.clientUID = request.args.get("userUID", None)
        g.useUid = request.args.get("clientUID", None)
        g.userName = request.args.get("userName", None)
        g.uidRequest = request.environ['HTTP_X_REQUEST_ID']
        g.httpNow = request.environ['HTTP_DATE']
        g.entorno = entorno

        inputSaveLog : InputSaveLog = InputSaveLog().set_service_uid(
            "1ef9e556-94e2-4ea2-8147-b80081140775"  #msTemplate
        ).set_client_uid(
            "1" #REDLINK g.clientUID ---> VIENE DEL REQUEST!!!
        ).set_user_uid(
            "g.useUid" # CAMBIAR!!!!!!!!!!!!!!!!
        ).set_log_uid(
            g.uidRequest
        ).set_endpoint(
            request.endpoint
        ).set_payload(
            {
                "method": request.method,
                "headers": "Customizar",
                "parameters":  {
                    "bodyParams": request.json,
                    "queryParams": request.args
                },
                "origin":  request.remote_addr,
            }
        )
        # if request.endpoint != None:
        #     log_service.save_log(inputSaveLog)

    @app.after_request
    def after_request(response):
        log_service: MsLogService = MsLogService(entorno=entorno)
        # """response.headers.add('Access-Control-Allow-Origin', '*')
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        # response.headers.add('Access-Control-Allow-Credentials', 'true')"""
        g.useUid = request.args.get("userUID", None)
        g.userName = request.args.get("userName", None)
        g.uidRequest = request.environ['HTTP_X_REQUEST_ID']
        g.httpNow = request.environ['HTTP_DATE']
        response_time_now = datetime.now()
        duration = (response_time_now - g.httpNow).total_seconds()

        if response.json == None:
            return response

        inputSaveLog : InputSaveLog = InputSaveLog().set_service_uid(
            "1ef9e556-94e2-4ea2-8147-b80081140775"  #msTemplate
        ).set_client_uid(
            "1"  #REDLINK
        ).set_user_uid(
            "g.useUid" # CAMBIAR!!!!!!!!!!!!!!!!
        ).set_log_uid(
            g.uidRequest
        ).set_payload(
            {
                "result": response.json,
                "statusCode": response.status_code,
                "duration": duration
            }
        )

        #log_service.save_log(inputSaveLog)
        return response

    register_error_handlers(app)
    return app

def load_envs_from_credenitals(responseService):

    unbox : SealedBox = SealedBox(
    PrivateKey("39001a4bf846ba219406905ff3a6073a4f4e490de05a1b242e35919c760050f9", 
    encoder=nacl.encoding.HexEncoder)
    )
    
    for i in responseService:
        cred_to_connect = responseService[i]
        for j in cred_to_connect:
            os.environ[j]=unbox.decrypt(bytes.fromhex(cred_to_connect[j])).decode('utf-8')
