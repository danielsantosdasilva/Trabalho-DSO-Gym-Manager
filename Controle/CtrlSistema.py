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
    def controlador_professor(self):
        return self.__controlador_professor

    @property
    def controlador_modalidade(self):
        return self.__controlador_modalidade

    def sistema_aluno(self):
        self.__controlador_aluno.iniciar_sist_aluno()

    def sair(self):
        exit()

    def inicializar(self):
        self.__controlador_aluno.aluno_logado = None
        switcher = {1: self.sistema_aluno, 2: self.login_professor, 0: self.sair}
        while True:
            opcao = self.__tela_sistema.tela_opcoes_inicio()
            metodo = switcher[opcao]
            metodo()

    def iniciar_sist_professor(self):
        switcher = {1: self.__controlador_professor.alterar_dados_prof, 2: self.__controlador_aluno.menu_cadastro_aluno,
                    3: self.__controlador_modalidade.iniciar_sist_modalidade, 0: self.inicializar}
        while True:
            opcao = self.__tela_sistema.tela_inicial_professor()
            metodo = switcher[opcao]
            metodo()

    def login_professor(self):
        dados = self.__tela_sistema.login()
        if dados is not None:
            matricula = dados["matricula"]
            senha = dados["senha"]
            professor = self.__controlador_professor.professor.get(1111)
            if professor.matricula == matricula and professor.senha == senha:
                self.iniciar_sist_professor()
            else:
                self.__tela_sistema.mensagem("Login falhou", "Matrícula ou senha erradas!")

    def login_aluno(self):
        dados = self.__tela_sistema.login()
        if dados is not None:
            matricula = dados["matricula"]
            senha = dados["senha"]
            for aluno in self.__controlador_aluno.lista_alunos.get_all():
                if aluno.matricula == matricula and aluno.senha == senha:
                    self.__controlador_aluno.aluno_logado = aluno
                    return True
            else:
                self.__tela_sistema.mensagem("Login falhou", "Matrícula ou senha erradas!")
