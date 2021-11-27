# Faça um programa que receba como entrada dois números e retorne o maior deles.
# Caso os números sejam iguais, retorne “Os números são iguais”.

print("Insira 2 números inteiros!")
numero1 = float(input ("Digite o Primeiro Número:"))
numero2 = float(input ("Digite o Segundo Número:"))

if numero1 > numero2 :
    print(int(numero1))

elif numero1 < numero2 :
    print(int(numero2))

elif numero1 == numero2:
    print("Os números são iguais!")