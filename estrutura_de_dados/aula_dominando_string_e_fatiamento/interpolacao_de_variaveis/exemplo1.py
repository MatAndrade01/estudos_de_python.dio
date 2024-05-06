nome = 'Matheus'
idade = 21
profissao = 'Programador'
liguagem = 'Python'
saldo= 45.435

dados = {'nome': 'Matheus', 'idade': 21}

print('Nome: %s Idade: %d' %(nome, idade))

print('Nome: {} Idade: {}'.format(nome, idade))

print('Nome: {1} Idade: {0}'.format(idade, nome))
print('Nome: {1} Idade: {0} Nome: {1} {1}'.format(idade, nome))

print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))
print('Nome: {nome} Idade: {idade} {nome} {nome} {idade}'.format(idade=idade, nome=nome))
print('Nome: {nome} Idade: {idade}'.format(**dados))

print(f'Nome: {nome} Idade {idade}')
print(f'Nome: {nome} Idade {idade} Saldo: {saldo:.2f}')
print(f'Nome: {nome} Idade {idade} Saldo: {saldo:10.2f}')