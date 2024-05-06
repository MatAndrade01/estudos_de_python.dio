def somar(a, b):
    return a + b

def subitrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + b * 3

def exibi_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é = {resultado}')

exibi_resultado(10, 10, somar)
exibi_resultado(10, 10, subitrair)
exibi_resultado(10, 10, test)

op = somar 

print(op(1, 23))