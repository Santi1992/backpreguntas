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
            "cocacola": "pasaseloa...",
            "price": "jovenesprofesionalesdrogadictos",
            "benei": "afnapasion",
            "mercadolibre": "yolavi",
            "bice": "pasameelip",
            "bna": "nuncasedaracuenta",
            "itau": "elloboyeldetective",
            "patagonia": "elbudamehacetocarmejor",
            "pañalera": "santiailuhoylaponenfuerte",
            "sabra": "lospoli",
            "techint": "mamateamo",
            "bancochanti": "tatisupercapo",
            "janos": "tigreyalsinasiempredefiesta",
            "clover": "analytica",
            "showpo": "santiailusexys",
            "schneider":"hoyesnochedesexo"
        }
        res = users.get(id, None)
        if res == None :
            raise ValidationException("error")
        return res
   
