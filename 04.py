Crie uma função recursiva que receba dois inteiros positivos n e k e calcule n**k.

def funcao(num,exp):
    if exp==0:
        return 1
    else:
        return num* funcao(num, exp - 1)
            
