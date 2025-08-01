Crie uma função recursiva que receba um número inteiro positivo n e calcule o somatório dos números de 1 até n.

def funcao(num):
    if num==1:
        return 1
    else:
        return num + funcao(num-1)

x = int(input(""))
y = funcao(x)
print(f"{y}")
