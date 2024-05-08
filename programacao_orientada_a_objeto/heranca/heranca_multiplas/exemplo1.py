class Animal:
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_do_pelo, **kwargs):
        self.cor_do_pelo = cor_do_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_do_bico, **kwargs):
        self.cor_do_bico = cor_do_bico
        super().__init__(**kwargs)

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_do_bico, cor_do_pelo, numero_de_patas):
        # Chama super() respeitando a ordem de herança
        super(Mamifero, self).__init__(cor_do_pelo=cor_do_pelo, numero_de_patas=numero_de_patas)
        super(Ave, self).__init__(cor_do_bico=cor_do_bico, numero_de_patas=numero_de_patas)

gato = Gato(numero_de_patas=4, cor_do_pelo='Preto')
print(gato)

ornitorrinco = Ornitorrinco(numero_de_patas=2, cor_do_pelo='Vermelho', cor_do_bico='Laranja')
print(ornitorrinco)
