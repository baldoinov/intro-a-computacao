# -*- coding: utf-8 -*-

'''
 * Arquivo: crivo4.py
 * ----------------
 * Este programa determina todos os primos menores que n, para um dado n.
 * Para isso, usa o metodo conhecido como o Crivo de Eratóstenes.
 *
 * O programa faz uso de um vetor a[0..n-1] que é inicializado com 1.
 * (Note que os índices 1..n-1 sao exatamente os números que desejamos 
 *  descobrir se são primos ou não.)
 * 
 * No final, as entradas desse vetor serão 0 ou 1, sendo que 
 *   a[i] = 1 indica que i é primo e
 *   a[i] = 0 indica que i não é primo.
 * 
 *
 
'''

import math

def main():
    
    n = int(input("De o valor de n (menor que 10000):  "))
    
    # inicializacao da lista a com valor 1 em todas as posicoes (nao precisa criar lista  vazia antes 
    a = [1] * (n+1)    # foi previsto o índice n 
                       # veja o segundo for quando i = 2  e n é mulitplo de 2 ==> ex: n= 100, a posicao i*j =n

    #print(" a = ", a)
    
    a[0] = a[1] = 0 # sabemos que 0 e 1 não são primos
    
    for i in range(2, n):  
        if a[i] == 1:
           # marque os múltiplos de i como não-primos 
           for j in range(2, n//i + 1):  #<================ Veja 
               a[i * j] = 0
            
               
    conta = 0 
    print("Números primos menores que %d:" %(n))           
    for i in range(2, n):
        if a[i] == 1:
            #print(i, end=',  ')
            conta += 1 

    print()
    print("total de números primos menores que %d  ====>  %d " %(n,conta))
    
#--------------
main()


'''
 ---  Você entendeu por que j começa em i? E por que zeramos as posicoes i*j?
 
 ---  O que acontece se o teste "if (a[i]) == 1" for retirado? 
 
'''

