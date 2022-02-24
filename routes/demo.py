from flask_restx import Namespace, Resource
from domain.entities.GenericRequest import GenericRequest
from useCase.LoginUserAndRetrieveToken import LoginUserAndRetrieveToken
from domain.parsers.GenericRequestParser import GenericRequestParser
from domain.validators.RequesValidator import RequestValidator
from useCase.ObtenerUsuario import ObtenerUsuario
from flask import request
import requests
from config.swagger import demo_obtener_usuario
import os

api = Namespace('app', description='demo route')

@api.route('/login')
class DemoEndpoint(Resource):

    api = api

    def __init__(self, restx_placeholder_param=None, request_parser=GenericRequestParser(), request_validator=RequestValidator(), use_case=LoginUserAndRetrieveToken()):
        self.request_parser: GenericRequestParser = request_parser
        self.request_validator: RequestValidator = request_validator
        self.login_user_and_retrieve_token: LoginUserAndRetrieveToken = use_case
        super().__init__(self.api)

    @api.expect()
    def post(self):

        genericRequest: GenericRequest = self.request_parser.parse_request(request)

        self.request_validator.login_endpoint_validate(genericRequest)

        token = self.login_user_and_retrieve_token.execute(genericRequest)

        return {"data": token}, 200

@api.route('/obtainquestion/<id>')
class DemoEndpoint2(Resource):

    api = api

    def __init__(self, restx_placeholder_param=None, request_parser=GenericRequestParser(), request_validator=RequestValidator()):
        self.request_parser: GenericRequestParser = request_parser
        self.request_validator: RequestValidator = request_validator
        super().__init__(self.api)

    def get(self, id):

        genericRequest: GenericRequest = self.request_parser.parse_request(request)

        self.request_validator.generic_validate(genericRequest)

        print(genericRequest.dataToken)
        print(genericRequest.dataToken)

        if str(id) == "1":
            return {"pregunta": "¿Qué le regalo nico a cami por la propuesta?", 
                    "opciones":[
                        {"id":1, "respuestaPosible":"Unos Aritos"},
                        {"id":2, "respuestaPosible":"Un portaRetratos"},
                        {"id":3, "respuestaPosible":"Un Termo"},
                        {"id":4, "respuestaPosible":"Un vaso térmico"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "nahh Bolu, no habia plata, elegí otra"
                    },
                    "msgPersonalizado": "Buenisimo contestaron la primera pregunta, pongan next para avanzar a la siguiente",
                    }
        if str(id) == "2":
            return {"pregunta": "¿Cuál es el deporte favorito de nico?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Rugby"},
                        {"id":"2", "respuestaPosible":"Futbol"},
                        {"id":"3", "respuestaPosible":"Basquet"},
                        {"id":"4", "respuestaPosible":"Jugar a la escondida"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "Nico ya creció, no sos gracioso"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "3":
            return {"pregunta": "¿Cuál es el Cuñado favorito de nico?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Ailin"},
                        {"id":"2", "respuestaPosible":"Santi"},
                        {"id":"3", "respuestaPosible":"Gisela"},
                        {"id":"4", "respuestaPosible":"No tiene"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "Alto salame, gisela es la suegra!"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }

@api.route('/obtainquestion/prueba')
class Prueba(Resource):

    api = api

    def __init__(self, restx_placeholder_param=None, request_parser=GenericRequestParser(), request_validator=RequestValidator()):
        self.request_parser: GenericRequestParser = request_parser
        self.request_validator: RequestValidator = request_validator
        super().__init__(self.api)
    
    def get(self):

        print(request.headers, flush=True)

        return {"response":"funcionando"}


@api.route('/obtainquestion/prueba2')
class Prueba(Resource):

    api = api

    def __init__(self, restx_placeholder_param=None, request_parser=GenericRequestParser(), request_validator=RequestValidator()):
        self.request_parser: GenericRequestParser = request_parser
        self.request_validator: RequestValidator = request_validator
        super().__init__(self.api)
    
    def get(self):

        algo = requests.get("http://http://52.200.8.58/5000/")

        return algo.json()