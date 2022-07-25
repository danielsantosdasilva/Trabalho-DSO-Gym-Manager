from Tela.TelaProfessor import TelaProfessor
from Entidade.professor import Professor
from DAO.ProfessorDAO import ProfessorDAO
from Tela.TelaAbstrata import TelaAbstrata


class CtrlProfessor:
    def __init__(self, controlador_sistema):
        self.__tela_professor = TelaProfessor()
        self.__dao_professor = ProfessorDAO()
        self.__controlador_sistema = controlador_sistema

    @property
    def tela_professor(self):
        return self.__tela_professor

    @property
    def professor(self):
        return self.__dao_professor

    @professor.setter
    def professor(self, professor):
        self.__dao_professor = professor

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def retornar(self):
        self.__controlador_sistema.inicializar()

    def alterar_dados_prof(self):
        if self.professor:
            professor = self.professor.get(1111)
            if isinstance(professor, Professor) and (professor is not None):
                dados = self.__tela_professor.opcoes_cadastro("professor")
                if dados is not None:
                    professor.nome = dados["nome"]
                    professor.idade = dados["idade"]
                    professor.peso = dados["peso"]
                    professor.cpf = dados["cpf"]
                    professor.altura = dados["altura"]
                    professor.senha = dados["senha"]
                    self.__dao_professor.add(professor)


