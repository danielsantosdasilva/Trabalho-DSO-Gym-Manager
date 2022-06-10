from Tela.TelaAluno import TelaAluno


class CtrlAluno:
    def __init__(self, controlador_sistema):
        self.__lista_alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    def consultar_cadastro(self):
        print("CHEGOU EM CONSULTAR CADASTRO")

    def consultar_aulas(self):
        print("CHEGOU EM CONSULTAR AULAS")

    def retornar(self):
        self.__controlador_sistema.inicializar()

    def iniciar_sist_aluno(self):
        switcher = {1: self.consultar_cadastro, 2: self.consultar_aulas, 0: self.retornar}
        opcao = self.__tela_aluno.mostrar_opcoes_aluno()
        metodo = switcher[opcao]
        metodo()
