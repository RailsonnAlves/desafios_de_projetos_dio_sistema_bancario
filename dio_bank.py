LIMITE_SAQUE = 3
valor_maximo = 500.0
numero_saque = 0
saldo = 1500.00
extrato = []

PARTE_SUPERIOR = '\n##########--Dio Bank--##########'
PARTE_INFERIOR = '################################'

mensagem_de_seguraca = f"""
##########--Dio Bank--##########

Por motivos de segurança seu valor
maximo de saque é R$ {valor_maximo}

################################
"""

MENU = """
##########--Dio Bank--##########

[1]Saque
[2]Déposito
[3]Extrato
[4]Sair

################################
"""

mensagem_de_despedidas = f"""
{PARTE_SUPERIOR}

Até logo, nós da Dio Bank
agradecemos a preferência

{PARTE_INFERIOR}
"""

while True:
    operacao = input(f"{MENU}Digite o numero da operação.\n")
    # saque
    if operacao == '1':
        if numero_saque < 3:
            print(PARTE_SUPERIOR, '\n')
            valor_de_saque = float(input("Digite o valor que deseja sacar:\n"))

            if valor_de_saque <= saldo and valor_de_saque <= valor_maximo and valor_de_saque > 0:
                print("Realizando saque.")
                saldo -= valor_de_saque
                numero_saque += 1
                string_saque = f"Saque.............R$ {valor_de_saque:.2f}"
                extrato.insert(0, string_saque)

            elif valor_de_saque > saldo:
                print("Saldo insuficiente.")

            elif valor_de_saque > valor_maximo:
                print(mensagem_de_seguraca)
                sair = input("Digite 1 para Continuar e 4 para sair:\n")

                if sair == '1':
                    pass

                elif sair == '4':
                    print(mensagem_de_despedidas)
                    break

            elif valor_de_saque < 0:
                print("O valor informado é invalido")

        else:
            print("""Você só pode fazer 3 saques diário.""")
    # Déposito
    elif operacao == '2':
        valor_de_deposito = float(input("Insira o valor de déposito.\n"))
        if valor_de_deposito > 0:
            print("Realizando déposito.")
            saldo += valor_de_deposito
            extrato.insert(0, f"Déposito..........R$ {valor_de_deposito:.2f}")
        else:
            print("Valor de déposito invalido")
    # Extrato..
    elif operacao == '3':
        extrato.insert(len(extrato)+1, f"\n\nSaldo.............R$ {saldo:.2f}")
        print("""Extrato referente ás suas
ultimas transações\n\n""")
        for i in extrato:
            print(i)
    # Sair
    elif operacao == '4':
        print(mensagem_de_despedidas)
        break
    else:
        print(f"""{PARTE_SUPERIOR}

A opção escolhida não existe,
por favor selecione uma opção
do menu, usando o teclado numérico

{PARTE_INFERIOR}""")
