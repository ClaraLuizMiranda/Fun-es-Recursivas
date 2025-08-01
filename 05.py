Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem crescente.

  def funcao(num):
    if num==0:
        print(0)
    else:
        funcao(num-1)
        print(num)


x = int(input(""))
funcao(x)
