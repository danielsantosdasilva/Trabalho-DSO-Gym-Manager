from Tela.TelaModalidade import TelaModalidade
from Entidade.aluno import Aluno
from Entidade.modalidade import Modalidade
from Entidade.horarioaluno import HorarioAluno
from Entidade.frequencia import Frequencia
from random import randint


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

    def selecionar_horario(self, modalidade, codigo):
        for horario in modalidade.horarios:
            if horario.codigo == codigo:
                return horario
        else:
            self.__tela_modalidade.mensagem("O horário escolhido não existe!")

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
                    codigo_horario = self.__tela_modalidade.escolher_horarios("Código do horário a inscrever aluno: ")
                    horario = self.selecionar_horario(modalidade, codigo_horario)
                    horario_aluno = HorarioAluno(horario, aluno, modalidade, randint(1000, 9999))
                    if isinstance(horario_aluno, HorarioAluno) and (horario_aluno is not None):
                        for aula in aluno.aulas:
                            for dia in aula.horario.dia_semana:
                                if aula.horario.periodo == horario.periodo and dia in horario.dia_semana:
                                    self.__tela_modalidade.mensagem("O horário selecionado para o aluno já está ocupado na sua agenda.")
                                    return None
                        else:
                            aluno.aulas.append(horario_aluno)
                            frequencia = Frequencia(modalidade, horario_aluno, horario.numero_aulas)
                            aluno.frequencia.append(frequencia)
                            modalidade.alunos.append(aluno) if aluno not in modalidade.alunos else None
                            aluno.modalidades.append(modalidade) if modalidade not in aluno.modalidades else None
                            self.__tela_modalidade.mensagem("Aluno cadastrado na modalidade com sucesso!")

    def desmatricular_aluno_modalidade(self):
        self.__controlador_sistema.controlador_aluno.listar_alunos()
        if self.__controlador_sistema.controlador_aluno.lista_alunos:
            matricula = self.__tela_modalidade.escolher_aluno("Insira a matricula do aluno a desmatricular: ")
            aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno_matricula(matricula)
            self.listar_modalidades()
            codigo_modalidade = self.__tela_modalidade.escolher_modalidade("Código da modalidade a desmatricular aluno: ")
            modalidade = self.selecionar_modalidade(codigo_modalidade)
            if isinstance(modalidade, Modalidade) and (modalidade is not None):
                if isinstance(aluno, Aluno) and (aluno is not None):
                    self.__tela_modalidade.mensagem(f"Aluno selecionado: {aluno.nome}")
                    modalidade.alunos.remove(aluno) if aluno in modalidade.alunos else None
                    for horarioaluno in aluno.aulas:
                        if horarioaluno.modalidade.nome == modalidade.nome:
                            aluno.aulas.remove(horarioaluno)
                            if modalidade in aluno.modalidades:
                                aluno.modalidades.remove(modalidade)
                    self.__tela_modalidade.mensagem("Aluno desmatriculado da modalidade com sucesso!")

    def listar_modalidades(self):
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
