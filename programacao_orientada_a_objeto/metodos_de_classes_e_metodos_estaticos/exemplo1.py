class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa('Matheus', 21)
#print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(2002, 10, 14, 'Matheus')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))