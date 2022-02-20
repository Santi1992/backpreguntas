import requests
from config.exceptions import RequestException
import uuid
import json
class RequestWrapper():

    def get(self, fullPath, inputRequest):
        req = None
        try:
            req = requests.get(fullPath, 
                        params=inputRequest.params, 
                        headers=inputRequest.headers,
                        verify=inputRequest.verify,
                        cert=inputRequest.cert,
                        timeout=inputRequest.timeout
                        )
            if req.status_code == 500 or req.status_code == 400:
                self.execute_error_handler(req, "REQUEST LLEGO A DESTINO", fullPath)
            return req.json(), req.status_code
        except Exception as e:
            self.execute_error_handler(req, e, fullPath)

    def post(self, fullPath, inputRequest):
        req=None
        try:
            req = requests.post(fullPath, 
                        params=inputRequest.params,
                        data=inputRequest.data,
                        headers=inputRequest.headers,
                        verify=inputRequest.verify,
                        cert=inputRequest.cert,
                        timeout=inputRequest.timeout,
                        files=inputRequest.files,
                        json=inputRequest.json
                        )
            if req.status_code == 500 or req.status_code == 400:
                self.execute_error_handler(req, "REQUEST LLEGO A DESTINO", fullPath)
                
            return req.json(), req.status_code
        except Exception as e:
            self.execute_error_handler(req, e, fullPath)

    def execute_error_handler(self, req, e, fullPath):
        error_other_api = None
        try:
            error_other_api = req.json().get("uidError", json.dumps(req.json()))
        except Exception as error:
            error_other_api = None
        if error_other_api !=None:
            # LA API DE DESTINO ROMPE PERO SABE MANEJAR EL ERROR
            raise RequestException(str(e), "Error en la request get del path : "+ fullPath + " " + "y su error es "+ error_other_api)
        # ERROR NO MANEJADO POR LA API DE DESTINO.
        raise RequestException(str(e), "Error en la request get del path : "+ fullPath)


