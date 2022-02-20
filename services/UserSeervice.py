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
            "mesa1": "soylamesapiola",  # OBJETO CON COSAS DE UN USUARIO.
            "mesa2": "soylamesaconmasonda",
            "mesa3": "soyunamesaaburida"
        }
        res = users.get(id, None)
        if res == None :
            raise ValidationException("error")
        return res
   
