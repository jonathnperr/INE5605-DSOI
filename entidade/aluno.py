from entidade.pessoa import Pessoa 
from entidade.curso import Curso
  
class Aluno(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, matricula, curso: Curso): 
        super().__init__(nome, cpf, data_nascimento)
        self.__matricula = matricula
        self.__curso = curso  
        self.__pontuacao = 0 

    @property 
    def matricula(self):
        return self.__matricula
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula

    @curso.setter
    def curso(self, curso):
        self.__curso = curso
        
    @pontuacao.setter
    def pontuacao(self, pontuacao: int):
        self.__pontuacao = pontuacao