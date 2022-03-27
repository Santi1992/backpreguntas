class CorrectAnswers ():

    # id pregunta es la clave , el value es la respuesta del dict de abajo
    res = {
        "1": "4",
        "2": "3",
        "3": "3",
        "4": "1",
        "5": "2",
        "6": "4",
        "7": "1",
        "8": "1",
        "9": "1",
        "10": "1",
        "11": "1",
        "12": "1",
        "13": "1",
        "14": "1",
        "15": "1",
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
