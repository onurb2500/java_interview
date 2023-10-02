def posicaoFibonacciLinear(n) :
    a, b = 0, 1 
    for _ in range(n):
        a, b = b, a + b
    return a

def posicaoFibonacciRecursiva(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return posicaoFibonacciRecursiva(n-1) + posicaoFibonacciRecursiva(n-2)

n = int(input())

if n >= 0:
    print(posicaoFibonacciLinear(n))
    print(posicaoFibonacciRecursiva(n))
else:
    print('Invalid number')
