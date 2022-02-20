from services.UserService import UserService
from domain.entities.GenericRequest import GenericRequest
from services.MsVaultService import MsVaultService

class ObtenerUsuario():

    def __init__(self, userService:UserService = UserService(), msVault:MsVaultService=MsVaultService()) -> None:
        self.userService = userService
        self.msVault: MsVaultService = msVault
    
    # TODOS LOS CASOS DE USO DEBEN TENER EL MÉTODO EXECUTE
    # TODOS LOS CASOS DEBE INGRESAR EL MISMO OBJETO.
    def execute(self, genericRequest:GenericRequest):

        self.msVault.guardar_clave_usuario()
        self.userService.ver_usuario(genericRequest)
        return self.msVault.guardar_clave_usuario()


    # FUNCIONES ADICIONALES PARA EL TRASPASO DE INFORMACIÓN ENTRE SERVICIOS.
    # FUNCIÓN PARA LÓGICA EN DEFINICIÓN DE QUE HACER.
    def build_more_functions(self, OBJEO_CASO_DE_USO):
        pass
