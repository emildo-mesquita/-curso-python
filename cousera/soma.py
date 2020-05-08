# Soma de sequencia de numeros
# ------------------------------------------------------------------------------------------------------

tamanho = int(input("Informe a quantidade de números a ser somados: "))
soma = 0
i = 0
while i < tamanho:
	valor = int(input("Digite um valor a ser somado: "))
	soma = soma + valor
	i = i + 1
print("A soma dos valores digitados é:", soma)