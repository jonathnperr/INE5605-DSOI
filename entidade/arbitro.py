from entidade.pessoa import Pessoa
    
class Arbitro(Pessoa):
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__(nome, cpf, data_nascimento)
        self.__numero_partidas = 0

    @property
    def numero_partidas(self):
        return self.__numero_partidas 
    
    @numero_partidas.setter
    def numero_partidas(self, numero_partidas: int):
        self.__numero_partidas = numero_partidas
        