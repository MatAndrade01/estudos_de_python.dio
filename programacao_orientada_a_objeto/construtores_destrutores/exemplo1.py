class Cachorro:
    def __init__(self, nome, cor, acordado = True):
        print('Inicianliando a classe!')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print('Removendo a instancia da Classe.')

    def falar(self):
        print('Au au')

def criar_cachorro():
    c = Cachorro('Zeus', 'Preto', False)
    print(c.nome)

c = Cachorro('Lily', 'Preta com Branca')
c.falar()

print('Ola Mundo!!')

del c

print('Ola Mundo!!')
print('Ola Mundo!!')
print('Ola Mundo!!')

#criar_cachorro()