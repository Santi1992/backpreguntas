from domain.entities.GenericRequest import GenericRequest
from domain.validators.Validations import Validations
from repository.locals.LocalEnvRepository import LocalEnvRepository
from config.exceptions import ValidationException, AuthorizationException
from services.TokenService import TokenService


class RequestValidator(Validations):

    def __init__(self, environment_repository=LocalEnvRepository()):
        self.environment_repository: LocalEnvRepository = environment_repository
        super().__init__()
    
    def generic_validate(self, genericRequest: GenericRequest):
        self.check_token_and_save_data_in_generic_request(genericRequest)

    def login_endpoint_validate(self, genericRequest: GenericRequest):
            user = genericRequest.body.get("id", "")
            password = genericRequest.body.get("password", "")
            if user == "" or password == "":
                raise ValidationException("debe enviar alguno de los dos")
    
    def check_token_and_save_data_in_generic_request(self, genericRequest: GenericRequest):
        if genericRequest.token == "" or None:
            raise AuthorizationException("Dont send the token")
        tokenService: TokenService = TokenService()
        genericRequest.dataToken = tokenService.check_token_and_retrieve_data(genericRequest.token)