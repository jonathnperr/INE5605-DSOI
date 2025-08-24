from DAOs.dao import DAO
from entidade.aluno import Aluno  

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('alunos.pkl')

    def add(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.matricula, int)):
            super().add(aluno.matricula, aluno)

    def update(self, aluno: Aluno):
        if((aluno is not None) and isinstance(aluno, Aluno) and isinstance(aluno.matricula, int)):
            super().update(aluno.matricula, aluno)
 
    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)