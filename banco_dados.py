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
        matutino_jiujitsu = Horario("Matutino(08:00-10:00)", [DiaSemana.SEGUNDA, DiaSemana.SEXTA], randint(1000, 9999), 8)
        noturno_jiujitsu = Horario("Noturno(20:00-22:00)", [DiaSemana.QUARTA, DiaSemana.SEXTA], randint(1000, 9999), 8)
        vespertino_jiujitsu = Horario("Vespertino(14:00-16:00)", [DiaSemana.TERCA], randint(1000, 9999), 4)
        matutino_yoga = Horario("Matutino(08:00-10:00)", [DiaSemana.QUARTA, DiaSemana.QUINTA], randint(1000, 9999), 8)
        noturno_yoga = Horario("Noturno(20:00-22:00)", [DiaSemana.SEGUNDA], randint(1000, 9999), 4)
        vespertino_yoga = Horario("Vespertino(14:00-16:00)", [DiaSemana.SEGUNDA, DiaSemana.SEXTA], randint(1000, 9999), 8)
        matutino_boxe = Horario("Matutino(08:00-10:00)", [DiaSemana.TERCA], randint(1000, 9999), 4)
        noturno_boxe = Horario("Noturno(20:00-22:00)", [DiaSemana.TERCA, DiaSemana.QUINTA], randint(1000, 9999), 8)
        vespertino_boxe = Horario("Vespertino(14:00-16:00)", [DiaSemana.QUARTA, DiaSemana.QUINTA], randint(1000, 9999), 8)
        ########################################

        # MODALIDADES:
        jiujitsu = Modalidade("Jiu-Jitsu", [matutino_jiujitsu, noturno_jiujitsu, vespertino_jiujitsu], randint(1000, 9999))
        yoga = Modalidade("Yoga", [matutino_yoga, vespertino_yoga, noturno_yoga], randint(1000, 9999))
        boxe = Modalidade("Boxe", [matutino_boxe, vespertino_boxe, noturno_boxe], randint(1000, 9999))
        self.__ctrl_sistema.controlador_modalidade.lista_modalidades.append(jiujitsu)
        self.__ctrl_sistema.controlador_modalidade.lista_modalidades.append(yoga)
        self.__ctrl_sistema.controlador_modalidade.lista_modalidades.append(boxe)
        ########################################
