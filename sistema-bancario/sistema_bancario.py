menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            print("Depósito feito com sucesso!")
            saldo += valor
            extrato += f"Depósito R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente!")
        
        elif excedeu_limite:
            print("O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Você excedeu o número de saques!")

        elif valor > 0:
            print("Saque efetuado com sucesso!")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1

        else:
            print("Valor informado é inválido")     

    elif opcao == "e":
        print("\n=================== EXTRATO ==================")
        print("Não foram realizadas movimentaçoẽs." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==============================================")               

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    



            