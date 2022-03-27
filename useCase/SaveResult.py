from domain.entities.GenericRequest import GenericRequest
from repository.connectors.SqlServerConector import SqlServerConector
from services.CorrectAnswers import CorrectAnswers

class SaveResult():

    def __init__(self, sql:SqlServerConector = SqlServerConector(),
                        correctAnswers: CorrectAnswers = CorrectAnswers()
    ) -> None:
        self.sql: SqlServerConector = sql
        self.correctAnswers = correctAnswers

    def execute(self, genericRequest: GenericRequest):

        idQuestion = genericRequest.body["idPregunta"]
        idUser = genericRequest.dataToken["id"]

        assignPoint = self.correctAnswers.check_answer(idQuestion, genericRequest.body["respuesta"])
        # Si repuesta correcta = 1 como string.

        try:
            cnx = self.sql.connect()
            cursor = cnx.cursor(dictionary=True)
            # STEP 1 VERIFICAR SI YA SE CONTESTO LA PREGUNTA.
            cursor.execute(f"SELECT * FROM camila.preguntas WHERE idmesa='{idUser}' and idpregunta='{idQuestion}'")
            res = cursor.fetchall()
            if len(res) == 0 :
                data_preguntas = {
                    'idmesa': idUser,
                    'idpregunta': idQuestion,
                    'resultado': assignPoint
                    }
                add_respuesta = ("INSERT INTO preguntas "
                    "(idmesa, idpregunta, resultado) "
                    "VALUES (%(idmesa)s, %(idpregunta)s, %(resultado)s)")
                cursor.execute(add_respuesta, data_preguntas)
                cnx.commit()
                cursor.close()
                cnx.close()
                return True
            else:
                cursor.close()
                cnx.close()
                return False
        except Exception as e:
            cursor.close()
            cnx.rollback()
            cnx.close()
            return "error"
