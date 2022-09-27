# -*- coding: utf-8 -*-

"""
   Programa 17a --- P17a_perfeito.py
   ---------------------
   Problema:  Dado um inteiro n > 0, este programa verifica se 
   n é perfeito. Dizemos que n é perfeito se n é igual  
   à soma dos seus divisores estritamente menores que n.
 
   Exemplo1:   6 é perfeito, pois  6 = 1 + 2 + 3. 
   Exemplo2:  10 não é q-perfeito pois 10 !=  1 + 2 + 5
   OBS:  !=   operador (de comparação) "diferente" em Python 
   
   Testar n = 24, n= 28,  n = 496, n = 8190
  
"""
def main():
    #      n:    inteiro a ser testado se é perfeito 
    #      d:    candidato a divisor de n
    #   soma:    soma dos divisores (menores que n)

    n = int(input("Digite o valor de n (inteiro positivo): ")) 
    soma = 0
    d = 1
    while d < n:    # <==== bastaria testar até n//2  (veja abaixo)
        if (n % d == 0):
            soma = soma + d
            print ("divisor = %4d  soma atual = %5d " %(d,soma))
        d = d + 1 
    if soma == n:
        print(n, "é perfeito.") 
    if soma!= n:
        print(n, "não é perfeito.")
# ---------------------------------------
main()

"""
OUTRA SOLUÇÃO (testando candidatos a divisor até  n//2)

Programa 17b --- P17b_perfeito.py


def main():
    #      n:    inteiro a ser testado se é perfeito 
    #      d:    candidato a divisor de n
    #   soma:    soma dos divisores (menores que n)

    n = int(input("Digite o valor de n (inteiro positivo): ")) 
    soma = 0
    d = 1
    while d < n//2:  # <====  depois de n//2 não há divisores próprios de n 
        if (n % d == 0):
            soma = soma + d
            print ("divisor = %4d  soma atual = %5d " %(d,soma))
        d = d + 1 
    if soma == n:
        print(n, "é perfeito.") 
    if soma!= n:
        print(n, "não é perfeito.")
# ---------------------------------------
main()

"""
