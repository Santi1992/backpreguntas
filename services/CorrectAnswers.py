class CorrectAnswers ():

    # id pregunta es la clave , el value es la respuesta del dict de abajo
    res = {
        "1": "4",
        "2": "3",
        "3": "2",
        "4": "",
        "5": "",
        "7": "",
        "8": "",
        "9": "",
        "10": "",
        "11": "",
        "12": "",
        "13": "",
        "14": "",
        "15": "",
    }

    def __init__(self) -> None:
        pass

    # Si la respuesta es correcta devuelve un 1 caso contrario un 0
    def check_answer(self, idQuestion, selectedResult):
        respuestaCorrecta = self.res[idQuestion]
        if respuestaCorrecta == selectedResult:
            return "1"
        else:
            return "0"
