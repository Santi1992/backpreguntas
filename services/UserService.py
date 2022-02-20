from repository.remotes.SqlServerUserRepository import SqlServerUserRepository

class UserService():

    def __init__(self, userRepository: SqlServerUserRepository=SqlServerUserRepository()) -> None:
        self.userRepository = userRepository
    
    def crear_usuario(self, objeto):
        self.userRepository.crear_usuario("santi")
    
    def ver_usuario(self, objeto):
        return self.userRepository.ver_usuarios()
              
