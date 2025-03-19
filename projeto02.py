import textwrap

def menu():
    menu =  """\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNova usuário
    [nc]\tNovo conta
    [lc]\tLista contas
    [q]\tSair
    => """
    
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n === Depósito realizado com sucesso! ===")

    else:
            print("\n @@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n === Saque realizado com sucesso! ===")

    else:
        print("@@@ Operação falhou! O valor informado é inválido.@@@")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
     
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def novo_usuario(usuarios):
     
     cpf = input(("Digite o CPF (Somente números): "))

     usuario_existente = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

     if usuario_existente:
        print("CPF já existe!")
        return
     
     nome = input("Informe o nome completo: ")
     data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
     endereco = input("Informe o endereço (logradouro, número - bairro - cidade/estado): ")
    
     usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "endereço": endereco,
        "data_nascimento": data_nascimento
     })

     print("Usuário criado com sucesso!")


def nova_conta(usuarios, contas, agencia = "0001"):
     
     cpf = input(("Digite o CPF (Somente números): "))

     usuario_existente = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

     if not usuario_existente:
        print("Usuário não encontrado! Realize o cadastro antes. ")
        return
     
     numero_conta = len(contas) + 1
    
     usuarios.append({
        "Agencia": agencia,
        "numero_conta": numero_conta,
        "cpf": cpf
     })

     print(f"Conta criada com sucesso! Agência: {agencia} Conta: {numero_conta}")
     

def listar_contas(contas):
    print("\n======= LISTA DE CONTAS =======")
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | CPF: {conta['cpf']}")
    print("===============================")


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
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
             valor = float(input("Informe o valor do saque: "))
             saldo, extrato = sacar(
                  saldo = saldo,
                  valor = valor,
                  extrato= extrato,
                  limite = limite,
                  numero_saques=numero_saques,
                  limite_saques=LIMITE_SAQUES
             )
        
        elif opcao == "e":
             exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            novo_usuario(usuarios)
        elif opcao == "nc":
            nova_conta(usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")


main()