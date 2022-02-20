class GenericRequest():

    dataToken= None

    def set_apikey(self, apiKey):
        self.apiKey: str = apiKey
        return self
    
    def set_body(self, json):
        self.body = json
        return self
    
    def set_args(self, args):
        self.args = args
        return self
    
    def set_headers(self, headers):
        self.headers = headers
        return self
    
    def set_token(self, token):
        self.token = token
        return self
    



    # r.headers["authorization"] = "Bearer " + self.token