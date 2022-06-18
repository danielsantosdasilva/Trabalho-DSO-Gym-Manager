from Tela.TelaAbstrata import TelaAbstrata


class TelaModalidade(TelaAbstrata):
    def __init__(self):
        pass

    def escolher_aluno(self, mensagem):
        print("-----ESCOLHER ALUNO-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def escolher_modalidade(self, mensagem):
        print("-----ESCOLHER MODALIDADE-----")
        opcao = super().ler_dados(int, mensagem)
        return opcao

    def escolher_horarios(self, modalidade):
        print("-----ESCOLHER HORARIOS-----")

    def listar_modalidades(self, modalidade):
        print("-----MODALIDADE-----")
        print(f"Modalidade: {modalidade.nome}")
        print(f"Codigo: {modalidade.codigo}")

    def listar_horarios(self, horario, dias_semana):
        print(f"Horario: {horario.periodo} - {', '.join(dias_semana)}")
        print(f"Código: {horario.codigo}")

    def menu_inicial_modalidade(self):
        print("--------MODALIDADES--------")
        print("1. Cadastrar aluno em uma modalidade")
        print("2. Remover aluno de uma modalidade")
        print("3. Listar Modalidades")
        print("0. Retornar")
        opcao = super().ler_entrada([1, 2, 3, 0])
        return opcao
