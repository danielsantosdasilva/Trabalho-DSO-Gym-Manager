from Controle.CtrlSistema import CtrlSistema
from banco_dados import BancoDados

if __name__ == "__main__":
    ctrl_sistema = CtrlSistema()
    BancoDados(ctrl_sistema).rodar()
    ctrl_sistema.inicializar()
