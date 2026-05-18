import csv
from datetime import datetime
import os, pathlib

class tarefas:

    def __init__(self):
        #self.a está fazendo dicionario vazio
        self.a = {'projeto': '', 'horario': 0}
        #self.coluna está fazendo as colunas do csv
        self.colunas = ['projeto' , 'horario']


    def texto(self):
        projeto = input('digite algo: ')
        hora = input('digite o horario: ')
        self.a['projeto'] = str(projeto)
        self.a['horario'] = int(hora)

    def mostrar_lista(self):
        print(self.a)

    def adiconar(self):
        caminho = r'C:\Users\lenno\Downloads\estudo-de-python-main\estudo-de-python-main\tarefas.csv'
        with open(caminho,'a', newline='', encoding='utf-8') as arquivo:
            escrever = csv.DictWriter(arquivo, fieldnames=self.colunas, extrasaction='ignore')
            escrever.writerow(self.a)
            #arquivo.flush()

    def ler_csv(self):
        caminho = r'C:\Users\lenno\Downloads\estudo-de-python-main\estudo-de-python-main\tarefas.csv'
        with open(caminho,'r',encoding='utf-8') as arquivo:
            ler = csv.reader(arquivo)
            for linha in ler:
                print(linha)  

lista = tarefas()

while True:
    print('menu')
    print('1: adicionar projeto e hora:')
    print('2: mostrar lista atual')
    print('3: mostrar lista completa')
    print('4: sair')
    opçao = input('selecione uma opçao: ')

    if opçao == '1':
        lista.texto()
        lista.adiconar()
    elif opçao == '2':
        lista.mostrar_lista()
    elif opçao == '3':
        lista.ler_csv()
    elif opçao == '4':
        print('saindo do arquivo')
        break
    else:
        print('erro, digite uma opçao valida')