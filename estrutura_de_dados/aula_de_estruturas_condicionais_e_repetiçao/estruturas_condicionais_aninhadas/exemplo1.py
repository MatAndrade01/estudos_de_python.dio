conta_normal = True
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado usando o cheque especial!')
    else:
        print('Não foi possivel realizar o saque!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
elif conta_especial:
    print('Conta especial selecionada')
else:
    print('O sistema não reconheceu o tipo de conta entre em contato com seu gerente.')