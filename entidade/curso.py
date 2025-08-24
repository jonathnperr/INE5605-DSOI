   
class Curso:
    def __init__(self, cod_curso, nome_curso) -> None:
        self.__cod_curso = cod_curso
        self.__nome_curso = nome_curso

    @property
    def cod_curso(self): 
        return self.__cod_curso
    
    @property
    def nome_curso(self):
        return self.__nome_curso
     
    @cod_curso.setter
    def cod_curso(self, cod_curso):
        self.__cod_curso = cod_curso

    @nome_curso.setter
    def nome_curso(self, nome_curso):
        self.__nome_curso = nome_curso