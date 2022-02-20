from flask import jsonify, request, g
import logging
from config.exceptions import *
import traceback
import uuid
from domain.entities.InputSaveLog import InputSaveLog
from services.MsLogService import MsLogService

# g.useUid = request.args.get("userUID", None)
# g.userName = request.args.get("userName", None)
# g.uidRequest = request.environ['HTTP_X_REQUEST_ID']
# g.httpNow = request.environ['HTTP_DATE']


# NUNCA DEBEMOS ENVIARLE EL ERROR AL CLIENTE POR EL CUAL EXPLOTO LA CONSULTA.
# PARA CREAR UNA EXCEPCIÓN, DEBE SER CONVERSADA CON EL EQUIPO.

def register_error_handlers(app):

    SERVICE_UID = "1ef9e556-94e2-4ea2-8147-b80081140775"
    logger = logging.getLogger(__name__)
    
    ERR_MSG = {
        'AUTH_ERR': 'Error de autenticación',
        'AUTHZ_ERR': 'Usuario no autorizado',
        'ERROR': 'Error desconocido',
        'SQL_ERROR': 'Error interno en consulta sql',
        'REQ_ERROR': 'Error interno en request a otra api',
        'VALIDATION_ERROR': 'Error en validación',
    }

    def create_input_log_and_send(e, uid):

        serviceLogger: MsLogService = MsLogService(g.entorno)

        NAME_CLASS = type(e).__name__
        log_error = uid

        inputSaveLog: InputSaveLog = InputSaveLog().set_log_uid(
            g.uidRequest
        ).set_payload(
            {"errorName": NAME_CLASS,
            "errorDescription": e.originalError,
            "customMessage": e.message}
        ).set_service_uid(
            SERVICE_UID  #msTemplate
        ).set_client_uid(
            "1"  # RED LINK , HACER QUE ESCALE
        ).set_user_uid(
            "g.useUid" # CAMBIAR!!!!!!!!!!!!!!!! VIENE DE G
        ).set_error_uid(
            log_error
        )        

        serviceLogger.save_log(inputSaveLog)

    def create_response(msg, status, uid=None):
        response_obj = {
            'status': 'error',
            'message': msg,
            'uidError': uid,
        }

        return jsonify(response_obj), status
    
    @app.errorhandler(AuthenticationException)
    def handle_error1(e: AuthenticationException):
        log_error = uuid.uuid4()
        # create_input_log_and_send(e, log_error)
        return create_response(ERR_MSG['AUTH_ERR'], 401, log_error)
    
    @app.errorhandler(AuthorizationException)
    def handle_error2(e: AuthorizationException):
        #print(e.message, flush=True)
        log_error = uuid.uuid4()
        # create_input_log_and_send(e, log_error)
        return create_response(ERR_MSG['AUTH_ERR'], 401,  log_error)
    
    @app.errorhandler(MSSQLDBExeption)
    def handle_error3(e: MSSQLDBExeption):
        #print(e.message, flush=True)
        log_error = uuid.uuid4()
        # create_input_log_and_send(e, log_error)
        return create_response(ERR_MSG['SQL_ERROR'], 500,  log_error)

    @app.errorhandler(RequestException)
    def handle_error4(e: RequestException):
        log_error = uuid.uuid4()
        # create_input_log_and_send(e, log_error)
        return create_response(ERR_MSG['REQ_ERROR'], 500,  log_error)

    @app.errorhandler(ValidationException)
    def handle_error5(e: ValidationException):
        log_error = uuid.uuid4()
        # create_input_log_and_send(e, log_error)
        return create_response(ERR_MSG['VALIDATION_ERROR'], 400,  log_error)
