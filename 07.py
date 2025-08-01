Faça uma função recursiva que receba um número inteiro positivo par n e imprima todos os números pares de 0 até n em ordem crescente.

def funcao(num):
    if num == 0:
        print(0)
    else:
        funcao(num-2)
        print(num)

 x = int(input(""))
funcao(x) 
