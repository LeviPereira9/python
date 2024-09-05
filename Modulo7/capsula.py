class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
""" 
@property - Define um método que pode ser acessado como um atributo.
@nome.setter - Define um método para atribuir um valor a uma propriedade.
@nome.deleter - Define um método para deletar uma propriedade.
@classmethod - Define um método de classe que recebe a própria classe como primeiro argumento (cls).
@staticmethod - Define um método estático que não recebe o primeiro argumento especial (como self ou cls).

 """


pessoa = Pessoa("Guilherme", 1994)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")