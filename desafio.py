menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[0] Sair

Digite a operação: '''

saldo = 0
limite = 500
LIMITE_SAQUES = 3
numero_saques = 0
deposito = 0
total_depositado = 0
saque = 0
total_sacado = 0
extrato = ''

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        
        deposito = float(input("Digite o valor de depósito: "))

        if deposito > 0:
            saldo = saldo + deposito
            total_depositado = total_depositado + deposito
            extrato = extrato + f"Depósito: R$ {deposito:.2f} \n"
        else:
            print("Valor inválido")
        
        
    elif opcao == "s":
        print("Saque")

        saque = float(input("Digite o valor que deseja sacar: "))

        if saque > limite:
            print("Saldo insuficente")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Você excedeu o limite de saques")

        elif saque > limite:
            print(f"O valor limite do saque é de R$ {limite:.2f}")
            
        elif saque > 0:
            numero_saques += 1
            saldo = saldo - saque
            total_sacado = total_sacado - saque
            extrato = extrato + f"Saque: R${saque:.2f}\n"
        else:
            print("Não foi possível realizar seu saque.")
    
    elif opcao == "e":
        print("Extrato")
        print(f"Saldo igual a R$ {saldo:.2f}")
        print(f"Total depositado = R$ {total_depositado:.2f}")
        print(f"Total sacado = R$ {total_sacado:.2f}")
        print(extrato)

    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Operação inválida. Digite uma opção válida! ")   