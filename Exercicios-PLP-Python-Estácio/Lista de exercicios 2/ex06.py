# 6) Refaça o exercício 2, identificando o conceito aprovado (média superior a 7),
# exame (média 7 e 8) ou reprovado (média inferior a 5).
# (Acredito que tenha acontecido uma falha na digitação da referência a qual questão deveria ser refeita.)

nomeAluno = (input ("Digite o nome do Aluno:"))
nota1 = float(input ("Digite a Primeira Nota:"))
nota2 = float(input ("Digite a Segunda Nota:"))
nota3 = float(input ("Digite a Terceira Nota:"))
mediaAluno = (nota1 + nota2 + nota3)/3
print(str(mediaAluno))

if mediaAluno >= 7.0 :
    print("APROVADO!!")

elif mediaAluno <=5.0 :
    print("REPROVADO!!")