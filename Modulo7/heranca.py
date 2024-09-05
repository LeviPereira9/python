class Veiculo:
    
    def __init__(self, motor, cor, modelo, rodas) -> None:
        self.motor = motor
        self.cor = cor
        self.modelo = modelo
        self.rodas = rodas
    
    def __str__(self) -> str:
       return f" {self.__class__.__name__}: {{ {', '.join([f'{chave} = {valor} ' for chave, valor in self.__dict__.items()])} }}"

    def buzinar(self, som):
        print(f"{som} - {som}")

    def acelerar(self):
        print("Acelerando")

    def parar(self):
        print("Parando...")

class Caminhao(Veiculo):

    def __init__(self, motor, cor, modelo, rodas) -> None:
        super().__init__(motor, cor, modelo, rodas)
    
    pass

class Moto(Veiculo):
    pass

c1 = Caminhao("O melhor", "Verde", 2024, 12)
c2 = Moto("Com cilindro", "Amarela", 2009, 2)

print(c1)
print(c2)