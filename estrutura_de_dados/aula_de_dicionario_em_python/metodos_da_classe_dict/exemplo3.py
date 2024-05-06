contatos = {'matheus@gmail.com': {'nome': 'Matheus', 'telefone': '3333-6543'}}

resultado = contatos.pop('matheus@gmail.com')
print(resultado)

resultado = contatos.pop('matheus@gmail.com', 'Nao encontrou!')
print(resultado)
