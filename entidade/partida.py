from entidade.arbitro import Arbitro
from entidade.equipe import Equipe 
from entidade.aluno import Aluno 

class Partida: 
    def __init__(self, id_partida, data, arbitro: Arbitro, ganhador: Equipe, perdedor: Equipe, sets_perdedor, pont_ganhador, maior_pontuador: Aluno):
        self.__id_partida = id_partida
        self.__data = data
        self.__arbitro = arbitro
        self.__ganhador = ganhador
        self.__perdedor = perdedor
        self.__sets_ganhador = 3
        self.__sets_perdedor = sets_perdedor
        self.__pont_ganhador = pont_ganhador
        self.__maior_pontuador = maior_pontuador

    @property
    def id_partida(self):
        return self.__id_partida
        
    @id_partida.setter
    def id_partida(self, id_partida):
        self.__id_partida = id_partida
    
    @property
    def data(self):
        return self.__data
        
    @data.setter
    def data(self, data):
        self.__data = data
        
    @property
    def arbitro(self):
        return self.__arbitro
        
    @arbitro.setter
    def arbitro(self, arbitro):
        self.__arbitro = arbitro
        
    @property
    def ganhador(self):
        return self.__ganhador
        
    @ganhador.setter
    def ganhador(self, ganhador):
        self.__ganhador = ganhador
        
    @property
    def perdedor(self):
        return self.__perdedor
        
    @perdedor.setter
    def perdedor(self, perdedor):
        self.__perdedor = perdedor
        
    @property
    def sets_ganhador(self):
        return self.__sets_ganhador
        
    @sets_ganhador.setter
    def sets_ganhador(self, sets_ganhador):
        self.__sets_ganhador = sets_ganhador
        
    @property
    def sets_perdedor(self):
        return self.__sets_perdedor
        
    @sets_perdedor.setter
    def sets_perdedor(self, sets_perdedor):
        self.__sets_perdedor = sets_perdedor
        
    @property
    def pont_ganhador(self):
        return self.__pont_ganhador
        
    @pont_ganhador.setter
    def pont_ganhador(self, pont_ganhador):
        self.__pont_ganhador = pont_ganhador
        
    @property
    def maior_pontuador(self):
        return self.__maior_pontuador
        
    @maior_pontuador.setter
    def maior_pontuador(self, maior_pontuador):
        self.__maior_pontuador = maior_pontuador
        
    
