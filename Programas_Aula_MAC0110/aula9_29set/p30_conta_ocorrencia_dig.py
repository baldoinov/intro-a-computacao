# -*- coding: utf-8 -*-
'''
  ---- Manipulação de digitos de um número --------
  -------------------------------------------------
  Programa P30 
  ------------
  Dados um inteiro n > 0  e um digito d (0<=d<=9)
  determinar quantas vezes d ocorre em n.

'''

n = int(input("Digite o valor de n: "))
d = int(input("Digite o digito d:  "))
n_copia = n
    
conta = 0 
while n > 0:
    dig = n % 10
    if dig == d:
        conta = conta + 1
    n = n // 10
    
print("O digito %d ocorre %d vezes em %d" %(d,conta,n_copia))
#-------------------

         
