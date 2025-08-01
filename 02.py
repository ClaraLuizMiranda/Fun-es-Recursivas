Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro n.


import math

def funcao(num):
    if num==0:
        return 1
    else:
        return num*math.factorial(num-1)
