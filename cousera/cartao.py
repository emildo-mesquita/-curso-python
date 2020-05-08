
meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
cartaoEncontrado = False

while cartaoLido != 0 and not cartaoEncontrado:
	cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
	if cartaoLido == meuCartao:
		cartaoEncontrado = True

if cartaoEncontrado:
	print("EBA! Encontrei meu cartão.")
else:
	print("XII! Não ncontrei meu cartão....")

