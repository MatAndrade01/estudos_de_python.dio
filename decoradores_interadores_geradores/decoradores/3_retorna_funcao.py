def calculadora(operacao):
    def soma(a,b):
        return a + b
    
    def sub(a,b):
        return a - b
    
    def mul(a,b):
        return a * b
    
    def div(a,b):
        return a / b
    
    if operacao == '+':
        return soma
    elif operacao == '-':
        return sub
    elif operacao == '*':
        return mul
    elif operacao == '/':
        return div

op = calculadora('+')
print(op(2, 2))
print('-=-')
print(calculadora('+')(2,2))