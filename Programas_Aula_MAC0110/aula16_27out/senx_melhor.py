# -*- coding: utf-8 -*-

"""
   arquivo: senx_melhor.py   (Comparar com senx.py)

   Dados x real e n natural, calcular uma aproximação para sen(x) 
   através dos n primeiros termos da série.
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...
    
   (Importante: Veja como cuidar da mudança de sinal dos termos.)
   (Importante: Veja como gerar um termo a partir do anterior.)

   OBS: Aproximacao é boa em torno do zero.  (Usar valores < 20) 
"""
##################################################################################
####### Solucao melhor do que senx.py (não calcular o fatorial para cada termo)
#################################################################################

import math  #para fazer o calculo de cos(x) usando a funcao sin(.)
             # do modulo math.  
def main():

    x = float(input("Digite o valor do ângulo x em radianos: "))
    n = int(input("Número de termos: "))
    
    soma  = x
    termo = x   # primeiro termo 
    
    for k in range (1, n):
        termo  =  - (termo * x * x) /((2 * k)*(2 * k + 1))      #  veja o sinal
        print("termo =", termo) 
        soma = soma + termo 
       
    print("Aproximação usando a série dada:       sen(%g) = " %(x), soma)
    print("Usando a funcao sin(.) do módulo math: sen(%g) = " %(x), math.sin(x))
#----
main()

"""
  Cálculo dos termos da somatória 
                                   k = 1                           k = 2 
  termo     -->   termo = - termo * x * x / (2* 3) --->   termo  = - termo * x * x / (4*5)  -->

   x         -->                  - x^3 /3!        --->                  x^5/5!             -->  


"""
