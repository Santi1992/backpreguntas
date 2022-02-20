from domain.entities.InputRequest import InputRequest
from domain.entities.InputSaveLog import InputSaveLog

class InputRequestParser():
    def __init__(self):
        pass
    def parse(self, method=None, params=None, headers=None, data=None, verify=False, timeout=None, cert=None, files=None, json=None, asyncc=False):
        return InputRequest().setMethod(
            method).setParams(
            params).setHeaders(
            headers).setData(
            data).setVerify(
            verify).setTimeOut(
            timeout).setCert(
            cert).setFile(
            files).setJson(
            json).setAsyncc(
                asyncc
            )
    
    def parse_save_log(self, inputSaveLog: InputSaveLog):
        params = {
            "userUid": inputSaveLog.user_uid,
            "clientUid": inputSaveLog.client_uid,
            "serviceUid": inputSaveLog.service_uid,
            "logUid": inputSaveLog.log_uid,
            "errorUid": inputSaveLog.error_uid,
            "endpoint": inputSaveLog.endpoint
        }

        return InputRequest().setJson(
            inputSaveLog.payload).setParams(
                params
            )
    def parse_env_and_listStringCredentials(self,env, listStringCrendtials):
        params = {
            "environment":env,
            "credentialList": listStringCrendtials
        }
        return InputRequest().setParams(
            params
        )

            
        