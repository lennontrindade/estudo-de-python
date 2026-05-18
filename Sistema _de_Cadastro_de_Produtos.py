class adicionar_lista:
    def __init__(self):
        self.adicionar_carro = {}

    def adcionar(self):
        modelo = input("marca: ")
        valor = input("valor: ")
        self.adicionar_carro.update({str (modelo) : int (valor)})


    def ver_lista(self):
        print(self.adicionar_carro)

lista = adicionar_lista()
# lista.adcionar()
# lista.ver_lista()

#menu de opçoes
while True:
    print("menu")
    print('1: adiconar produto')
    print('2: ver lista')
    print("3: sair")

    opçoes = input('escolha uma opçao: ')

    if opçoes == "1":
        lista.adcionar()
    elif opçoes == "2":
        lista.ver_lista()
    elif opçoes == "3":
        print("saindo")
        break
    else:
        print('deu erro')



