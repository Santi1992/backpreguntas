class CorrectAnswers ():

    # id pregunta es la clave , el value es la respuesta del dict de abajo
    res = {
        "1": "4",
        "2": "3",
        "3": "3",
        "4": "4",
        "5": "2",
        "6": "2",
        "7": "1",
        "8": "4",
        "9": "2",
        "10": "3",
        "11": "1",
        "12": "2",
        "13": "2",
        "14": "2",
        "15": "3",
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
