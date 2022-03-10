from flask_restx import Api
from routes.demo import api as ns1
from repository.locals.LocalEnvRepository import LocalEnvRepository

localEnv = LocalEnvRepository()
env: str = localEnv.get_environment()

api = Api(
    title='demo app',
    version='1.0',
    description='demo app',
    doc="/swagger/" if env != "production" else None
)

api.add_namespace(ns1, path='/api')