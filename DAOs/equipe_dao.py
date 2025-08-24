from DAOs.dao import DAO
from entidade.equipe import Equipe  

class EquipeDAO(DAO):
    def __init__(self):
        super().__init__('equipes.pkl')

    def add(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance(equipe.cod_equipe, int)):
            super().add(equipe.cod_equipe, equipe)

    def update(self, equipe: Equipe):
        if((equipe is not None) and isinstance(equipe, Equipe) and isinstance(equipe.cod_equipe, int)):
            super().update(equipe.cod_equipe, equipe)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)