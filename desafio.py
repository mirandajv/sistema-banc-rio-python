menu = """ 

Selecione a operação desejada:

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

    opçao = input(menu)

    if opçao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else: 
            print ("Operação falhou! O valor informado não é válido!")

    
    
    elif opçao == "s":
        saque = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não foi possivel completa a operação por falta de saldo")

        elif excedeu_limite:
            print("O valor solicitado excede o limite atual da sua conta, verifique seu limite e tente novamente")

        elif excedeu_saques:
            print("Limite de saques diários atingido")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            print("Saque efetuado com sucesso!")
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado não é válido!")

    elif opçao == "e":
        print(f"Operações efetuadas:\n{extrato} \n Saldo: {saldo:.2f} \n Saque restantes: {LIMITE_SAQUES-numero_saques}")

    elif opçao == "q":
        break

    else:
        print("Operação inválida, por favor selecione ovamente a opção desejada.")
