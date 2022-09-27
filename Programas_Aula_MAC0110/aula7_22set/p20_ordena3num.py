# -*- coding: utf-8 -*-

""" Programa 20  -- p20_ordena3num.py
     -------------------
    Problema: dados 3 números inteiros, imprimi-los em ordem
    crescente.  (com um único comando print.)
    ------------------
    Queremos que no final os numeros dados fiquem em x, y, z,
    e que tenhamos  x <= y <= z
"""
print("Vamos ordenar 3 números em ordem crescente.")

x = int(input("Digite o primeiro número:"))
y = int(input("Digite  o segundo número:"))
z = int(input("Digite o terceiro número:"))
     
if x > y:
    aux = x    
    x = y      
    y = aux 
  
######  agora temos x <= y 

if x > z:
    aux = x
    x = z   
    z = aux

######  agora temos  x <= y  e  x <= z 

if y > z:
    aux = y
    y = z
    z = aux
  
#####  agora temos  x <= y <= z 

print("Temos %d <= %d <= %d.\n" %(x, y, z))

######################################################
#
#      x  |    y   |    z         aux 
#    -----|--------|--------     -----
#     20  |   11   |   5          20
#     11  |   20   |  11       
#      5  |   11   |  20
#         |        |
#------------------------------------------

