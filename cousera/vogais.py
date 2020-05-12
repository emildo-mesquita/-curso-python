# Exercício 3 - Vogais
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

def vogal(x):
	vog = True
	if x == 'a' or x == 'A':
		return vog
	
	if x == 'e' or x == 'E':
		return vog
	
	if x == 'i' or x == 'I':
		return vog
	
	if x == 'o' or x == 'O':
		return vog
	
	if x == 'u' or x == 'U':
		return vog
	else:
		return not vog

	
