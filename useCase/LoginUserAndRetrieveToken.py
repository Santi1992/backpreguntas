from domain.entities.DataToken import DataToken
from domain.entities.GenericRequest import GenericRequest
import datetime
from services.AuthenticationService import AuthenticationService
from services.TokenService import TokenService
from services.UserSeervice import UserSeervice

class LoginUserAndRetrieveToken ():

    def __init__(self, userSeervice: UserSeervice=UserSeervice(),
         authenticationService: AuthenticationService= AuthenticationService(), 
         tokenService : TokenService = TokenService()) -> None:
        self.userSeervice = userSeervice
        self.tokenService = tokenService
        self.authenticationService = authenticationService

    def execute(self, genericRequest: GenericRequest):
        user = self.userSeervice.obtain_user(genericRequest.body["id"]) # usr y password hasheado
        self.authenticationService.check_password(user, genericRequest.body["password"])
        self.authenticationService.is_already_logged(user)
        dataToken: DataToken = self._create_data_token(genericRequest, user)
        return self.tokenService.create_token(dataToken)
    

    def _create_data_token(self, genericRequest, user):
        return DataToken().set_payload(
            {"id": genericRequest.body["id"]}
        ).set_exp(
            datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=180)
        ).set_secret("236723FjdHjhsdf-hj@_sfd")
