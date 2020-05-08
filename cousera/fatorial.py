# Escreva um programa que receba um número natural nn na entrada e imprima n! (fatorial) na saída.

n = int(input("Digite um número natural: ")) # 5
contador = 1
fator = 1

while contador <= n:
	fator = fator * contador
	contador = contador + 1
print(fator)