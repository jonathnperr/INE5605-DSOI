from entidade.curso import Curso
  
class Equipe:
    def __init__(self, cod_equipe, curso: Curso, nome_equipe):
        self.__cod_equipe = cod_equipe
        self.__curso = curso
        self.__nome_equipe = nome_equipe 
        self.__alunos = []
        self.__pontuacao_total = 0
        self.__levou_a_3x2 = 0  

    @property  
    def cod_equipe(self):
        return self.__cod_equipe
    
    @property   
    def curso(self):
        return self.__curso
    
    @property
    def nome_equipe(self):
        return self.__nome_equipe
    
    @property
    def alunos(self):
        return self.__alunos
    
    @property
    def pontuacao_total(self):
        return self.__pontuacao_total
    
    @property
    def levou_a_3x2(self):
        return self.__levou_a_3x2
        
    @cod_equipe.setter
    def cod_equipe(self, cod_equipe):
        self.__cod_equipe = cod_equipe

    @curso.setter
    def curso(self, curso):
        self.__curso = curso

    @nome_equipe.setter
    def nome_equipe(self, nome_equipe):
        self.__nome_equipe = nome_equipe
        
    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos
        
    @pontuacao_total.setter
    def pontuacao_total(self, pontuacao_total):
        self.__pontuacao_total = pontuacao_total
        
    @levou_a_3x2.setter
    def levou_a_3x2(self, levou_a_3x2):
        self.__levou_a_3x2 = levou_a_3x2