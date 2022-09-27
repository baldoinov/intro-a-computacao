# -*- coding: utf-8 -*-
'''
 Escreva um programa que recebe como entrada um inteiro positivo n, 
 e determina os coeficientes binomiais Comb(n,0), Comb(n, 1),..., Comb(n,n).  
 onde Comb(n,k)  =  n!/((n-k)!k!).

 Este programa deve usar o programa function que define as funcoes coef_bin(.,.) e fatorial(.)

'''
import function  ## no programa function.py está definida a funcao coef_bin(.,.) e fatorial(.)
                 ## Veja como chamar aqui essas funcoes.

def main():
     n = int(input("Digite um inteiro positivo (n>=0): ")) 
     k = 0
     while k <= n:
         result = function.coef_bin(n,k)                    # chamada da funcao coef_bin(.,.)
         print("Combinacao(%d,%d) = %d" %(n,k,result))
         k += 1

     print("*** Testes da funcao coef_bin(.,.) :")
     print("Combinacao(4,2) =", function.coef_bin(4,2))      # chamada da funcao coef_bin(.,.)
     print("Combinacao(5,2) =", function.coef_bin(5,2))      # chamada da funcao coef_bin(.,.)
     print("Combinacao(10,4) =", function.coef_bin(10,4))    # chamada da funcao coef_bin(.,.)

     print("**** Testes da funcao fatorial(.) :")
     print("Fatorial de 5 =", function.fatorial(5))      # chamada da funcao fatorial(.)
     print("Fatorial de 8 =", function.fatorial(8))      # chamada da funcao fatorial(.)
     print("Fatorial de 10 =", function.fatorial(10))    # chamada da funcao fatorial(.)

#--------------------------------
main()

