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

    def sair(self):
        exit()

    def inicializar(self):
        switcher = {1: self.sistema_aluno, 2: self.iniciar_sist_professor, 0: self.sair}
        while True:
            opcao = self.__tela_sistema.mostrar_opcoes_sistema()
            metodo = switcher[opcao]
            metodo()

    def iniciar_sist_professor(self):
        switcher = {1: self.__controlador_professor.alterar_dados_prof, 2: self.__controlador_aluno.menu_cadastro_aluno,
                    3: self.__controlador_modalidade.matricular_aluno_modalidade, 0: self.inicializar}
        while True:
            opcao = self.__tela_sistema.menu_inicial_professor()
            metodo = switcher[opcao]
            metodo()
