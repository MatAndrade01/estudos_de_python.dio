class Veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(selft):
        print('Ligando o Motor!!')

    def __str__(self):
         return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(selft, cor, placa, numero_de_rodas, carregado):
        super().__init__(cor,placa, numero_de_rodas)
        selft.carregado = carregado

    def esta_carregado(selft):
        print(f'{'Sim' if selft.carregado else 'Nao'} estou carregado')

moto = Motocicleta('Preta', 'ABC-1234', 2)
carro = Carro('Rosa', 'ABC-3456', 4)
caminhao = Caminhao('Vermelho', 'ABC-8954', 8, False)

print(moto)
print(carro)
print(caminhao)