from datetime import datetime

""" Deposito, Saque e Extrato """

contas = []
usuarios = []
historico = []
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

def cadastrarUsuario():
    global usuarios

    print("""
           CADASTRAR USUARIO
    ==============================
""")

    #nome, data_nascimento, cpf, endereço: logradouro, num, bairro, cidade/estado
    novo_usuario = {
        "nome": input("Nome: "),
        "data_nascimento": datetime.strftime(input("Data de nascimento: "),"%d/%m/%Y"),
        "cpf": input("CPF: ").replace(".", "").replace("-", ""),
        "endereco": {
            "logradouro":input("Logradouro: "),
            "num": input("Número: "),
            "bairro": input("Bairro"),
            "cidade/estado": input("Cidade/Estado")
        }
    }

    usuarios.append(novo_usuario)


def cadastrarConta():
    global contas
    #agencia, numero, usuario
    nova_conta = {
        "agencia": input("Agência: "),
        "numero": input("Número: "),
        "usuario": input("CPF: ").replace(".", "").replace("-","")
    }

    contas.append(nova_conta)
    


def registrarExtrato(acao):
    global extrato
    global historico

    #Registra no extrato
    extrato += f"Horario: {datetime.now().strftime('%d/%m/%Y')} - {acao}\n"
    #Adiciona no histórico de registros
    historico.append(datetime.now().strftime('%d/%m/%Y'))

def checarLimite():
    global historico

    #Checa quantas transações foram feitas hoje.
    if(historico.count(datetime.now().strftime('%d/%m/%Y')) >= 10):
        return True
    else:
        return False

def depositar(valor):
    global saldo
    global extrato
    global historico


    saldo += valor
    registrarExtrato(f"Deposito: + R${valor}")

def sacar(valor):
    global saldo
    global extrato

    if(valor>saldo):
        print("Saldo insuficiente.")
        return

    saldo-= valor
    registrarExtrato(f"Saque: - R$ {valor}")

print(mensagem)
while True:

    if(checarLimite()):
        print("Limite de transações atigindo.")
        break

    opcao = input("Opção desejada: ")

    if(opcao == "1"):
        valor = int(input("Valor de deposito: "))
        depositar(valor)
        continue
    elif(opcao == "2"):
        if(saldo == 0):
            print("Saldo insuficiente.")
            continue
        else:
            retirar = int(input("Valor de saque: "))
            sacar(retirar)
            continue
    elif(opcao == "3"):
        print(f"Extrato: \n{extrato}")
        print(f"Saldo: R$:{saldo}")
    elif(opcao == "4"):

        continue
    else:
        print("Opção invalida")
      


