teste = True
texto = "Transcenda o mundo material."
VOGAIS = "AEIOU"
conta = 0


if teste:
    print("Oh noh!")
    teste = False

if not teste:
    print("Oh yeah")
    teste = True

for letra in texto:
    print(letra, end=" ")

for letra in texto:
    if letra in VOGAIS:
        print(letra, end=" ")

for numero in range(10):
    print(numero)

for numero in range(0,10,2):
    print(numero)

while conta < 10:
    print("Contando")
    conta+= 1