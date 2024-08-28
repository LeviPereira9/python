""" Deposito, Saque e Extrato """

limite_saque_diario = 3
maximo_saque = 500
saldo = 2000
extrato = ""
mensagem = """
=============MENU=============

1 - Deposito
2 - Saque
3 - Extrato
0 - Finalizar

==============================
"""

print(mensagem)
while True:

    opcao = input("Opção desejada: ")

    if(opcao == "1"):
        deposito = input("Valor de deposito: ")
        saldo += int(deposito)
        extrato += f"Deposito: +R${deposito}\n"

    elif(opcao == "2"):
        
        if(limite_saque_diario == 0):
            print("Limite de saque atigindo.")
            continue
        elif(saldo == 0):
            print("Saldo insuficiente.")
            continue
        else:
            retirar = int(input("Valor de saque: "))
            if(retirar>saldo):
                print("Saldo insuficiente.")
            else:
                saldo -= retirar
                extrato += f"Saque: -R$:{retirar} \n"
                limite_saque_diario-= 1
            

    elif(opcao == "3"):
        print(f"Extrato: \n{extrato}")
        print(f"Saldo: R$:{saldo}")

    elif(opcao == "4"):
        break
    
    else:
        print("Opção invalida")
      


