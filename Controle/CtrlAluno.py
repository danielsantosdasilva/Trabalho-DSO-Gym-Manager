from DAO.AlunoDAO import AlunoDAO
from Tela.TelaAluno import TelaAluno
from Entidade.aluno import Aluno
from random import randint
from Entidade.dia_semana import DiaSemana
from Exception.SemAlunoException import SemAlunoException
from Exception.AlunoNaoExisteException import AlunoNaoExisteException


class CtrlAluno:
    def __init__(self, controlador_sistema):
        self.__dao_alunos = AlunoDAO()
        self.__tela_aluno = TelaAluno()
        self.__controlador_sistema = controlador_sistema
        self.__aluno_logado = None

    @property
    def lista_alunos(self):
        return self.__dao_alunos

    @property
    def aluno_logado(self):
        return self.__aluno_logado

    @aluno_logado.setter
    def aluno_logado(self, aluno_logado):
        self.__aluno_logado = aluno_logado

    def consultar_cadastro(self):
        self.__tela_aluno.mostrar_cadastro(self.__aluno_logado)

    def gerar_lista_grade(self,aluno):
        dias = {DiaSemana.SEGUNDA: 0, DiaSemana.TERCA: 1,
                DiaSemana.QUARTA: 2, DiaSemana.QUINTA: 3, DiaSemana.SEXTA: 4}
        dias_keys = [DiaSemana.SEGUNDA, DiaSemana.TERCA,
                     DiaSemana.QUARTA, DiaSemana.QUINTA, DiaSemana.SEXTA]
        horarios = ["Matutino(08:00-10:00)","Vespertino(14:00-16:00)","Noturno(20:00-22:00)"]
        grade = [["Segunda", "N/A", "N/A", "N/A"], ["Terça", "N/A", "N/A", "N/A"],
                 ["Quarta", "N/A", "N/A", "N/A"], ["Quinta", "N/A", "N/A", "N/A"], ["Sexta", "N/A", "N/A", "N/A"]]
        for aula in aluno.aulas:
            for dia in dias_keys:
                if dia in aula.horario.dia_semana:
                    if aula.horario.periodo == horarios[0]:
                        grade[dias[dia]][1] = aula.modalidade.nome
                    elif aula.horario.periodo == horarios[1]:
                        grade[dias[dia]][2] = aula.modalidade.nome
                    elif aula.horario.periodo == horarios[2]:
                        grade[dias[dia]][3] = aula.modalidade.nome
        return grade

    def consultar_aulas(self):
        aluno = self.__aluno_logado
        dados = self.gerar_lista_grade(aluno)
        if aluno.aulas:
            self.__tela_aluno.consultar_aulas(dados)
        else:
            self.__tela_aluno.mensagem_error("O aluno não está cadastrado em nenhuma modalidade!")

    def retornar(self):
        self.__controlador_sistema.iniciar_sist_professor()

    def iniciar_sist_aluno(self):
        self.listar_alunos()
        if self.__dao_alunos.get_all():
            if self.__controlador_sistema.login_aluno():
                switcher = {1: self.consultar_cadastro, 2: self.consultar_aulas, 3: self.registrar_frequencia, 4: self.emitir_relatorio, 0: self.__controlador_sistema.inicializar}
                while True:
                    opcao = self.__tela_aluno.tela_inicial_aluno()
                    metodo = switcher[opcao]
                    metodo()

    def menu_cadastro_aluno(self):
        switcher = {1: self.cadastrar_aluno, 2: self.alterar_dados_aluno, 3: self.excluir_aluno, 4: self.listar_alunos, 0: self.retornar}
        while True:
            opcao = self.__tela_aluno.cadastro_aluno_prof()
            metodo = switcher[opcao]
            metodo()

    def cadastrar_aluno(self):
        dados = self.__tela_aluno.opcoes_cadastro("aluno")
        if dados is not None:
            for aluno in self.__dao_alunos.get_all():
                if aluno.cpf == dados["cpf"]:
                    self.__tela_aluno.mensagem("Falha", "O aluno já está cadastrado no sistema!")
                    break
            else:
                aluno = Aluno(dados["nome"], dados["senha"], dados["idade"], dados["cpf"], dados["peso"], dados["altura"], randint(1000, 9999))
                self.__dao_alunos.add(aluno)
                self.__tela_aluno.mensagem("Sucesso", "Aluno cadastrado com sucesso!")

    def alterar_dados_aluno(self):
        if self.__dao_alunos.get_all():
            self.listar_alunos()
            matricula = self.__tela_aluno.escolher_aluno()
            if isinstance(matricula, int) and matricula is not None:
                aluno = self.selecionar_aluno_matricula(matricula)
                if isinstance(aluno, Aluno) and (aluno is not None):
                    dados = self.__tela_aluno.opcoes_cadastro("aluno")
                    if dados is not None:
                        aluno.nome = dados["nome"]
                        aluno.idade = dados["idade"]
                        aluno.peso = dados["peso"]
                        aluno.cpf = dados["cpf"]
                        aluno.altura = dados["altura"]
                        aluno.senha = dados["senha"]
                        self.__dao_alunos.add(aluno)
                        self.__tela_aluno.mensagem("Sucesso", "Os dados do aluno foram alterados com sucesso!")

    def selecionar_aluno_matricula(self, matricula):
        try:
            for aluno in self.__dao_alunos.get_all():
                if aluno.matricula == matricula:
                    return aluno
            else:
                raise AlunoNaoExisteException
        except Exception:
            self.__tela_aluno.mensagem_error("O aluno selecionado não existe!")

    def excluir_aluno(self):
        self.listar_alunos()
        if self.__dao_alunos.get_all():
            matricula = self.__tela_aluno.escolher_aluno()
            if isinstance(matricula, int) and matricula is not None:
                aluno = self.selecionar_aluno_matricula(matricula)
                if isinstance(aluno, Aluno) and (aluno is not None):
                    self.__dao_alunos.remove(aluno.matricula)
                    self.__tela_aluno.mensagem("Sucesso", "O aluno selecionado foi excluído do sistema!")

    def listar_alunos(self):
        lista_alunos = self.__dao_alunos
        try:
            if not lista_alunos.get_all():
                raise SemAlunoException
            else:
                dados_alunos = self.gerar_lista_alunos()
                self.__tela_aluno.listar_alunos(dados_alunos)
        except Exception:
            self.__tela_aluno.mensagem_error("Não há nenhum aluno cadastrado no sistema!")

    def gerar_lista_alunos(self):
        alunos = []
        if self.__dao_alunos.get_all():
            for aluno in self.__dao_alunos.get_all():
                dados = []
                dados.append(aluno.nome)
                dados.append(aluno.matricula)
                dados.append(aluno.cpf)
                alunos.append(dados)
            return alunos

    def listar_aulas(self, aluno):
        dados = self.gerar_lista_aulas(aluno)
        if aluno.aulas:
            self.__tela_aluno.listar_aulas(dados)
        else:
            self.__tela_aluno.mensagem.mensagem_error('O Aluno não está cadastrado em nenhuma aula!')

    def gerar_lista_aulas(self, aluno):
        aulas = []
        if self.__dao_alunos.get_all():
            for aula in aluno.aulas:
                dados = []
                dados.append(aula.modalidade.nome)
                dados.append(aula.horario.periodo)
                dados.append(aula.codigo)
                aulas.append(dados)
            return aulas

    def registrar_frequencia(self):
        aluno = self.__aluno_logado
        self.listar_aulas(aluno)
        if aluno.aulas:
            codigo_aula = self.__tela_aluno.escolher_codigo("Escolha o código da aula")
            if isinstance(codigo_aula, int) and (codigo_aula is not None):
                for horarioaluno in aluno.aulas:
                    if horarioaluno.modalidade in aluno.modalidades and horarioaluno.codigo == codigo_aula:
                        for frequencia in aluno.frequencia:
                            if frequencia.aula == horarioaluno:
                                frequencia.aulas_feitas += 1
                                self.__dao_alunos.add(aluno)
                                self.__tela_aluno.mensagem("Sucesso", f"Frequência registrada na aula de {frequencia.modalidade.nome} com sucesso!")
                                return
                else:
                    self.__tela_aluno.mensagem_error("A aula escolhida não existe!")

    def emitir_relatorio(self):
        aluno = self.__aluno_logado
        if aluno.modalidades:
            dados = self.gerar_lista_relatorio(aluno)
            self.__tela_aluno.emitir_relatorio(dados)
        else:
            self.__tela_aluno.mensagem_error(f"{aluno.nome} não está cadastrado em nenhuma modalidade.")

    def gerar_lista_relatorio(self, aluno):
        if aluno.modalidades:
            relatorio = []
            for modalidade in aluno.modalidades:
                dados = []
                dados.append(modalidade.nome)
                total_aulas = 0
                aulas_feitas = 0
                for frequencia in aluno.frequencia:
                    if frequencia.modalidade == modalidade:
                        total_aulas += frequencia.aulas_totais
                        aulas_feitas += frequencia.aulas_feitas
                if aulas_feitas != 0:
                    quociente = aulas_feitas / total_aulas * 100
                else:
                    quociente = 0
                dados.append(str(quociente)+'%')
                dados.append(total_aulas)
                dados.append(aulas_feitas)
                relatorio.append(dados)
            return relatorio
