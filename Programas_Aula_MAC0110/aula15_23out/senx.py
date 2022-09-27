# -*- coding: utf-8 -*-

"""
   arquivo: senx.py

   Dados x real e n natural, calcular uma aproximação para sen(x) 
   através dos n primeiros termos da série.
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...
    
   (Importante: Veja como cuidar da mudança de sinal dos termos.)
   (Importante: Veja como gerar um termo a partir do anterior.)

   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========
"""

import math  #para fazer o calculo de cos(x) usando a funcao sin(.)
             # do modulog math.  
def main():

    x = float(input("Digite o valor do ângulo x em radianos: "))
    n = int(input("Número de termos: "))
    
    senx = x
    fatorial = 1
    num = x   #<== numerador do primeiro termo 
    
    for k in range (1, n):
        num =  - (num * x * x)         #  veja o sinal 
        fatorial = fatorial * (2 * k) * (2 * k + 1);   #  calculo do fatorial
                                                    # aproveitando o fatorial anterior.
        senx = senx + num/fatorial 
       
    print("sen(%g) = %g\n" %(x, senx))
    
    seno = math.sin(x)
    print("Usando a funcao sin(.) disponivel no módulo math:  sen(%g) = %g\n" %(x, seno))
#----
main()

"""
   numumerador num 

   num     -->   num = - num * x * x  --->   num = - num * x * x   -->

   x       -->          - x^3         --->            x^5           -->  - x^7 



   denominador fatorial

                                  k = 1                                 k = 2 
   fatorial   ---> fatorial = fatorial * (2 * k) * (2 * k + 1)  --->   .........
      1 

"""
