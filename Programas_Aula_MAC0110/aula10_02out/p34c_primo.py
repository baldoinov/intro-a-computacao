# -*- coding: utf-8 -*-
'''
   Programa p34c  ------------p34a_primo.py
   
   Dado n > 0 (inteiro positivo), testar se n é primo.
   Def: um inteiro positivo n é primo se tem exatamente dois divisores: o 1 e o próprio n.
   (1 não é primo; 2 é primo; 3 é primo; 4 não é primo; 5 é primo,...)
'''

n = int(input("Digite um número inteiro positivo (n): ")) 

print("Número dado = %d \n" %n)


if n == 1:
    is_prime = False
else
    is_prime = True   # até prova em contrário 

d = 2
while d * d <= n:    # d <= raiz quadrada de n 
    if n % d == 0:
        is_prime = False     
    d = d + 1
        
if is_prime:
    print(n, "é primo")
else:
    print(n, "não é primo")

