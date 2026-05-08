nota = float(input("nota em matematica: "))
nota1 = float(input("nota em ciencias: "))
nota2 = float(input("nota em portugues: "))

aluno_nota = nota + nota1 + nota2
aluno_nota1 = aluno_nota / 3

if aluno_nota1 >= 7:
    print("aprovado " + str(aluno_nota1))
elif aluno_nota1 >= 5:
    print("recuperaçao " + str(aluno_nota1))
else:
    print("reprovado " + str(aluno_nota1))


