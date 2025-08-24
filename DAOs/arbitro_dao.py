from DAOs.dao import DAO
from entidade.arbitro import Arbitro  

class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitros.pkl')

    def add(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance(arbitro.cpf, int)):
            super().add(arbitro.cpf, arbitro)

    def update(self, arbitro: Arbitro):
        if((arbitro is not None) and isinstance(arbitro, Arbitro) and isinstance(arbitro.cpf, int)):
            super().update(arbitro.cpf, arbitro)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)