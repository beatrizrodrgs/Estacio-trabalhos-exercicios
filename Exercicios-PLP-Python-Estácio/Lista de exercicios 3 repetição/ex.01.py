#1) Faça um programa para montar a tabela de multiplicação de números de 1 a 10
# (ex.: 1 x 1 = 1, 1 x 2= 2, etc.)


tabuada = int(input('Digite um número da tabuada que preferir: '))
print('-' * 15)
print('{} x {:2} = {:2}'.format(tabuada, 1, tabuada*1))
print('{} x {:2} = {:2}'.format(tabuada, 2, tabuada*2))
print('{} x {:2} = {:2}'.format(tabuada, 3, tabuada*3))
print('{} x {:2} = {:2}'.format(tabuada, 4, tabuada*4))
print('{} x {:2} = {:2}'.format(tabuada, 5, tabuada*5))
print('{} x {:2} = {:2}'.format(tabuada, 6, tabuada*6))
print('{} x {:2} = {:2}'.format(tabuada, 7, tabuada*7))
print('{} x {:2} = {:2}'.format(tabuada, 8, tabuada*8))
print('{} x {:2} = {:2}'.format(tabuada, 9, tabuada*9))
print('{} x {:2} = {:2}'.format(tabuada, 10, tabuada*10))
print('-' * 15)