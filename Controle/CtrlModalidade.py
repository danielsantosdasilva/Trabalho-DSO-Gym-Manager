from Tela.TelaModalidade import TelaModalidade
from Entidade.aluno import Aluno
from Entidade.modalidade import Modalidade

class CtrlModalidade:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_modalidade = TelaModalidade()
        self.__lista_modalidades = []

    @property
    def lista_modalidades(self):
        return self.__lista_modalidades

    def iniciar_sist_modalidade(self):
        switcher = {1: self.matricular_aluno_modalidade, 2: self.desmatricular_aluno_modalidade,
                    3: self.listar_modalidades, 0: self.__controlador_sistema.iniciar_sist_professor}
        while True:
            opcao = self.__tela_modalidade.menu_inicial_modalidade()
            metodo = switcher[opcao]
            metodo()

    def selecionar_modalidade(self, codigo):
        for modalidade in self.__lista_modalidades:
            if modalidade.codigo == codigo:
                return modalidade
        else:
            self.__tela_modalidade.mensagem("A modalidade escolhida não existe!")

    def matricular_aluno_modalidade(self):
        print("CHEGOU EM MATRICULAR ALUNO MODALIDADE")
        self.__controlador_sistema.controlador_aluno.listar_alunos()
        if self.__controlador_sistema.controlador_aluno.lista_alunos:
            matricula = self.__tela_modalidade.escolher_aluno("Insira a matricula do aluno a cadastrar: ")
            aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno_matricula(matricula)
            if isinstance(aluno, Aluno) and (aluno is not None):
                self.__tela_modalidade.mensagem(f"Aluno selecionado: {aluno.nome}")
                self.listar_modalidades()
                codigo_modalidade = self.__tela_modalidade.escolher_modalidade("Código da modalidade a inscrever aluno: ")
                modalidade = self.selecionar_modalidade(codigo_modalidade)
                if isinstance(modalidade, Modalidade) and (modalidade is not None):
                    self.listar_horarios(modalidade)

    def desmatricular_aluno_modalidade(self):
        print("CHEGOU EM DESMATRICULAR ALUNO MODALIDADE")

    def listar_modalidades(self):
        print("CHEGOU EM LISTAR MODALIDADES")
        lista_modalidades = self.__lista_modalidades
        if lista_modalidades:
            for modalidade in lista_modalidades:
                self.__tela_modalidade.listar_modalidades(modalidade)

    def listar_horarios(self, modalidade):
        self.__tela_modalidade.mensagem(f"-----HORARIOS {modalidade.nome.upper()}-----")
        for horario in modalidade.horarios:
            dias_semana = self.listar_horarios_dias(horario.dia_semana)
            self.__tela_modalidade.listar_horarios(horario, dias_semana)

    def listar_horarios_dias(self, horario):
        lista_dias = []
        for dia in horario:
            lista_dias.append(dia.value)
        return lista_dias
