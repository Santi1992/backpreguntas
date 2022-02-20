from repository.locals.LocalEnvRepository import LocalEnvRepository
import os

localEnv = LocalEnvRepository()
class ClientsUrl():

    DEMO_GET_USUARIO =  f"{localEnv.get_ms_prueba()}/middle/hello"
