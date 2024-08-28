def somar(a, b):
    return a + b

def calcular(a,b, funcao):
    resultado = funcao(a,b)

    print(f"Resultado de {a} + {b} = {resultado}")

calcular(1,2,somar)