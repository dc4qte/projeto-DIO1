import textwrap

def menu():
    menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova onta
    [lc] Lista contas
    [nu] Novo usario
    [0] Sair

    Digite a operação: '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato = extrato + f"Depósito: R$ {valor:.2f} \n"
    else:
         print("Valor inválido")
        
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite_saques = numero_saques >= limite_saques
    excedeu_valor = valor > limite

    if excedeu_saldo:
        print("Saldo insuficente")
        
    elif excedeu_limite_saques:
        print("Você excedeu o limite de saques")

    elif excedeu_valor:
            print(f"O valor limite do saque é de R$ {limite:.2f}")   
    elif valor > 0:
        numero_saques += 1
        saldo -= valor
        extrato = extrato + f"Saque: R${valor:.2f}\n"
        print("Saque realizade com sucesso")
    else:
        print("Não foi possível realizar seu saque.")

    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
        
    print("Extrato")
    print("Nao foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf" : cpf, "endereco": endereco})
    print("Usuario criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta" : numero_conta, "usuario": usuario}
    print("Usuario não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
            

def main():
    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3
    numero_saques = 0
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Digite o valor do saque: "))

            saldo, extrato = sacar(
                saldo= saldo,
                valor= valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
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
        elif opcao == "0":
            break
        else:
            print("Operação inválida")

main()
