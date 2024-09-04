

saque = None
deposito = 0
extrato = ""
saldo = 0
qtdSaques = 0

while(True):

    opcao = input("Qual operacao deseja realizar(1 - Depositar, 2 - Sacar, 3 - Verificar o extrato, 4 - Sair)?\n")

    if(int(opcao) == 1):

        deposito = int(input("Digite quanto voce quer depositar:"))
        saldo += deposito
        extrato += f"Deposito: R${deposito:.2f}\n"

    elif(int(opcao) == 2):

        if(qtdSaques == 3):
            print("Quantidade maxima de saques usadas!!!")

        saque = int(input("Digite quanto voce quer sacar:"))

        if((saldo - saque) < 0):
            print("Saldo Insuficiente!!!")
            
        elif(saque > 500):
            print("Superou o limite maximo de R$500,00 por saque.")
        else:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            qtdSaques += 1

    elif(int(opcao) == 3):
         print(extrato)
    elif(int(opcao) == 4):
        break
    
    
print("Saindo...")