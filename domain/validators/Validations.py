import re

class Validations:

    URL = "^[*\\w\\-]+(\\.[\\w\\-]+)+[/#?]?"  # ejemplo algo.com
    MAIL = '[a-z0-9]+@[a-z]+\.[a-z]{2,3}'
    
    def __init__(self) -> None:
        pass

    def validate_regex_expresion(self, regex, strAValidar):
        regex = re.compile(regex)
        res = regex.search(strAValidar) 
        return bool(res)
    
    def validate_is_url(self, strAValidar):
        regex = re.compile(self.URL)
        res = regex.search(strAValidar) 
        return bool(res)
    
    def validate_is_email(self, strAValidar):
        regex = re.compile(self.MAIL)
        res = regex.search(strAValidar) 
        return bool(res)

    def validate_min(self, arg, min):
        if len(arg) >= min:
            return True
        else:
            raise Exception
    
    def validate_max(self, arg, max):
        if len(arg) <= max:
            return True
        else:
            raise Exception
    
    def prevent_dict_sql(self, dict:dict):
        for i in dict.values():
            res = self.prevent_str_sql(i)
            if res == False:
                return False
        return True

    def prevent_str_sql(self, strAValidar:str):
        upper = strAValidar.upper()
        reserveWords = ["SELECT", "CURSOR", "EXEC", "EXECUTE", "CURSOR", "ALTER", "SP_",
        "GRANT", "XP_", "DENY", "DROP", "ROLLBACK", "INSERT", "DELETE", "UPDATE", "GO", "CREATE",
        "SHUTDOWN", "BEGIN", "WHERE"]
        for i in reserveWords:
            res = upper.find(i)
            if res != -1:
                return False
        return True
        

    def validate_min_max(self, arg, min, max):
        if len(arg) >= min and len(arg) <= max:
            return True
        else:
            raise Exception