from Entidade.professor import Professor
from Entidade.modalidade import Modalidade
from Entidade.horario import Horario
from Entidade.dia_semana import DiaSemana
from random import randint

class BancoDados:
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
