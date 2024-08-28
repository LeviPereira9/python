nome = "Levi"
idade = 24
curso = "ADS"
PI = 3.14159

print("Olá, meu nome é %s, tenho %d anos e estudo %s na Fatec" %(nome, idade, curso))
print("Olá, meu nome é {1}, tenho {2} anos e estudo {0} na Fatec".format(curso, nome, idade))
print("Olá, meu nome é {nome}, tenho {idade} anos e estudo {curso} na Fatec".
      format(
          nome=nome, 
          idade=idade, 
          curso=curso
        )
    )

print(f"Olá meu nome é {nome}, tenho {idade} e estudo {curso} na Fatec ")
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

