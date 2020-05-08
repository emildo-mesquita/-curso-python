#desafiosoma

i = int(input("Digite um número: ")) # 150
x = i
soma = 0

while i != 0:
	resto = i % 10
	i = (i - resto) // 10
	soma = soma + resto
print ("A soma do número digitado",x, "é:",soma)

