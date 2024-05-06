def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Sejá bem vindo {nome}')

def exibir_mensagem_3(nome='Anônimo'):
    print(f'Sejá bem vindo {nome}')

exibir_mensagem()
exibir_mensagem_2(nome='Matheus')
exibir_mensagem_3()
exibir_mensagem_3(nome='Milena')