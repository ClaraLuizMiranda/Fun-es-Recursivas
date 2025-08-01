Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem decrescente.

  def funcao(num):
    print(num)
    
    if num == 0:
        return
    else:
        funcao(num-1)

x = int(input(""))
funcao(x)
