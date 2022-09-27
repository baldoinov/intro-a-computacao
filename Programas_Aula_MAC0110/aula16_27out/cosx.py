# -*- coding: utf-8 -*-

"""
   arquivo: cosx.py
   ---------------

   Dados x real e n natural, calcular uma aproximação para cos(x) 
   através dos n primeiros termos da série.
 
    cos x = 1 - x^2/2!  + x^4/4!  - x^6/6!  + ... + (-1)^k x^(2k)/ (2k)! + ...

   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========

"""
###################################################################################
## Solucao 1 -- nao recomendada se o numero de termos (valor de k) for muito grande
## o fatorial pode ficar muito grande e dar overflow 
###################################################################################

import math #para calcular cos(x) usando a funcao cos(.) do módulo math

def main():
    x = float(input("Digite o valor do ângulo x em radianos: "))
    n = int(input("Número de termos: "))
    
    soma = 1.0
    fatorial = 1
    num  = 1.0   ## primeiro termo
    
    for k in range (1, n):
        num =  - (num * x * x)         #  veja o sinal 
        fatorial = fatorial * (2 * k - 1) * (2 * k);   #  calculo do fatorial
                                                       # aproveitando o fatorial anterior.
        soma = soma + num/fatorial 

    print("Aproximação usando a série dada:       cos(%g) = " %(x), soma)
    print("Usando a funcao cos(.) do módulo math: cos(%g) = " %(x), math.cos(x))
    
#----
main()

"""
   numumerador num 
   ----------------
                       k = 1                      k = 2 
   num     -->   num = - num * x * x     --->   num = - num * x * x   -->

    1       -->        - x^2         --->            x^4         -->  - x^6

   denominador fatorial
   --------------------
                          k = 1                                         k = 2            k = 3        
   fatorial ---> fatorial = fatorial * (2 * k - 1) * (2 * k)  --->   2! * 3 * 4  --->  4! * 5 * 6
      1                               1 * 1 * 2                                    
                                          2!                             4!              6!
  
   cada termo é num/fatorial
  
"""
