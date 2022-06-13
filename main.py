from Controle.CtrlSistema import CtrlSistema
from Entidade.professor import Professor

if __name__ == "__main__":
    ctrl_sistema = CtrlSistema()
    professor = Professor("Roberto", "admin123", 35, 12543542354, 80, 1.90, 1111)
    ctrl_sistema.controlador_professor.professor = professor
    ctrl_sistema.inicializar()
