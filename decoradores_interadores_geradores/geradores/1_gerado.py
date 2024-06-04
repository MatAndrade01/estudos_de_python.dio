def meu_gerador():
    texto = 'PYTHON'
    yield texto

for i in meu_gerador():
    print(i)
