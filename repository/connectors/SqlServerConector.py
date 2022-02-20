from repository.locals.LocalEnvRepository import LocalEnvRepository
from config.exceptions import MSSQLDBExeption
import pymssql
import uuid
class SqlServerConector():

    def __init__(self, localEnvRepository:LocalEnvRepository=LocalEnvRepository()):
            self.DBUSER= localEnvRepository.get_db_user()
            self.DBPASS=localEnvRepository.get_db_pass()
            self.DBSERVER=localEnvRepository.get_db_server()
            self.DBBASE=localEnvRepository.get_db_base()

    def connect(self):
        try:
            conn = pymssql.connect(
                self.DBSERVER,
                self.DBUSER,
                self.DBPASS,
                self.DBBASE
            )
            return conn
        except pymssql.DatabaseError as e:
            raise MSSQLDBExeption(str(e), "Error intentando conectarme en la bbdd sql")
    
    def closeCursor(self, cur):
        cur.close()
    
    def disconnect(self, conn):
        conn.close()
    
    def commit(self, conn):
        conn.commit()
    
    def rollback(self, conn):
        conn.rollback()
    
    def cursor(self, conn):
        try:
            return conn.cursor(as_dict=True)
        except Exception as e:
            self.disconnect(conn)
            raise MSSQLDBExeption(str(e), "Error intentando obtener el curosr en la bbdd sql")

    def query_storeprocedure_many_resultset(self, name, args=()):
        conect = self.connect()
        cursor = self.cursor(conect)
        result=[]
        try:
            cursor.callproc(name, args)
            while True:
                if not cursor.nextset():
                    break
                result.append(cursor.fetchall())
            self.closeCursor(cursor)
            self.disconnect(conect)
            return result
        except Exception as e:
            if cursor:
                self.closeCursor(cursor)
                self.disconnect(conect)
            raise MSSQLDBExeption(str(e), "Error, intento ejecutar el store procedure : " + name)