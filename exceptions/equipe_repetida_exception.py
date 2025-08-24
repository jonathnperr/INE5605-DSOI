class EquipeRepetidaException(Exception):
    def __init__(self, cod_equipe):
        self.mensagem = "Equipe com código ou curso já cadastrado" 
        super().__init__(self.mensagem.format(cod_equipe)) 