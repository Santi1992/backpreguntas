from flask_restx import Namespace, Resource
from domain.entities.GenericRequest import GenericRequest
from useCase.LoginUserAndRetrieveToken import LoginUserAndRetrieveToken
from domain.parsers.GenericRequestParser import GenericRequestParser
from domain.validators.RequesValidator import RequestValidator
from useCase.ObtenerUsuario import ObtenerUsuario
from useCase.GetResults import GetResults
from flask import request
import requests
from config.swagger import demo_obtener_usuario
import os
import random

from useCase.SaveResult import SaveResult

api = Namespace('api', description='demo route')

@api.route('/getresults')
class Result(Resource):

    api = api

    def __init__(self, restx_placeholder_param=None, request_parser=GenericRequestParser(), request_validator=RequestValidator(), use_case=GetResults()):
        self.request_parser: GenericRequestParser = request_parser
        self.request_validator: RequestValidator = request_validator
        self.getResults: GetResults() = use_case
        super().__init__(self.api)

    @api.expect()
    def get(self):

        genericRequest: GenericRequest = self.request_parser.parse_request(request)

        self.request_validator.generic_validate(genericRequest)
        
        result = self.getResults.execute(genericRequest)

        return {"message": result}

@api.route('/saveresult')
class Result(Resource):

    api = api

    def __init__(self, restx_placeholder_param=None, request_parser=GenericRequestParser(), request_validator=RequestValidator(), use_case=SaveResult()):
        self.request_parser: GenericRequestParser = request_parser
        self.request_validator: RequestValidator = request_validator
        self.save_result: SaveResult = use_case
        super().__init__(self.api)

    @api.expect()
    def post(self):

        genericRequest: GenericRequest = self.request_parser.parse_request(request)

        self.request_validator.generic_validate(genericRequest)

        res = self.save_result.execute(genericRequest)

        if res == "error":
            return {"msg":"error"}, 500

        return {"data": res}, 200

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

        if str(id) == "1":
            return {"ultima": "15",
                    "pregunta": "¿Quién se enamoro primero?", 
                    "opciones":[
                        {"id":1, "respuestaPosible":"Ninguno"},
                        {"id":2, "respuestaPosible":"Los dos a la vez"},
                        {"id":3, "respuestaPosible":"Camila"},
                        {"id":4, "respuestaPosible":"Nico"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "nahh Bolu, nos estamos casando, no jodas"
                    },
                    "msgPersonalizado": "Buenisimo contestaron la primera pregunta, pongan next para avanzar a la siguiente",
                    }
        if str(id) == "2":
            return {"ultima": "15",
                    "pregunta": "¿Cuál fue la primer película que los novios vieron juntos?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"9 reinas"},
                        {"id":"2", "respuestaPosible":"Corazon de leon"},
                        {"id":"3", "respuestaPosible":"This is it"},
                        {"id":"4", "respuestaPosible":"Batman"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "Cami no vio ninguna de batman!, elegi otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "3":
            return {"ultima": "15",
                "pregunta": "¿Quién cocina más rico?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Los dos por igual"},
                        {"id":"2", "respuestaPosible":"Cami"},
                        {"id":"3", "respuestaPosible":"Nico"},
                        {"id":"4", "respuestaPosible":"Ninguno, aguante rapi"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Siempre alguien es mejor, volve a elegir!"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "4":
            return {"ultima": "15",
                "pregunta": "¿De qué equipo de fútbol son los novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Los dos de riBer"},
                        {"id":"2", "respuestaPosible":"Boca nico- River cami"},
                        {"id":"3", "respuestaPosible":"River nico- Cami san lorenzo"},
                        {"id":"4", "respuestaPosible":"River nico- Boca cami"},
                        ],
                    "preguntaTramposa": {
                        "id":"2",
                        "msg": "Dale boludo no viste todos los buzos que tiene nico, elegi otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "5":
            return {"ultima": "15",
                "pregunta": "¿Cuantos gatos tienen los novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"1"},
                        {"id":"2", "respuestaPosible":"2"},
                        {"id":"3", "respuestaPosible":"3"},
                        {"id":"4", "respuestaPosible":"4"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "Dale que somos los locos de los gatos, elegi otra!"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "6":
            return {"ultima": "15",
                "pregunta": "¿Como se llama el primer gato que tuvieron los novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"muñeco"},
                        {"id":"2", "respuestaPosible":"leia"},
                        {"id":"3", "respuestaPosible":"Enzo"},
                        {"id":"4", "respuestaPosible":"ivael"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "No elegimos nombres tan horribles, elegi otro!"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "7":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "8":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "9":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "10":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "11":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "12":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "13":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "14":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
        if str(id) == "15":
            return {"ultima": "15",
                "pregunta": "¿Cuál es el Cuñado favorito de nico?", 
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
      