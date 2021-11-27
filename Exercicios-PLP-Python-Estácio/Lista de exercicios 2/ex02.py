#2) Faça um programa para calcular a idade de uma pessoa. O programa deve receber:
# o nome da pessoa, o ano de nascimento da pessoa e o ano atual pela função input();
# e no final deve imprimir a idade da pessoa

nomePessoa = (input ("Digite o Nome:"))
anoNascimento = float(input ("Digite o Ano de Nascimento:"))
anoAtual = float(input ("Digite o Ano Atual:"))

idadeAtual = (anoAtual - anoNascimento)
print(int(idadeAtual))