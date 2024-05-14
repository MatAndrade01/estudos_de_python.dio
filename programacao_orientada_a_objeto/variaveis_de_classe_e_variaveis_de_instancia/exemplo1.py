class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante('Matheus', 1)
aluno_2 = Estudante('Lucas', 2)
mostrar_valores(aluno_1, aluno_2)
print('='*20)

Estudante.escola = 'Python'#Trovando variavel de classe
aluno_1.matricula = 4 #Trovando variavel de instancia
aluno_3 = Estudante('Tiago', 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)