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
            "mesa2": "ailucapa",
            "mesa3": "ailucapa",
            "mesa4": "ailucapa",
            "mesa5": "ailucapa",
            "mesa6": "ailucapa",
            "mesa7": "ailucapa",
            "mesa8": "ailucapa",
            "mesa9": "ailucapa",
            "mesa10": "ailucapa",
            "mesa11": "ailucapa",
            "mesa12": "ailucapa",
            "mesa13": "ailucapa",
            "mesa14": "ailucapa",
            "mesa15": "ailucapa",
            "mesa16": "ailucapa",
            "mesa17": "ailucapa",
            "mesa18": "ailucapa",
        }
        res = users.get(id, None)
        if res == None :
            raise ValidationException("error")
        return res
   
