#2) Faça um programa que preencha por leitura um vetor de 10 posições,
# e imprima no final todos os números informados pelo usuário no vetor.
vetor = []

for i in range(10):
    tmp = int(input("Entre com um número: "))
    vetor.append(tmp)

for i in vetor:
    print(vetor[i])