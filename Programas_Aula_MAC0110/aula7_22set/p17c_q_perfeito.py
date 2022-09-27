# -*- coding: utf-8 -*-

"""
   Programa 17c --- p17c_q_perfeito.py  
   -----------------------------------

   Problema:  Dado um inteiro n > 0, este programa verifica se 
   n é q-perfeito. Dizemos que n é q-perfeito se existe k tal que 
   n é igual à soma dos seus k primeiros divisores estritamente menores que n.
 
   Compare com a definição de "perfeito". (Programa p17ab_perfeito.py)

   Todo perfeito é q-perfeito, mas nem todo q-perfeito é perfeito.g

   Exemplo1:   6 é q-perfeito, pois  6 = 1 + 2 + 3. (No caso, k=3)

   Exemplo2:  10 não é q-perfeito, pois 10 != 1 + 2  e  10 != 1 + 2 + 5 
   Exemplo3:  24 é q-perfeito, pois 24 = 1 + 2 + 3 + 4 + 6 + 8  (no caso k=6)
             (24 é q-perfeito, mas não é perfeito.)

   OBS: Testar n = 24, n= 28,  n = 496, n = 8128 e n = 8190. 

"""

def main():
    #      n:    inteiro a ser testado se é q-perfeito 
    #      d:    candidato a divisor de n
    #   soma:    soma dos divisores (menores que n)

    n = int(input("Digite o valor de n (inteiro positivo): ")) 
    soma = 0
    d = 1
    while (d <= n//2 and soma < n):  # <== VEJA! Diferença ao teste de ser "perfeito"
        if (n % d == 0):
            soma = soma + d
            print ("divisor = %4d  soma atual = %5d " %(d,soma))
        d = d + 1 
    if soma == n:
        print(n, "é q-perfeito.") 
    if soma != n:                       
        print(n, "nao é q-perfeito.")
# ---------------------------------------
main()

# ----------------------------------------------------
# OBS: Note que os candidatos a divisor ocorrem até n//2.
#
# Note que se a soma parcial ultrapassar n não há necessidade
# de continuar testando novos candidatos a divisor.
# E também temos que parar de somar outros
# possíveis divisores menores que n//2, senão
# se continuarmos somando, podemos perder o momento em que soma == n
# (que pode ocorrer com divisores menores do que n//2),
# e quando saímos do while, podemos ter soma > n, e concluir
# erradamente que n não é q-perfeito. (Por ex, veja quando n = 24.)
# Teste para n = 24 e  n = 8190 para entender bem  isso.
