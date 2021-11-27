# 5) Faça um programa que leia 2 notas de um aluno da ESTACIO,
# calcule a média e imprima aprovado, reprovado ou recuperação
# (para ser aprovado a média deve ser no mínimo 7).

print("Aluno ESTÁCIO, insira suas 2 notas a seguir!")
nota1 = float(input ("Digite a Primeira Nota:"))
nota2 = float(input ("Digite a Segunda Nota:"))

mediaAluno = (nota1 + nota2)/2
print("A sua média é:" , mediaAluno)

if mediaAluno <7.0 :
    print("Tente novamente na RECUPERAÇÃO!!")
elif mediaAluno > 7.0 :
    print("100% APROVADO!!")