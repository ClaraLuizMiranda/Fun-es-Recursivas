Escreva uma função recursiva SomaSerie(i,j,k). Esta função devolve a soma da série de valores no intervalo [i,j], com incremento k.


 def SomaSerie(num1,num2,num3):
    if num1>num2:
        return 0
    else:
        return num1+SomaSerie(num1+num3,num2,num3)

x1 = int(input(""))
x2 = int(input(""))
x3 = int(input(""))
y = SomaSerie(x1, x2, x3)
print(f"{y}")
