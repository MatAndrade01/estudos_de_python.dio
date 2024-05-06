def calcular_total(numeros):
    return sum(numeros)

def retonar_antecessor_e_sucesso(numeros):
    antecessor = numeros - 1
    sucessor = numeros + 1

    return antecessor, sucessor

def func_3():
    print('Olá mundo!')

print(calcular_total([10, 20, 34]))
print(retonar_antecessor_e_sucesso(10))
print(func_3())