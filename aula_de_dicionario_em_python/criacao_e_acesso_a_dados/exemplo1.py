contatos = {
    "guilherme@gmai.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    'giovana@gmail.com': {'nome': 'Giovana', 'telefone': '3443-2121'},
    'chappin@gmail.com': {'nome': 'Chappie', 'telefone': '3344-9871'},
    'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766', 'extra': {'a': 1}},
}

telefone = contatos['giovana@gmail.com']['telefone']
print(telefone)

extra = contatos['melaine@gmail.com']['extra']['a']

print(extra)