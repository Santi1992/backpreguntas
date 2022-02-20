from repository.connectors.SqlServerConector import SqlServerConector
from config.exceptions import MSSQLDBExeption
from repository.locals.StoreProcedure import StoreProcedure
import uuid

class SqlServerUserRepository():

    def __init__(self) -> None:
        self.sqlServer:SqlServerConector = SqlServerConector()
        self.SP: StoreProcedure = StoreProcedure()

    def crear_usuario(self,name):
        cur, con = self.cursor()
        self.run_native_query(f"INSERT INTO TEMPLATE_PRUEBA ([NAME]) VALUES ('{name}')", cur, con)
        self.sqlServer.commit(con) #En caso de querer commitear, luego de varias consultas.
        self.sqlServer.closeCursor(cur)
        self.sqlServer.disconnect(con)


    def ver_usuarios(self, args=()):
        return self.sqlServer.query_storeprocedure_many_resultset(self.SP.DEMO, args)

    ###### NO TOCAR DE ACÁ PARA ABAJO ###################################    
    def run_native_query(self,strQuery, cur, con):
        try:
            return cur.execute(strQuery)
        except Exception as e:
            self.sqlServer.rollback(con)
            self.sqlServer.closeCursor(cur)
            self.sqlServer.disconnect(con)
            raise MSSQLDBExeption(str(e), "Error corriendo : " + strQuery)
    
    def connect(self):
        return self.sqlServer.connect()
    
    def cursor(self):
        conection = self.connect()
        return self.sqlServer.cursor(conection), conection

   
