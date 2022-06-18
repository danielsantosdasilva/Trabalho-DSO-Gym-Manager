from Entidade.professor import Professor
from Entidade.modalidade import Modalidade
from Entidade.horario import Horario
from Entidade.dia_semana import DiaSemana
from random import randint

class BancoDados:
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema

    def rodar(self):
        # PROFESSOR:
        professor = Professor("Roberto", "admin123", 35, 12543542354, 80, 1.90, 1111)
        self.__ctrl_sistema.controlador_professor.professor = professor
        ########################################

        # HORARIOS:
        matutino_jiujitsu = Horario("Matutino(08:00-10:00)", [DiaSemana.SEGUNDA, DiaSemana.QUARTA, DiaSemana.SEXTA], randint(1000,9999))
        noturno_jiujitsu = Horario("Noturno(20:00-22:00)", [DiaSemana.TERCA, DiaSemana.QUINTA], randint(1000,9999))
        ########################################

        # MODALIDADES:
        jiujitsu = Modalidade("Jiu-Jitsu", [matutino_jiujitsu,noturno_jiujitsu], randint(1000,9999))
        self.__ctrl_sistema.controlador_modalidade.lista_modalidades.append(jiujitsu)
        ########################################
