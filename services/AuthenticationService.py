from config.exceptions import ValidationException

class AuthenticationService():

    def __init__(self) -> None:
        pass

    def check_password(self, user, password):
        if user != password:
            raise ValidationException("Error de comprobación")

    def is_already_logged(self, user):
        pass

