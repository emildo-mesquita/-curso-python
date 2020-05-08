# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.

impar = int(input("Digite o valor de números impares: ")) 
contador = 0 

while contador < impar:
	print(2* contador + 1)
	contador = contador + 1
