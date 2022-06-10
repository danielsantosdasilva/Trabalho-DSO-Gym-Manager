

class Horario:
    def __init__(self, horario: str, dia_semana: []):
        self.__horario = horario
        self.__dia_semana = dia_semana

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

