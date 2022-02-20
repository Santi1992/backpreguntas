from domain.entities.InputRequest import InputRequest
from domain.entities.InputSaveLog import InputSaveLog
from repository.clients.RequestWrapper import RequestWrapper
from domain.parsers.InputRequestParser import InputRequestParser

class MsLogService(RequestWrapper):

    URLS = {
        "local":"http://172.16.200.200:8118/v1/log/save",
        "homo" :"http://172.16.208.37:8106/v1/log/save"
    }
    API_KEY_DESA = "C4k*MROdTz_DJ-M"

    def __init__(self, entorno, inputRequestParser=InputRequestParser()) -> None:
        self.entorno = entorno
        self.reqParser: InputRequestParser = inputRequestParser
        super().__init__()
    
    def save_log(self, inputSaveLog: InputSaveLog):
        inputRequest :InputRequest = self.create_input_request(inputSaveLog)
        response, status = self.post(self.URLS[self.entorno],inputRequest)
        return response

    def create_input_request (self, inputSaveLog: InputSaveLog) -> InputRequest:
        input_request_withOutHeader: InputRequest = self.reqParser.parse_save_log(inputSaveLog)
        input_request_withOutHeader.setHeaders({"X-API-KEY": self.API_KEY_DESA})
        return input_request_withOutHeader