 # leia o valor de n
n = int(input("Digite um número inteiro: "))

    # n é primo até que se prove o contrário
numPrimo = True

    # procure por um divisor de n entre 2 e n-1
divisor = 2
while divisor < n and numPrimo: # equivalente a "div... and é_primo == True:"
    if n % divisor == 0:
    	numPrimo = False
    divisor += 1
  
    
if numPrimo and n != 1: # 1 não é primo
    print("primo")
else:
    print("não primo")








