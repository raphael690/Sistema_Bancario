import datetime
# cores para o terminal --------------------------
RED = "\033[91m"
BLUE = "\033[94m"
ENDC = "\033[0m"

sistema = print("""  
    ===========Sistema Bancario=========== 
                """)
menu = """
    =============== menu ==================  
    [d]{blue} Depositar{end}
    [s]{red} Sacar{end}
    [e] Extrato
    [q] Sair
    
=> """.format(blue=BLUE, red=RED, end=ENDC)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
#saque_especial = 450
LIMITE_SAQUES = 3


# loop principal -----------------------------------------------------------------------------------------------
while True:

    opcao = input(menu)
# ---------------------------------Depósito ------------------------------
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print("Operação falhou! O valor informado é inválido. Tente novamente!")

# --------------------------------saque-------------------------------------   
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        

        if excedeu_saldo:    
         print("Operação falhou! Você não possui saldo suficiente!")
         
        elif excedeu_limite:
         print("Operação falhou! O valor do saque excedeu o limite!")

        elif excedeu_saques:            
         print("Operação falhou! Número máximo de saques foi excedido!")

        
        elif valor > 0:
         saldo -= valor 
         extrato += f'Saque: R$ {valor:.2f}\n'
         numero_saques += 1

        else:
         print("O limite de saque diario foi excedido (x3).")


 
# ---------------------------Extrato------------------------------------------
    elif opcao == "e":

         print("\n==========EXTRATO==========")
         print("Não foram realizadas movimentações." if not extrato else extrato)
         print(f"\nSaldo: R$ {saldo:.2f}")
         print("==============================")
# --------------------------Sair-----------------------------------------------    
    elif opcao == "q":
         break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")