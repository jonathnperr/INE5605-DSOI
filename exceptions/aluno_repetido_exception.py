class AlunoRepetidoException(Exception):
    def __init__(self):
        self.mensagem = "Aluno com informações inseridas já cadastrado."
        super().__init__(self.mensagem.format()) 