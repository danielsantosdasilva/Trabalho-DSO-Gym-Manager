from Tela.TelaSistema import TelaSistema
from Controle.CtrlAluno import CtrlAluno
from Controle.CtrlProfessor import CtrlProfessor
from Controle.CtrlModalidade import CtrlModalidade

class CtrlSistema:
    def __init__(self):
        self.__controlador_aluno = CtrlAluno(self)
        self.__controlador_professor = CtrlProfessor(self)
        self.__controlador_modalidade = CtrlModalidade(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlar_professor(self):
        return self.__controlador_professor

    @property
    def controlador_modalide(self):
        return self.__controlador_modalidade

    def sistema_aluno(self):
        self.__controlador_aluno.iniciar_sist_aluno()

    def sistema_professor(self):
        self.__controlador_professor.iniciar_sist_professor()

    def sair(self):
        exit()

    def inicializar(self):
        switcher = {1: self.sistema_aluno, 2: self.sistema_professor, 0: self.sair}
        while True:
            opcao = self.__tela_sistema.mostrar_opcoes_sistema()
            metodo = switcher[opcao]
            metodo()