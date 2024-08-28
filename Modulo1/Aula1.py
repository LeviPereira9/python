nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")

print(nome, sobrenome)
print(nome, sobrenome, end="?\n")
print(nome, sobrenome, sep="_")

sobrenome.replace(" ", "_", -1)
print(nome, sobrenome)