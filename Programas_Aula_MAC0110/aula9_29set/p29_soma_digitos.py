# -*- coding: utf-8 -*-
'''
  ---- Manipulação de digitos de um número --------
  -------------------------------------------------
  Programa P29 
  ------------
  Dados um inteiro n > 0  
  determinar a soma dos digitos de n.

'''

n = int(input("Digite o valor de n: "))
n_copia = n
    
soma = 0
    
while n > 0:
    dig = n % 10
    print("digito = ", dig)
    soma = soma + dig
    n = n // 10
    
print("A soma dos digitos de", n_copia, "é igual a", soma)
#--------------------------
         
