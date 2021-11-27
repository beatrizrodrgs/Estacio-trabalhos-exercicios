#Faça um programa que receba 4 notas de um aluno, imprima as notas informadas
#e calcule a média das 4 notas.

notas = []
somaNotas = 0
qtdNotas = 1

for i in range(4):
    tmp = float(input("Entre com a {}ª nota: ".format(i+1)))
    notas.append(tmp)
    somaNotas += notas[i]

for i in notas:
    print("{0}ª nota: {1}".format(qtdNotas, i))
    qtdNotas += 1

media = somaNotas / 4.0

print("A média é: {}".format(media))