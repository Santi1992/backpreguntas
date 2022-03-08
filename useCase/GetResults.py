from domain.entities.GenericRequest import GenericRequest
from repository.connectors.SqlServerConector import SqlServerConector

class GetResults():

    def __init__(self, sql:SqlServerConector = SqlServerConector()) -> None:
        self.sql: SqlServerConector = sql

    def execute(self, genericRequest: GenericRequest):
        try:
            cnx = self.sql.connect()
            cursor = cnx.cursor()
            cursor.execute("""
            SELECT idmesa, CAST(SUM(CAST(resultado as UNSIGNED)) AS CHAR)
            FROM camila.preguntas
            GROUP BY idmesa
            """)
            res = cursor.fetchall()
            cursor.close()
            cnx.close()
            return self.build_answers(res)
        except Exception as e:
            print(e)
            cursor.close()
            cnx.close()
    
    def build_answers(self, resSql):
        finalList = []
        for i in resSql:
            dictt={}
            dictt["id"] = i[0]
            dictt["puntaje"] = int(i[1])
            finalList.append(dictt)
        return finalList

