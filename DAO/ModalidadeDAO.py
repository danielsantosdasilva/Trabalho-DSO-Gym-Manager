from DAO.AbstractDAO import AbstractDAO
from Entidade.modalidade import Modalidade


class ModalidadeDAO(AbstractDAO):
    def __init__(self):
        super().__init__('modalidades.pkl')

    def add(self, modalidade: Modalidade):
        if isinstance(modalidade, Modalidade) and modalidade is not None:
            super().add(modalidade.codigo, modalidade)

    def get(self, codigo: int):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo: int):
        if isinstance(codigo, int):
            return super().remove(codigo)
