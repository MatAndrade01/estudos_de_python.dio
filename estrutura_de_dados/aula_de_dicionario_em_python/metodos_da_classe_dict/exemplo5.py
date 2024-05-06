contatos = {
    "guilherme@gmai.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3443-2121'},
    'chappin@gmail.com': {'nome': 'Chappie', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766', 'extra': {'a': 1}},
}

resultado = 'guilherme@gmail.com' in contatos
print(resultado)

resultado = 'melaine@gmail.com' in contatos
print(resultado)

resultado = 'idade' in contatos['guilherme@gmai.com']
print(resultado)

resultado = 'telefone' in contatos['giovana@gmail.com']
print(resultado)
