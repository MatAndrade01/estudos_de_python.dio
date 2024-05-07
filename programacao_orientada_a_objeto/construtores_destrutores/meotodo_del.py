class Cachorro:
    def __del__(self):
        print('Destruindo a Instancia')

c = Cachorro()
del c