contatos = {'matheus@gmail.com': {'nome': 'Matheus', 'telefone': '3333-6543'}}

resultado= contatos.get('chave')
print(resultado)

resultado = contatos.get('chave', {})
print(resultado)

resultado = contatos.get(
    'matheus@gmail.com', {}
)
print(resultado)