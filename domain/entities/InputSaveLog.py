class InputSaveLog():

    def __init__(self) -> None:
        self.error_uid=None
        self.endpoint=None
        pass

    def set_user_uid(self, user_uid): # usuario q genero el problema deberia ser opcional.
        self.user_uid=user_uid
        return self

    def set_client_uid(self, client_uid): # ejemplo redlink
        self.client_uid=client_uid
        return self
    
    def set_service_uid(self, service_uid): # ejemplo el ms que le pega, siempre el mismo
        self.service_uid=service_uid
        return self

    def set_log_uid(self, log_uid): # uid único del log.
        self.log_uid=log_uid
        return self

    def set_error_uid(self, error_uid): # uid único del log.
        self.error_uid=error_uid
        return self
    
    def set_endpoint(self, endpoint): # uid único del log.
        self.endpoint=endpoint
        return self
    
    def set_payload(self, payload): # uid único del log.
        self.payload=payload
        return self
    