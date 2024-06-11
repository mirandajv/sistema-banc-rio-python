def menu():
    menu_texto = """ \n
    ======================== Menu =============================
    Selecione a operação desejada:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    ==> """
    return input(menu_texto)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Operação falhou, não foi possível concluir o depósito")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    
    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif excedeu_saldo:
        print("Saldo insuficiente, verifique seu extrato e tente novamente.")
    elif excedeu_limite:
        print("O valor solicitado excede o limite atual da sua conta, verifique seu limite e tente novamente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
        numero_saques += 1
    else:
        print("Operação falhou, o valor informado não é válido!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("============================= Extrato ==============================\n")
    if not extrato:
        print("Não foram realizadas movimentações")
    else:
        print(f"\tOperações efetuadas:\n{extrato} \n \tSaldo: R$ {saldo:.2f} \n")
    print("===================================================================")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente")
        return
    
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Rua, bairro, cidade, sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "nome": usuario['nome']}
    print("\nUsuário não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        CC: {conta['numero_conta']}
        Titular: {conta['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0  
    limite = 500    
    extrato = ""    
    numero_saques = 0 
    usuarios = []
    contas = [] 
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Insira o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione a operação desejada.")

if __name__ == "__main__":
    main()
