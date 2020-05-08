# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
# Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

    # leia o valor de n
    n=int(input("Digite o valor de n (n > 0): "))

    # n é primo até que se prove o contrário
    if n == 2 or (n != 1 and n % 2 == 1): # 2 é primo , 1 não é primo
        primo = True
    else:
        primo = False  # pares maiores que 2 não são primos
