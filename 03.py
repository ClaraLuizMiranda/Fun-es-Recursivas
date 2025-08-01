Escreva uma função recursiva que calcule a soma dos primeiros n cubos: S(n) = 13 + 23 + … + n3.

def funcao(num):
    
    if num==1:
        return 1
    else:
        return num**3 + funcao(num-1)


x = int(input(""))
y = funcao(x)
print(f"{y}")
