import math

def eh_primo(n):
    if n == 1 or (n % 2 == 0 and n != 2):
        eh_primo = False
    else:
        eh_primo = True
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                eh_primo = False
                break
    return eh_primo

def retornaPrimoLinear(n):
    primos = [i for i in range(n+1) if eh_primo(i)]
    return primos

def retornaPrimoRecursiva(n, contadorPrimo=2, primos=[]):
    if contadorPrimo <= n:
        if eh_primo(contadorPrimo):
            primos.append(contadorPrimo)
        retornaPrimoRecursiva(n, contadorPrimo + 1, primos)
    return primos

n = int(input())

if n > 1:
    print(retornaPrimoLinear(n))
    print(retornaPrimoRecursiva(n))
else:
    print('Invalid number')