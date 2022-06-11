from Tela.TelaProfessor import TelaProfessor


class CtrlProfessor:
    def __init__(self, controlador_sistema):
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema

    @property
    def tela_professor(self):
        return self.__tela_professor

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def menu_alunos(self):
        pass

    def menu_modalidades(self):
        pass

    def retornar(self):
        self.__controlador_sistema.inicializar()

    def alterar_dados_prof(self):
        pass
