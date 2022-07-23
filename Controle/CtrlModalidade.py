from Tela.TelaModalidade import TelaModalidade
from Entidade.aluno import Aluno
from Entidade.modalidade import Modalidade
from Entidade.frequencia import Frequencia
from Entidade.horarioaluno import HorarioAluno
from DAO.ModalidadeDAO import ModalidadeDAO
from random import randint


class CtrlModalidade:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_modalidade = TelaModalidade()
        self.__dao_modalidades = ModalidadeDAO()

    @property
    def lista_modalidades(self):
        return list(self.__dao_modalidades.get_all())

    def iniciar_sist_modalidade(self):
        switcher = {1: self.matricular_aluno_modalidade, 2: self.desmatricular_aluno_modalidade,
                    3: self.listar_modalidades, 0: self.__controlador_sistema.iniciar_sist_professor}
        while True:
            opcao = self.__tela_modalidade.menu_inicial_tela()
            metodo = switcher[opcao]
            metodo()

    def selecionar_modalidade(self, codigo):
        for modalidade in self.__dao_modalidades.get_all():
            if modalidade.codigo == codigo:
                return modalidade
        else:
            self.__tela_modalidade.mensagem("Error", "A modalidade escolhida não existe!")

    def selecionar_horario(self, modalidade, codigo):
        for horario in modalidade.horarios:
            if horario.codigo == codigo:
                return horario
        else:
            self.__tela_modalidade.mensagem("Error", "O horário escolhido não existe!")

    def matricular_aluno_modalidade(self):
        self.__controlador_sistema.controlador_aluno.listar_alunos()
        if self.__controlador_sistema.controlador_aluno.lista_alunos.get_all():
            matricula = self.__tela_modalidade.escolher_aluno()
            if isinstance(matricula, int) and matricula is not None:
                aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno_matricula(matricula)
                if isinstance(aluno, Aluno) and (aluno is not None):
                    self.listar_modalidades()
                    codigo_modalidade = self.__tela_modalidade.escolher_codigo('Escolher Modalidade')
                    modalidade = self.selecionar_modalidade(codigo_modalidade)
                    if isinstance(modalidade, Modalidade) and (modalidade is not None):
                        self.listar_horarios(modalidade)
                        codigo_horario = self.__tela_modalidade.escolher_codigo("Código do Horário")
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
                                self.__controlador_sistema.controlador_aluno.lista_alunos.add(aluno)
                                self.__tela_modalidade.mensagem("Sucesso", "Aluno cadastrado na modalidade com sucesso!")

    def desmatricular_aluno_modalidade(self):
        self.__controlador_sistema.controlador_aluno.listar_alunos()
        if self.__controlador_sistema.controlador_aluno.lista_alunos.get_all():
            matricula = self.__tela_modalidade.escolher_aluno()
            aluno = self.__controlador_sistema.controlador_aluno.selecionar_aluno_matricula(matricula)
            if aluno.modalidades:
                self.listar_modalidades_aluno(aluno)
                codigo_modalidade = self.__tela_modalidade.escolher_codigo("Escolher Modalidade")
                modalidade = self.selecionar_modalidade_aluno(aluno, codigo_modalidade)
                if isinstance(modalidade, Modalidade) and (modalidade is not None)\
                        and isinstance(aluno, Aluno) and (aluno is not None):
                    aluno.modalidades.remove(modalidade) if modalidade in aluno.modalidades else None
                    modalidade.alunos.remove(aluno) if aluno in modalidade.alunos else None
                    for aula in aluno.aulas:
                        if aula.modalidade.horarios == modalidade.horarios:
                            aluno.aulas.remove(aula)
                    self.__controlador_sistema.controlador_aluno.lista_alunos.add(aluno)
                    self.__tela_modalidade.mensagem("Sucesso", "Aluno desmatriculado da modalidade com sucesso!")
            else:
                self.__tela_modalidade.mensagem_error("O aluno não está cadastrado em nenhuma modalidade.")

    def listar_modalidades(self):
        lista_modalidades = self.__dao_modalidades.get_all()
        if lista_modalidades:
            dados = self.gerar_lista_modalidades()
            self.__tela_modalidade.listar_modalidades(dados)

    def gerar_lista_modalidades(self):
        modalidades = []
        if self.__dao_modalidades.get_all():
            for modalidade in self.__dao_modalidades.get_all():
                dados = []
                dados.append(modalidade.nome)
                dados.append(modalidade.codigo)
                modalidades.append(dados)
            return modalidades

    def listar_horarios(self, modalidade):
        if self.__dao_modalidades.get_all():
            dados = self.gerar_lista_horarios(modalidade)
            self.__tela_modalidade.listar_horarios(modalidade, dados)

    def gerar_lista_horarios(self, modalidade):
        horarios = []
        if self.__dao_modalidades.get_all():
            for horario in modalidade.horarios:
                dados = []
                lista_dias = self.listar_horarios_dias(horario.dia_semana)
                dias_semana = ', '.join(lista_dias)
                dados.append(horario.periodo)
                dados.append(dias_semana)
                dados.append(horario.codigo)
                horarios.append(dados)
            return horarios

    def listar_horarios_dias(self, horario):
        lista_dias = []
        for dia in horario:
            lista_dias.append(dia.value)
        return lista_dias

    def selecionar_modalidade_aluno(self, aluno, codigo):
        for modalidade in aluno.modalidades:
            if modalidade.codigo == codigo:
                return modalidade
        else:
            self.__tela_modalidade.mensagem_error("A modalidade escolhida não existe!")

    def listar_modalidades_aluno(self, aluno):
        dados = self.gerar_lista_modalidade_aluno(aluno)
        self.__tela_modalidade.listar_modalidades(dados)

    def gerar_lista_modalidade_aluno(self, aluno):
        modalidades = []
        if aluno.modalidades:
            for modalidade in aluno.modalidades:
                dados = []
                dados.append(modalidade.nome)
                dados.append(modalidade.codigo)
                modalidades.append(dados)
            return modalidades
