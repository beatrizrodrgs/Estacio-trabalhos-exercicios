# 3) Agora refaça a questão 1 melhorando o
# resultado da média para imprimir o resultado final acrescente ao código:
# print(‘{0} teve media igual a: {1:4.2f}’.format(nome, media))

nomeAluno = (input ("Digite o nome do Aluno:"))
nota1 = float(input ("Digite a Primeira Nota:"))
nota2 = float(input ("Digite a Segunda Nota:"))
nota3 = float(input ("Digite a Terceira Nota:"))
mediaAluno = (nota1 + nota2 + nota3)/3
print(str(mediaAluno))

print("{0} teve media igual a: {1:4.2f}".format(nomeAluno, mediaAluno))