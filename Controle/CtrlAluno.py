from Tela.TelaAluno import TelaAluno
from Entidade.aluno import Aluno
from random import randint

class CtrlAluno:
    def __init__(self, controlador_sistema):
        self.__lista_alunos = []
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__aluno_logado = None

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @property
    def aluno_logado(self):
        return self.__aluno_logado

    @aluno_logado.setter
    def aluno_logado(self, aluno_logado):
        self.__aluno_logado = aluno_logado

    def consultar_cadastro(self):
        print("CHEGOU EM CONSULTAR CADASTRO")
        print(f"Usuário logado é {self.__aluno_logado.nome}")

    def consultar_aulas(self):
        print("CHEGOU EM CONSULTAR AULAS")

    def retornar(self):
        self.__controlador_sistema.iniciar_sist_professor()

    def iniciar_sist_aluno(self):
        self.listar_alunos()
        if self.__lista_alunos:
            if self.__controlador_sistema.login_aluno():
                switcher = {1: self.consultar_cadastro, 2: self.consultar_aulas, 0: self.__controlador_sistema.inicializar}
                while True:
                    opcao = self.__tela_aluno.mostrar_opcoes_aluno()
                    metodo = switcher[opcao]
                    metodo()

    def menu_cadastro_aluno(self):
        switcher = {1: self.cadastrar_aluno, 2: self.alterar_dados_aluno, 3: self.excluir_aluno, 4: self.listar_alunos, 0: self.retornar}
        while True:
            opcao = self.__tela_aluno.cadastro_aluno_prof()
            metodo = switcher[opcao]
            metodo()

    def cadastrar_aluno(self):
        print("CHEGOU EM CADASTRO ALUNO")
        dados = self.__tela_aluno.opcoes_cadastro("--------CADASTRO ALUNO--------", "aluno")
        for aluno in self.__lista_alunos:
            if aluno.cpf == dados["cpf"]:
                self.__tela_aluno.mensagem("O aluno já está cadastrado no sistema!")
                break
        else:
            aluno = Aluno(dados["nome"], dados["senha"], dados["idade"], dados["cpf"], dados["peso"], dados["altura"], randint(1000,9999))
            print(aluno.matricula)
            self.__lista_alunos.append(aluno)

    def alterar_dados_aluno(self):
        print("CHEGOU EM ALTERAR DADOS ALUNO")
        self.listar_alunos()
        if self.__lista_alunos:
            matricula = self.__tela_aluno.escolher_aluno("*Matrícula do aluno desejado: ")
            aluno = self.selecionar_aluno_matricula(matricula)
            if isinstance(aluno, Aluno) and (aluno is not None):
                dados = self.__tela_aluno.opcoes_cadastro("--------ALTERAR DADOS DO ALUNO--------", "aluno")
                aluno.nome = dados["nome"]
                aluno.idade = dados["idade"]
                aluno.peso = dados["peso"]
                aluno.cpf = dados["cpf"]
                aluno.altura = dados["altura"]
                aluno.senha = dados["senha"]

    def selecionar_aluno_matricula(self, matricula):
        for aluno in self.__lista_alunos:
            if aluno.matricula == matricula:
                return aluno
        else:
            self.__tela_aluno.mensagem("O aluno selecionado não existe!")

    def excluir_aluno(self):
        print("CHEGOU EM EXCLUIR ALUNO")
        self.listar_alunos()
        if self.__lista_alunos:
            matricula = self.__tela_aluno.escolher_aluno("*Matrícula do aluno a excluir: ")
            aluno = self.selecionar_aluno_matricula(matricula)
            if isinstance(aluno, Aluno) and (aluno is not None):
                self.__tela_aluno.mensagem(f"O aluno {aluno.nome} de matrícula {aluno.matricula} foi excluído do sistema.")
                self.__lista_alunos.remove(aluno)

    def listar_alunos(self):
        print("CHEGOU EM LISTAR ALUNOS")
        lista_alunos = self.__lista_alunos
        if not lista_alunos:
            self.__tela_aluno.mensagem("Não há nenhum aluno cadastrado no sistema.")
        for aluno in lista_alunos:
            self.__tela_aluno.listar_alunos(aluno)
