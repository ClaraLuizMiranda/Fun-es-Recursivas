Implemente a função A definida recursivamente por: A(m, n) = n + 1, se m = 0; A(m, n) = A(m − 1, 1), se m > 0 e n = 0; A(m, n) = A(m − 1, A(m, n − 1)) , se m > 0 e n > 0.

def A(m, n):
    
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))

x1 = int(input(""))
x2 = int(input(""))
y = A(x1, x2)
print(f"{y}")  
