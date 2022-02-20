import datetime
from domain.entities.DataToken import DataToken
import jwt

class TokenService():

    def __init__(self) -> None:
        pass

    def create_token(self, dataToken: DataToken):
        
        payload = dataToken.payLoad
        payload["exp"] = dataToken.exp

        return jwt.encode(
        payload,
        dataToken.secret,
        algorithm="HS256",
    )

    def check_token_and_retrieve_data(self, token):
        splitTokenBearer = token.split(" ")[1]
        return jwt.decode(splitTokenBearer, "236723FjdHjhsdf-hj@_sfd", algorithms=["HS256"])