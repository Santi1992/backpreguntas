from config.exceptions import ValidationException

# import hashlib  -------------->>>> PARA HASHEAR

# h = hashlib.new('sha256')
# h.update("1234".encode())
# h.update("hola".encode())
# contraseña = h.hexdigest()
# print(contraseña)

class UserSeervice():

    def __init__(self) -> None:
        pass
    
    def obtain_user(self, id):
        users = {
            "mesa1": "camiessexy",  # OBJETO CON COSAS DE UN USUARIO.
            "mesa2": "nicoessexy",
            "mesa3": "lanoviaessexy",
            "mesa4": "elnovioessexy",
            "mesa5": "niconacioparaelbasquet",
            "mesa6": "deestamesasalesexo",
            "mesa7": "ibaelesabueno",
            "mesa8": "camibailasexy",
            "mesa9": "camirompelapista",
            "mesa10": "nicorompelapista",
            "mesa11": "instrumentadorasexy",
            "mesa12": "elnoviolatienebig",
            "mesa13": "caminicoseamanmucho",
            "mesa14": "santiesuncapo",
            "mesa15": "elnoviolatienesuperbig",
            "mesa16": "nicoesbobelconstructor",
            "mesa17": "sevieneelpibe",
            "mesa18": "estanochesereproduce",
            "mesa19": "santiesuncapo",
        }
        res = users.get(id, None)
        if res == None :
            raise ValidationException("error")
        return res
   
