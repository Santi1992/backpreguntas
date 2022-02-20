class DataToken():

    def __init__(self) -> None:
        pass

    def set_payload(self, payLoad):
        self.payLoad = payLoad
        return self

    def set_exp(self, exp):
        self.exp = exp
        return self

    def set_secret(self, secret):
        self.secret = secret
        return self