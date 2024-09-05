class Bicicleta:

    #Todo metodo incluindo o construtor, precisa iniciar com o self de parametro.
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("HOOOOOONK HONK")

    def freio(self):
        print("IIIIIHHHGGGG")
        print("parou")

    def acelerar(self):
        print("Boboboot")
        print("Acelerou")

    # Caso a gente queira criar o metodo toString, é simples, segue o pai:
    
    
    #Na mão
    """def __str__(self) -> str:
            return f'''
    {{
        "Cor": "{self.cor}",
        "Modelo: "{self.modelo}",
        "Ano": {self.ano},
        "Valor: {self.valor}
    }}'''
    """
    #Automatizado
    def __str__(self):
       return f"
       {self.__class__.__name__} :
         {', '.
          join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 


    
 
b1 = Bicicleta("Vermelho", "Mitsubishi", 2024, 350)

print(b1)