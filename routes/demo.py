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
                "pregunta": "¿ Cómo se llamaron los primeros perros que tuvieron Cami y Nico en su infancia?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Luna-Archie."},
                        {"id":"2", "respuestaPosible":"Flash- Lola."},
                        {"id":"3", "respuestaPosible":"Luna-Lola"},
                        {"id":"4", "respuestaPosible":"Flash-Archie."},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "Esta no es !!, por esta vez selecciona otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "5":
            return {"ultima": "15",
                "pregunta": "¿Como se llama el primer gato que tuvieron los novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Muñeco"},
                        {"id":"2", "respuestaPosible":"Iavel |||"},
                        {"id":"3", "respuestaPosible":"River"},
                        {"id":"4", "respuestaPosible":"Pity"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Esta no es, pero fue nuestra segunda opción"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "6":
            return {"ultima": "15",
                "pregunta": "¿Quién suele olvidarse de darle de tomar agua a los gatos?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Cami"},
                        {"id":"2", "respuestaPosible":"Nico"},
                        {"id":"3", "respuestaPosible":"Nadie se olvida, ambos les damos agua y comida por igual"},
                        {"id":"4", "respuestaPosible":"Los gatos toman agua del inohodoro"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "A veces pasa jajaja , pero no es, elegí otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "7":
            return {"ultima": "15",
                "pregunta": "¿En qué año se pusieron de novios Cami y Nico?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"2012"},
                        {"id":"2", "respuestaPosible":"2013"},
                        {"id":"3", "respuestaPosible":"2014"},
                        {"id":"4", "respuestaPosible":"2008"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "esta no es elegí otra, no nos dan la cuenta"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "8":
            return {"ultima": "15",
                "pregunta": "¿A qué club fueron Cami y Nico de chicos?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Club Hacoaj-Club Ciudad"},
                        {"id":"2", "respuestaPosible":"Club Nahuel-GEBA"},
                        {"id":"3", "respuestaPosible":"Club Hacoaj-GEBA"},
                        {"id":"4", "respuestaPosible":"Club Nahuel-Club Ciudad"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Podría haber sido pero no"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "9":
            return {"ultima": "15",
                "pregunta": "¿Qué día cumplen años Cami y Nico?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"18/07 - 06/01"},
                        {"id":"2", "respuestaPosible":"18/07 - 07/01"},
                        {"id":"3", "respuestaPosible":"28/07 - 07/01"},
                        {"id":"4", "respuestaPosible":"28/07 - 06/01"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "trampita, muchos piensan que Nico cumple años el 06, no te confundas, elegí otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "10":
            return {"ultima": "15",
                "pregunta": "¿Qué se regalaron los novios para el festejo de los 6 meses ( en aquella epoca se festejaban los meses ♡)", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Una camiseta de river-unos aritos"},
                        {"id":"2", "respuestaPosible":"Conjunto sexy-paletas de ping pong "},
                        {"id":"3", "respuestaPosible":"dvd de la primer pelicula que vieron-anillo de compromiso"},
                        {"id":"4", "respuestaPosible":"No se regalaron nada :( "},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Podría haber sido, pero no. Elegí otra."
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "11":
            return {"ultima": "15",
                "pregunta": "¿A qué jardín de infantes fueron Cami y Nico?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Pipoca-Peter Pan"},
                        {"id":"2", "respuestaPosible":"Tarbut-Peter Pan"},
                        {"id":"3", "respuestaPosible":"Sholem-Northbridge"},
                        {"id":"4", "respuestaPosible":"Tarbut-Northbridge"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "trampita, Cami si fue al Sholem unos años :)), elegí otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "12":
            return {"ultima": "15",
                "pregunta": "¿Quién de la pareja habla más?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Nico"},
                        {"id":"2", "respuestaPosible":"Cami"},
                        {"id":"3", "respuestaPosible":"Los dos por igual"},
                        {"id":"4", "respuestaPosible":"Ninguno habla mucho"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Realmente pusiste nico?? En qué momento lo escuchaste hablar más que a Cami?), elegí otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "13":
            return {"ultima": "15",
                "pregunta": "¿ Ante una discusión, siempre uno de los novios es el primero en pedir perdón. Quién es?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Cami"},
                        {"id":"2", "respuestaPosible":"Nico"},
                        {"id":"3", "respuestaPosible":"Los novios nunca discuten"},
                        {"id":"4", "respuestaPosible":"Los novios no se perdonan"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "jaja claro claro, ya quisieras, elegí otra te doy otra oportunidad"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "14":
            return {"ultima": "15",
                "pregunta": "¿A qué país de Europa los novios no fueron juntos?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Italia"},
                        {"id":"2", "respuestaPosible":"España"},
                        {"id":"3", "respuestaPosible":"Reino Unido"},
                        {"id":"4", "respuestaPosible":"República checa"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "estuvieron en Praga. Experiencias inolvidables con los borrachos de la calle escupiendo a la novia, elegí otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "15":
            return {"ultima": "15",
                "pregunta": "¿A dónde van los novios de luna de miel?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"México"},
                        {"id":"2", "respuestaPosible":"Colombia"},
                        {"id":"3", "respuestaPosible":"Brasil"},
                        {"id":"4", "respuestaPosible":"Perú"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "yy este es un viaje pendiente, pero queremos playita bebe!!"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este día tan especial, pongan next para la siguiente pregunta"
                    }
      