from Tela.TelaProfessor import TelaProfessor
from Entidade.professor import Professor

class CtrlProfessor:
    def __init__(self, controlador_sistema):
        self.__tela_professor = TelaProfessor()
        self.__controlador_sistema = controlador_sistema
        self.__professor = None

    @property
    def tela_professor(self):
        return self.__tela_professor

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def retornar(self):
        self.__controlador_sistema.inicializar()

    def alterar_dados_prof(self):
        print("CHEGOU EM ALTERAR DADOS PROF")
        if self.__professor:
            professor = self.__professor
            if isinstance(professor, Professor) and (professor is not None):
                dados = self.__tela_professor.opcoes_cadastro("--------ALTERAR DADOS DO PROFESSOR--------", "professor")
                professor.nome = dados["nome"]
                professor.idade = dados["idade"]
                professor.peso = dados["peso"]
                professor.cpf = dados["cpf"]
                professor.altura = dados["altura"]
                professor.senha = dados["senha"]

