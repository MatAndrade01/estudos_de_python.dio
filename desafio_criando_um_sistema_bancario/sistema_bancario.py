saldo = 0
limite = 500
extrato = ''
numeros_de_saque = 0
LIMITE_DE_SAQUES = 3


print('''
======================= OPERAÇÕES =======================
      
      [1] - SAQUE
      [2] - DEPOSITO
      [3] - EXTRATO
      [0] - SAIR

=========================================================
''')

opcao = int(input('Escolha a operção que você deseja: '))

while True:

    if opcao == 1:
        if numeros_de_saque == LIMITE_DE_SAQUES:
            print(f'O seu limte de saques foi atingido: {numeros_de_saque}')
            print()
            opcao = int(input('Escolha outra opção: '))
        else:
            valor_do_saque = int(input('Quanto deseja sacar: '))

            if valor_do_saque > limite:
                print(f'O valor digitado é maior que o seu limite por saque, digite um valor até {limite}')
                print()

            elif valor_do_saque > saldo:
                print('Saldo insuficiente, escolha um valor dentro do seu saldo.')
        
            elif valor_do_saque <= saldo and valor_do_saque <= limite:
                numeros_de_saque += 1
                saldo -= valor_do_saque
                print(f'''Saque no valor de {valor_do_saque} realizado,
                      Quantidade de saques: {numeros_de_saque}''')
                print()
                continuar_sacando = int(input(f'Seu saldo é de {saldo}, deseja continuar sacando. [1] - SIM | [2] - NÃO: '))

                if continuar_sacando == 1:
                    if numeros_de_saque == LIMITE_DE_SAQUES:
                        print(f'O seu limte de saques foi atingido: {numeros_de_saque}')
                        opcao = int(input('Escolha outra operação: '))
                    else:
                        valor_do_saque = int(input('Quanto deseja sacar: R$'))
                        if valor_do_saque > limite:
                            print(f'O valor digitado é maior que o seu limite por saque, digite um valor até R${limite}')
                            print()

                        elif valor_do_saque > saldo:
                            print('Saldo insuficiente, escolha um valor dentro do seu saldo.')
                        
                        elif valor_do_saque  <= saldo and valor_do_saque <= limite:
                            numeros_de_saque += 1
                            saldo = saldo - valor_do_saque
                            print(f'''Saque no valor de R${valor_do_saque} realizado,
                            Quantidade de saques: {numeros_de_saque}''')
                            print()
                            continuar_sacando = int(input(f'Seu saldo é de {saldo}, deseja continuar sacando. [1] - SIM | [2] - NÃO: '))
                elif continuar_sacando == 2:
                    print()
                    opcao = int(input('Escolha a operção que você deseja: '))
    
    elif opcao == 2:
        print()
        print(f'Seu Saldo atual é de: R${saldo}')
        print()
        valor_do_deposito = float(input('Quando você deseja depositar: R$'))
        saldo += valor_do_deposito
        print(f'Deposito realizado seu saldo atual é de R${saldo}')

        fazer_novo_deposito = int(input('Deseja fazer um novo deposito [1] - SIM | [2] - NÃO: '))
        while fazer_novo_deposito != 1 and fazer_novo_deposito != 2:
            print('Digite um valor valido!')
            fazer_novo_deposito = int(input('Deseja fazer um novo deposito [1] - SIM | [2] - NÃO: '))
        if fazer_novo_deposito == 1:
            print(f'Seu Saldo atual é de: R${saldo}')
            valor_do_deposito = float(input('Quando você deseja depositar: R$'))
            saldo += valor_do_deposito
            print(f'Deposito realizado seu saldo atual é de R${saldo}')
            fazer_novo_deposito = int(input('Deseja fazer um novo deposito [1] - SIM | [2] - NÃO: '))

        
        elif fazer_novo_deposito == 2:
            print('''
            ======================= OPERAÇÕES =======================
      
                [1] - SAQUE
                [2] - DEPOSITO
                [3] - EXTRATO
                [0] - SAIR

            =========================================================
            ''')
            opcao = int(input('Escolha a operção que você deseja: '))

    