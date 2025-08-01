Faça uma função recursiva que receba um número inteiro positivo n e retorne o superfatorial desse número. Exemplo de superfatorial: sf (4) = 1! * 2! * 3! * 4! = 288.

def fatorial(num):
    if num == 0:
        f = 1
    else:    
        f = num * fatorial(num - 1)
    return f
def sf(x):
    if x == 1 or x == 0:
        sfatorial = 1
    else:    
        sfatorial = fatorial(x) * sf(x-1)
    return sfatorial    


x = int(input(""))
y = sf(x)
print(f"{y}")
