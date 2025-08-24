from DAOs.dao import DAO
from entidade.curso import Curso   

class CursoDAO(DAO):
    def __init__(self):
        super().__init__('cursos.pkl')

    def add(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.cod_curso, int)):
            super().add(curso.cod_curso, curso)

    def update(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.cod_curso, int)):
            super().update(curso.cod_curso, curso)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)