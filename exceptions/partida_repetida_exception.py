class PartidaRepetidaException(Exception):
    def __init__(self, cod_partida):
        self.mensagem = "Partida com cód. {} já cadastrado"
        super().__init__(self.mensagem.format(cod_partida))  