# -*- coding: utf-8 -*-

"""
   arquivo: cosx_melhor.py  (compare com cosx.py) 
   ----------------------

   Dados x real e n natural, calcular uma aproximação para cos(x) 
   através dos n primeiros termos da série.
 
    cos x = 1 - x^2/2!  + x^4/4!  - x^6/6!  + ... + (-1)^k x^(2k)/ (2k)! + ...

   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========

"""

##################################################################################
#######  Solucao melhor: fatorial não é calculado explicitamente  ##############
#################################################################################

import math  #para calcular cos(x) usando a funcao cos(.) do módulo math

def main():
    x = float(input("Digite o valor do ângulo x em radianos: "))
    n = int(input("Número de termos: "))
    
    soma  = 1.0
    termo = 1.0   ## primeiro termo
    
    for k in range (1, n):
        termo =  - (termo * x * x)/((2* k - 1)*(2 * k))         #  veja o sinal 
        soma = soma  + termo

    print("Aproximação usando a série dada:       cos(%g) = " %(x), soma)
    print("Usando a funcao cos(.) do módulo math: cos(%g) = " %(x), math.cos(x)) 
    
#---------------
main()


