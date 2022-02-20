from flask_restx.reqparse import RequestParser

def demo_obtener_usuario():
    request_parser = RequestParser()

    request_parser.add_argument('accountId', type=str, help='ID de cuenta a eliminar', required=True, location='args')
    request_parser.add_argument('X-USER-TOKEN', type=str, help='Token conteniendo el UID y dominio del usuario que realizo la solicitud', required=True, location='headers')
    request_parser.add_argument('X-SITE-URL', type=str, help='URL del sitio (Ej: "https://recovery.redlink.com.ar")', required=True, location='headers')
    request_parser.add_argument('X-LANGUAGE-LOCALE', type=str, help='Lenguaje del sistema', required=False, location='headers')

    return request_parser
