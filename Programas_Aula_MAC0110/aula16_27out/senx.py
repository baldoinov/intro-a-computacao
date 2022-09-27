# -*- coding: utf-8 -*-

"""
   arquivo: senx.py

   Dados x real e n natural, calcular uma aproximação para sen(x) 
   através dos n primeiros termos da série.
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...
    
   (Importante: Veja como cuidar da mudança de sinal dos termos.)
   (Importante: Veja como gerar um termo a partir do anterior.)

   OBS: Aproximacao é boa em torno do zero. (Usar valores < 20) 
"""
##################################################################################
#######  Solucao nao recomendada: fatorial pode ficar muito grande ##############
#################################################################################

import math  #para fazer o calculo de cos(x) usando a funcao sin(.)
             # do modulog math.  
def main():

    x = float(input("Digite o valor do ângulo x em radianos: "))
    n = int(input("Número de termos: "))
    
    soma = x
    fatorial = 1
    num = x   #<== numerador do primeiro termo 
    
    for k in range (1, n):
        num =  - (num * x * x)         #  veja o sinal 
        fatorial = fatorial * (2 * k) * (2 * k + 1);   #  calculo do fatorial aproveitando o anterior 
        soma = soma + num/fatorial 
       
    print("Aproximação usando a série dada:       sen(%g) = " %(x), soma)
    print("Usando a funcao sin(.) do módulo math: sen(%g) = " %(x), math.sin(x)) #<=== sin(x) não é sen(x)
#----
main()

"""
   numumerador num 
   ----------------
                       k = 1                      k = 2 
   num     -->   num = - num * x * x     --->   num = - num * x * x   -->

   x       -->             - x^3         --->            x^5           -->  - x^7 

   denominador fatorial
   --------------------
                          k = 1                                       k = 2            k = 3        
   fatorial ---> fatorial = fatorial * (2 * k) * (2 * k + 1)  --->  3! * 4 * 5 --->  5! * 6 * 7 
      1                               3!                                 5!             7! 

  cada termo é  num/fatorial

"""
