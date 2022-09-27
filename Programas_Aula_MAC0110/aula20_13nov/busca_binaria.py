# -*- coding: utf-8 -*-

'''
 * arquivo: busca_binaria.py
 * ------------------------
 * Este programa recebe uma sequência crescente de n inteiros
 * e um inteiro x.  Determina se x ocorre na sequência dada.
 
'''

def main():
     n = int(input("Forneca o valor de n: "))
     v = []
     for i in range(n):
         num = int(input("\nDigite um elemento da sequencia:"))
         v.append(num)

     print("\nSequencia dada: v =", v)

     x = int(input("\nDigite o elemento a ser procurado: "))
     print("\nElemento procurado = ", x)
     
     esq = 0
     dir = n-1
     achou = False   # supomos que x nao ocorre na lista v
                     # achou vai mudar so'se x for encontrado na lista v
     while dir >= esq:
         meio = (esq + dir) // 2
         if x == v[meio]:      #     -------------------------------------------------
             achou = True      # v =  2   5   8   12   15    20     25   40    50   56
             break             #     -------------------------------------------------
         if x < v[meio]:       #      0   1   2   3    4     5      6    7     8    9
             dir = meio - 1           
                                       
         else:                              
             esq = meio + 1     
                                           
     print()
     if achou:
         print("O elemento %d ocorre na sequencia." %(x))
     else:
         print("O elemento %d nao ocorre na sequencia." %(x))
#--------------------------------------
main()
