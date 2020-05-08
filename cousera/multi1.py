tabuada = int(input("Qual tabuada você quer que eu resolva?")) # 2
limite = int(input("Quantas vezes será a multiplicação?")) # 3
contador = 0

while contador <= limite:
	resultado = tabuada * contador
	print("A tabuada de " ,tabuada," x ", contador, "é: " ,resultado)
	contador = contador+1


