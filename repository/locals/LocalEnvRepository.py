import os

# REGISTRAR CADA MIROSERVICIO RUTA ORIGINAL IP Y PUERTO EN LAS ENV.
# EN CLIENTS URL DIRECTAMENTE LA RUTA ESPECÍFICA.

class LocalEnvRepository():

    def __init__(self):
        self.variables = {
            "API_KEY": os.getenv("API_KEY"),
            "PORT": os.getenv("API_KEY"),
            "PROTOCOL": os.getenv("PROTOCOL"),
            "DBUSER": os.getenv("DBUSER"),
            "DBPASS": os.getenv("DBPASS"),
            "DBSERVER": os.getenv("DBSERVER"),
            "DBBASE": os.getenv("DBBASE"),
            "ENVIRONMENT": os.getenv("ENVIRONMENT"),
            "MSPRUEBA": os.getenv("MSPRUEBA"),
            "MSLOGS": os.getenv("MSLOGS"),
            "MSLOGSKEY": os.getenv("API_KEY_MSLOGS")
        }

    def get_api_key(self):
        return self.variables["API_KEY"]
    
    def get_port(self):
        return self.variables["PORT"]

    def get_protocol(self):
        return self.variables["PROTOCOL"]
    
    def get_db_user(self):
        return self.variables["DBUSER"]

    def get_db_pass(self):
        return self.variables["DBPASS"]

    def get_db_server(self):
        return self.variables["DBSERVER"]

    def get_db_base(self):
        return self.variables["DBBASE"]
    
    def get_environment(self):
        return self.variables["ENVIRONMENT"]
    
    def get_ms_prueba(self):
        return self.variables["MSPRUEBA"]

    def get_ms_log(self):
        return self.variables["MSLOGS"]
    
    def get_key_ms_log(self):
        return self.variables["MSLOGSKEY"]