EXERCICIOS DE PYTHON

1. Cálculo de Média (Controle de Fluxo)
Este é o clássico exemplo de como o computador toma decisões.

float(input(...)): O input sempre recebe texto. O float transforma esse texto em um número decimal para que você consiga fazer contas matemáticas.

aluno_nota / 3: Processamento de dados simples para chegar à média.

if / elif / else: É o caminho da decisão. O elif (else if) é importante porque ele só é testado se o primeiro if for falso, economizando processamento.

str(aluno_nota1): Você converte o número de volta para texto para poder "colar" (concatenar) com a frase do print.

2. Filtro de Primos (Algoritmo e Listas)
Aqui você usou uma lógica matemática mais avançada.

def numeros_primos(n): Cria uma função reutilizável.

n0.5: Esta é a sacada de mestre. Em vez de testar todos os números, você testa até a raiz quadrada. Matematicamente, se ele não tiver divisores até ali, ele é primo. Isso torna o código muito mais rápido.

[num for num in numeros if...]: Isso é uma "Lista Compreensiva". É como se você desse um filtro para o Python: "Gere uma lista nova, mas só coloque o num se ele passar no teste da função de primos".

3. Manipulação de JSON (Persistência de Dados)
Essencial para salvar o que o seu programa faz.

import json: Traz ferramentas prontas para lidar com esse formato, que é o padrão da web hoje em dia.

with open(..., 'r'): O with é um gerenciador de contexto. Ele abre o arquivo e, o mais importante, fecha sozinho quando termina, mesmo se der erro. O 'r' significa read (leitura).

readlines(): Pega o arquivo inteiro e transforma cada linha em um item de uma lista.

json.dump(..., indent=4): Transforma os dados do Python em um arquivo JSON bonitinho e organizado (o indent cria aqueles espaços no início das linhas para facilitar a leitura humana).