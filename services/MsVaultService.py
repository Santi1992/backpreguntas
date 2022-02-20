from domain.entities.InputRequest import InputRequest
from repository.locals.ClientsUrl import ClientsUrl
from repository.clients.RequestWrapper import RequestWrapper
from domain.parsers.InputRequestParser import InputRequestParser

class MsVaultService(RequestWrapper):

    def __init__(self, clientsUrl: ClientsUrl= ClientsUrl(), inputRequestParser=InputRequestParser() ) -> None:
        self.client: ClientsUrl = clientsUrl
        self.reqParser: InputRequestParser = inputRequestParser
        super().__init__()
    
    def guardar_clave_usuario(self):
        inputRequest :InputRequest = self.create_input_request()
        response, status = self.get(self.client.DEMO_GET_USUARIO,inputRequest)
        return response

    def create_input_request(self):
        return self.reqParser.parse()
    
    def prueba(self):
        return self.client.DEMO_GET_USUARIO
        


    
        
        