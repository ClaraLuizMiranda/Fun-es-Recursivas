O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y. Escreva uma função recursiva mdc que retorna o máximo divisor comum de x e y. O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto da divisão.

def mdc(num1, num2):

    if num2 == 0:
        return num1
    else:
        return mdc(num2, num1 % num2)

x1 = int(input(""))
x2 = int(input(""))
y = mdc(x1, x2)
print(f"{y}")  
