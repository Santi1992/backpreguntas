class AuthenticationException(Exception):
    def __init__(self, originalError, message="", aditionalErrorInformation=""):
        self.originalError = originalError
        self.message = message
        self.aditionalErrorInformation = aditionalErrorInformation
        super().__init__(originalError)

class AuthorizationException(Exception):
    def __init__(self, originalError, message="", aditionalErrorInformation=""):
        self.originalError = originalError
        self.message = message
        self.aditionalErrorInformation = aditionalErrorInformation
        super().__init__(originalError)

class ValidationException(Exception):
    def __init__(self, originalError, message="", aditionalErrorInformation=""):
        self.originalError = originalError
        self.message = message
        self.aditionalErrorInformation = aditionalErrorInformation
        super().__init__(originalError)

class SqlServerException(Exception):
    def __init__(self, originalError, message, aditionalErrorInformation=""):
        self.originalError = originalError
        self.message = message
        self.aditionalErrorInformation = aditionalErrorInformation
        super().__init__(originalError)

class MSSQLDBExeption(Exception):
    def __init__(self, originalError, message, aditionalErrorInformation=""):
        self.originalError = originalError
        self.message = message
        self.aditionalErrorInformation = aditionalErrorInformation
        super().__init__(originalError)

class RequestException(Exception):
    def __init__(self, originalError, message, aditionalErrorInformation=""):
        self.originalError = originalError
        self.message = message
        self.aditionalErrorInformation = aditionalErrorInformation
        super().__init__(originalError)