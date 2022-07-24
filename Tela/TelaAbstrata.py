from abc import ABC, abstractmethod
import PySimpleGUI as sg


class TelaAbstrata(ABC):
    @abstractmethod
    def __init__(self):
        self.__window = None

    def opcoes_cadastro(self, nome):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text(f'Cadastro dados pessoais do {nome}', font=('Arial', 25))],
            [sg.Text('Nome: ', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="nome")],
            [sg.Text('Idade: ', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="idade")],
            [sg.Text('CPF: ', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="cpf")],
            [sg.Text('Peso: ', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="peso")],
            [sg.Text('Altura: ', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="altura")],
            [sg.Text('Senha: ', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="senha", password_char='*')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Cadastro dados pessoais').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None
        self.__window.Close()
        if self.check_type(values['nome'], "nome") and self.check_type(values["idade"], int) and \
                self.check_type(values["cpf"], int) and self.check_type(values["peso"], float) and \
                self.check_type(values["altura"], float) and self.check_type(values["senha"], str):
            return {"nome": values["nome"], "idade": int(values["idade"]),
                    "cpf": int(values["cpf"]), "peso": float(values["peso"]),
                    "altura": float(values["altura"]), "senha": values["senha"]}

    def mensagem(self, titulo, mensagem):
        sg.popup(titulo, mensagem)

    def mensagem_error(self, mensagem):
        sg.popup_error(mensagem)

    def check_type(self, opcao, tipo):
        try:
            if opcao is not None:
                if tipo == "nome":
                    tipo = str
                    if opcao.isnumeric():
                        raise ValueError
                elif tipo == int:
                    opcao = int(opcao)
                elif tipo == float:
                    opcao = float(opcao)
                if not isinstance(opcao, tipo):
                    raise ValueError
                return True
        except ValueError:
            sg.popup_error("Por favor, preencha os dados corretamente!")
            return None

    def login(self):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text('Matrícula:', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="matricula")],
            [sg.Text('Senha:', size=(11, 1), font=('Arial', 15)), sg.InputText('', key="senha", password_char='*')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Login').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None
        self.__window.Close()
        if self.check_type(values['matricula'], int):
            return {"matricula": int(values['matricula']), "senha": values['senha']}
        else:
            return None

    def escolher_codigo(self, mensagem):
        sg.ChangeLookAndFeel('DarkTeal10')
        layout = [
            [sg.Text(mensagem, font=('Arial', 25))],
            [sg.Text('Código: ', font=('Arial', 15)), sg.InputText('', key="codigo")],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window(mensagem).Layout(layout)
        button, values = self.__window.Read()
        if button in (None, 'Cancelar'):
            self.__window.Close()
            return None
        self.__window.Close()
        if self.check_type(values['codigo'], int):
            return int(values['codigo'])
        else:
            return None

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self, window):
        window.Close()

    def exit(self):
        self.exit()
