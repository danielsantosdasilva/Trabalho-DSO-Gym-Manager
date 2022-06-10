from Tela.TelaProfessor import TelaProfessor
from Entidade.aluno import Aluno
from random import randint


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

    def cadastrar_aluno(self):
        print("CHEGOU EM CADASTRO ALUNO")
        dados = self.__tela_professor.opcoes_cadastro_aluno("--------CADASTRO ALUNO--------")
        for aluno in self.__controlador_sistema.controlador_aluno.lista_alunos:
            if aluno.cpf == dados["cpf"]:
                print("O aluno já está cadastrado no sistema!")
                break
        else:
            aluno = Aluno(dados["nome"], dados["idade"], dados["cpf"], dados["peso"], dados["altura"], randint(1000,9999))
            print(aluno.matricula)
            self.__controlador_sistema.controlador_aluno.lista_alunos.append(aluno)

    def alterar_dados_aluno(self):
        print("CHEGOU EM ALTERAR DADOS ALUNO")
        self.listar_alunos()
        if self.__controlador_sistema.controlador_aluno.lista_alunos:
            matricula = self.__tela_professor.escolher_aluno("*Matrícula do aluno desejado: ")
            aluno = self.selecionar_aluno_matricula(matricula)
            if aluno is not None:
                dados = self.__tela_professor.opcoes_cadastro_aluno("--------ALTERAR DADOS DO ALUNO--------")
                aluno.nome = dados["nome"]
                aluno.idade = dados["idade"]
                aluno.peso = dados["peso"]
                aluno.cpf = dados["cpf"]
                aluno.altura = dados["altura"]

    def selecionar_aluno_matricula(self, matricula):
        for aluno in self.__controlador_sistema.controlador_aluno.lista_alunos:
            if aluno.matricula == matricula:
                return aluno
        else:
            print("O aluno selecionado não existe!")

    def excluir_aluno(self):
        print("CHEGOU EM EXCLUIR ALUNO")
        self.listar_alunos()
        if self.__controlador_sistema.controlador_aluno.lista_alunos:
            matricula = self.__tela_professor.escolher_aluno("*Matrícula do aluno a excluir: ")
            aluno = self.selecionar_aluno_matricula(matricula)
            self.__tela_professor.mensagem(f"O aluno {aluno.nome} de matrícula {aluno.matricula} foi excluído do sistema.")
            self.__controlador_sistema.controlador_aluno.lista_alunos.remove(aluno)

    def listar_alunos(self):
        print("CHEGOU EM LISTAR ALUNOS")
        lista_alunos = self.__controlador_sistema.controlador_aluno.lista_alunos
        if not lista_alunos:
            self.__tela_professor.mensagem("Não há nenhum aluno cadastrado no sistema.")
        for aluno in lista_alunos:
            self.__tela_professor.listar_alunos(aluno)

    def matricular_aluno_modalidade(self):
        print("CHEGOU EM MATRICULAR ALUNO MODALIDADE")

    def desmatricular_aluno_modalidade(self):
        print("CHEGOU EM DESMATRICULAR ALUNO MODALIDADE")

    def retornar(self):
        self.__controlador_sistema.inicializar()

    def iniciar_sist_professor(self):
        switcher = {1: self.cadastrar_aluno, 2: self.alterar_dados_aluno, 3: self.excluir_aluno,
                    4: self.listar_alunos, 5: self.matricular_aluno_modalidade, 6: self.desmatricular_aluno_modalidade, 0: self.retornar}
        while True:
            opcao = self.__tela_professor.mostrar_opcoes_professor()
            metodo = switcher[opcao]
            metodo()