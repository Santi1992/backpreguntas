from domain.entities.InputRequest import InputRequest
from domain.entities.InputSaveLog import InputSaveLog
from repository.clients.RequestWrapper import RequestWrapper
from domain.parsers.InputRequestParser import InputRequestParser

class MsEntornoService(RequestWrapper):

    URLS = {
        "local":"http://localhost:5000/entorno/obtenervariables",
        "homo" :"http://172.16.208.37:8106/entorno/obtenervariables"
    }
    API_KEY_DESA = "7fhn_FCa,[L`!2U=3214"

    def __init__(self, entorno, inputRequestParser=InputRequestParser()) -> None:
        self.entorno = entorno
        self.reqParser: InputRequestParser = inputRequestParser
        super().__init__()

    def obtain_credentials(self, env, listStringCredentials):
        inputRequest: InputRequest = self.create_input_request(env, listStringCredentials)
        response, status = self.get(self.URLS[self.entorno], inputRequest)
        return response

    def create_input_request (self, env, listStringCredentials) -> InputRequest:
        inputRequest: InputRequest = self.reqParser.parse_env_and_listStringCredentials(env, listStringCredentials)
        inputRequest.setHeaders({"X-API-KEY": self.API_KEY_DESA})
        return inputRequest