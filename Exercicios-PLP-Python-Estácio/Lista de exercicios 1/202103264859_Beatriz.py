#) Calcule de cabeça as seguintes expressões numéricas e depois use a janela do active code (Python Console) para verificar as suas respostas:
print(5**2)      #5^2 = 25
25
print(9*5)       #9x5 = 45
45
print(15/12)     #15/12 = 1,25
1.25
print(12/15)     #12/15 = 0,8
0.8
print(5//12)     #5/12 = 0,41 porém na divisao inteira ele trunca o resultado para o menor inteiro a esqueda da linha real. Sendo assim o resultado é 0.
0
print(12//15)    #12/15 = 0,80 porém na divisao inteira ele truca o resultado para o menor inteiro a esqueda da linha real. Sendo assim o resultado é 0.
0
print(5%2)       #5/2 = 2 (resto 1)
1
print(9%5)       #9/4 = 4 (resto 4)
4
print(15%12)     #15/12 = 1 (resto 3)
3
print(12%15)     #12/15 = 0,8 (resto 12)
12
print(6%6)       #6/6 = 1 (resto 0)
0
print(0%7)       #0%7 = 0 (resto 0)
0


# Você olha para um relógio e são exatamente 2 da tarde. Você coloca um alarme para tocar daqui a 51 horas. A que horas o alarme irá tocar?
horaAtual = 2
tempoEspera = 51
horasDia = 24
print(tempoEspera%horasDia + horaAtual)
5

#Considere a sentença: Só trabalho sem diversão faz de João um chato. Armazene cada palavra em uma variável, então imprima a sentença em uma linha usando a função print
palavra1 = "Só"
palavra2 = "trabalho"
palavra3 = "sem"
palavra4 = "diversão"
palavra5 = "faz"
palavra6 = "de"
palavra7 = "João"
palavra8 = "um"
palavra9 = "chato."
print(palavra1, palavra2, palavra3, palavra4, palavra5, palavra6, palavra7, palavra8, palavra9)

#Acrescente parênteses à expressão 6 * 1 - 2 para mudar o seu valor de 4 para -6.
print(6*(1-2))
-6


#Escreva um programa que converta uma temperatura de graus Celsius para Fahrenheit.

celsius = float(input("Digite a temperatura em ºC:"))
fahrenheit = 9 * celsius / 5 + 32
print("A temperatura de {} ºC corresponde a {} ºF.".format(celsius, fahrenheit))


# Escreva um programa que converta uma temperatura de Farenheit para graus Celsius.
fahrenheit = float(input("Digite a temperatura em ºF:"))

celsius = 32 - fahrenheit * 5 / 9
print("A temperatura de {} ºF corresponde a {} ºC.".format(fahrenheit, celsius))