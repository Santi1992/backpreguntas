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
                    "pregunta": "??Cuanto mide la de Santi?", 
                    "opciones":[
                        {"id":1, "respuestaPosible":"22"},
                        {"id":2, "respuestaPosible":"24"},
                        {"id":3, "respuestaPosible":"23"},
                        {"id":4, "respuestaPosible":"tan enorme que no entro en la regla que tenemos en casa"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "nahh Bolu, mira si la va a tener tan chica"
                    },
                    "msgPersonalizado": "Buenisimo contestaron la primera pregunta, pongan next para avanzar a la siguiente",
                    }
        if str(id) == "2":
            return {"ultima": "15",
                    "pregunta": "??Cu??l fue la primer pel??cula que los novios vieron juntos?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"El Patriota"},
                        {"id":"2", "respuestaPosible":"Dreamgirls"},
                        {"id":"3", "respuestaPosible":"Notting Hill"},
                        {"id":"4", "respuestaPosible":"Diario de una Pasi??n"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Dale panqueques, le mostr?? una mejor como primera, elijan otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta. Fue Notting Hill"
                    }
        if str(id) == "3":
            return {"ultima": "15",
                "pregunta": "??Cu??l fue la primer pelea?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Helado"},
                        {"id":"2", "respuestaPosible":"Santi no lav?? los platos"},
                        {"id":"3", "respuestaPosible":"Ravioles"},
                        {"id":"4", "respuestaPosible":"Ailu tir?? mate en el auto"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Reeee podr??a ser, pero no.. casi je"
                    },
                    "msgPersonalizado": "Santi le sac?? un raviol a Ailu y explot?? todo, pongan next para la siguiente pregunta"
                    }
        if str(id) == "4":
            return {"ultima": "15",
                "pregunta": "Despu??s de Ushuaia Ailu se convirti?? en...", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"La renga chulata"},
                        {"id":"2", "respuestaPosible":"La traga Nieve"},
                        {"id":"3", "respuestaPosible":"La reina de la monta??a"},
                        {"id":"4", "respuestaPosible":"La princesa Castor"},
                        ],
                    "preguntaTramposa": {
                        "id":"2",
                        "msg": "Nieve no...pero... ,  eleg?? otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "5":
            return {"ultima": "15",
                "pregunta": "??Como se llama la empresa de programaci??n de los novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Clover Princess"},
                        {"id":"2", "respuestaPosible":"Marry Me Solutions"},
                        {"id":"3", "respuestaPosible":"Princess Labs"},
                        {"id":"4", "respuestaPosible":"Code Fingers"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "Daaa, que pensas que solo la estrella es Ailin"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "6":
            return {"ultima": "15",
                "pregunta": "En tiempos de guerra, para encontrarse, ??que muralla hab??a que cruzar?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"La muralla China"},
                        {"id":"2", "respuestaPosible":"La General Paz"},
                        {"id":"3", "respuestaPosible":"maipu y lavalle, alto control"},
                        {"id":"4", "respuestaPosible":"Cabildo y congreso"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Estamos en argentina nabolin"
                    },
                    "msgPersonalizado": "Plena cuarentena obligatoria, la general paz estaba minada, pongan next para la siguiente pregunta"
                    }
        if str(id) == "7":
            return {"ultima": "15",
                "pregunta": "??Que es lo que mas le gusta a ailu de santi?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"los rulitos"},
                        {"id":"2", "respuestaPosible":"su culo"},
                        {"id":"3", "respuestaPosible":"sus abominales"},
                        {"id":"4", "respuestaPosible":"su simpat??a"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "Ailu es m??s superficial..... ja"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "8":
            return {"ultima": "15",
                "pregunta": "??Como se llama el arbol q plantaron los novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"el gran arbol"},
                        {"id":"2", "respuestaPosible":"el arbol del amor"},
                        {"id":"3", "respuestaPosible":"tomatero"},
                        {"id":"4", "respuestaPosible":"baby tree"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "Somos mas creativos que eso.... eleg?? otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "9":
            return {"ultima": "15",
                "pregunta": "??Como se va a llamar el perro de la pareja?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"rudolf"},
                        {"id":"2", "respuestaPosible":"baby dog"},
                        {"id":"3", "respuestaPosible":"flash junior"},
                        {"id":"4", "respuestaPosible":"gasparsito"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "diosss, no quedo claro con la anterior pregunta????, eleg?? otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "10":
            return {"ultima": "15",
                "pregunta": "?? Como se va a llamar el perro de los novios cuando crezca ?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"dog abuelo"},
                        {"id":"2", "respuestaPosible":"dog jubilado "},
                        {"id":"3", "respuestaPosible":"dog crecido"},
                        {"id":"4", "respuestaPosible":"dog"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Podr??a haber sido, pero no, quiza en la pr??xima pregunta...... Eleg?? otra."
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "11":
            return {"ultima": "15",
                "pregunta": "??Como se va a llamar el perro de los novios, de super viejo?... na joda, Eleg?? el cronograma correcto", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"match tinder 03/05, noviazgo 06/06"},
                        {"id":"2", "respuestaPosible":"match tinder 19/05, sacada pasaje a cancun 06/06"},
                        {"id":"3", "respuestaPosible":"match tinder 03/05, propuesta 16/06"},
                        {"id":"4", "respuestaPosible":"match tinder 21/05, propuesta 02/09"},
                        ],
                    "preguntaTramposa": {
                        "id":"3",
                        "msg": "mmmm la prouesta es muy cercana, tan manijas no somos"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "12":
            return {"ultima": "15",
                "pregunta": "??A cuantos d??as de conocerse sacaron un pasaje a cancun?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"61"},
                        {"id":"2", "respuestaPosible":"24"},
                        {"id":"3", "respuestaPosible":"43"},
                        {"id":"4", "respuestaPosible":"123"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "somos bastante m??s intensos je, muy in lovee, eleg?? otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "13":
            return {"ultima": "15",
                "pregunta": "?? Que festejan los novios hoy ademas del casamiento?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"Aniversario de novios"},
                        {"id":"2", "respuestaPosible":"Un a??o de conocerse"},
                        {"id":"3", "respuestaPosible":"Compromiso de por vida"},
                        {"id":"4", "respuestaPosible":"Ninguna es correcta"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "siempre una es correcta, eleg?? otra te doy otra oportunidad"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "14":
            return {"ultima": "15",
                "pregunta": "??Cual fue el primer regalo que se hicieron los novios mutuamente?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"un block - un rutini"},
                        {"id":"2", "respuestaPosible":"un llavero - luces"},
                        {"id":"3", "respuestaPosible":"colgador de zapatos - bolsa de vino de 5 litos"},
                        {"id":"4", "respuestaPosible":"caja de forros - lubricante"},
                        ],
                    "preguntaTramposa": {
                        "id":"4",
                        "msg": "que zarpados, eso no era un regalo, era rutina jeje... , eleg?? otra"
                    },
                    "msgPersonalizado": "Esperemos la esten pasando bien en este d??a tan especial, pongan next para la siguiente pregunta"
                    }
        if str(id) == "15":
            return {"ultima": "15",
                "pregunta": "??Quien le pregunto a quien de ser novios?", 
                    "opciones":[
                        {"id":"1", "respuestaPosible":"No hubo pregunta, se dio solo"},
                        {"id":"2", "respuestaPosible":"Ailu a santi"},
                        {"id":"3", "respuestaPosible":"Santi a ailu"},
                        {"id":"4", "respuestaPosible":"Los dos a la vez"},
                        ],
                    "preguntaTramposa": {
                        "id":"1",
                        "msg": "Siempre hay una formalidad.... mas en un contrato como s.a , eleg?? otra"
                    },
                    "msgPersonalizado": "Gracias por jugar, espero saquen un buen resultado!!!!!, aunque no nos importa"
                    }
      