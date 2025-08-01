Escreva uma função recursiva que calcule a sequência dada por: F(1) = 1; F(2) = 2; e F(n) = 2*F(n − 1) + 3*F(n − 2).

def funcao(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return 2*funcao(num-1)+3*funcao(num-2)
                                                                                                             
x = int(input(""))
y = funcao(x)
print(f"{y}")                                                                                                                                                                                         
