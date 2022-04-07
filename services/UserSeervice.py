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
            "mesa1": "chicasdelosmartes",  # OBJETO CON COSAS DE UN USUARIO.
            "mesa2": "atailandianovuelvomas",
            "mesa3": "chofilinlinlan...",
            "mesa4": "nuevedoce",
            "mesa5": "carlosmepasaslosmorrones",
            "mesa6": "elculicerebro",
            "mesa7": "lospoli",
            "mesa8": "elespigon",
            "mesa9": "labolucompra",
            "mesa10": "duadameesaipa",
            "mesa11": "mecinayvino",
            "mesa12": "podesparar",
            "mesa14": "tengoladata",
            "mesa15": "quehaceschiquito",
            "mesa16": "cuandohayajuste",
            "mesa17": "clubnahuel",
            "mesa18": "alliskocher",
            "mesa19": "master",
        }
        res = users.get(id, None)
        if res == None :
            raise ValidationException("error")
        return res
   
