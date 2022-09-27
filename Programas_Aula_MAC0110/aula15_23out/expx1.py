# -*- coding: utf-8 -*-

'''
   Arquivo:  expx1.py 
   -----------------

   Dados dois números reais x e epsilon, com 0 < epsilon < 1,
   determinar uma aproximação para e^x através da seguinte série infinita:
            e^x = 1 + x + x^2/2! + x^3/3! + ... + x^k/k! + ... , 
   incluindo todo termo cujo absoluto seja maior ou igual a epsilon.
   (Ou seja, não incluir um termo cujo valor absoluto seja menor do que epsilon.)

  Este programa deve usar uma função chamada exponencial, com dois parâmetros reais, 
  x e epsilon (com  0 < epsilon < 1), que calcula uma aproximação de exp(x) com 
  precisão epsilon (cf descrito acima).

'''

import math  # para usar a função math.exp(.) <================

def main():
     print("Determina uma aproximação para e elevado a x, com precisão epsilon.\n")

     x = float(input("Digite um número real para x: "))
     epsilon = float(input("Digite um número real (>0 e <1) para epsilon: "))

     ex = exponencial(x, epsilon)  #<================================ chamada da função exponencial(.,.) 
     print("\nUma aproximacao para a exponencial de %f :" %(x), ex)
    
     print("\nExponencial de %f obtida pela função math.exp :" %(x), math.exp(x))
     print()
#------------------------------------------------------------------------------

def exponencial(x, eps):
    '''  (float, float) -> float

         Recebe dois números reais x e eps, com 0 < eps < 1 e
         retorna uma aproximação de exp(x) com precisão eps.
    '''
    
    soma = 0.0
    termo = 1.0
    k = 0
    while valor_absoluto(termo) >= eps:
        soma = soma + termo                 ## só somo se o valor absoluto do termo é >= eps
        print("termo = ", termo)
        print("soma parcial = ", soma)
        k = k + 1 
        termo = termo * x/k
        
    return soma 
   
#------------------------------------------------------------------

def valor_absoluto(x):
    '''  (float) -> float

         Recebe um número real x e retorna o módulo de x.
    '''

    if x < 0:
         return -x
    else:
         return x

#-----------------------------------------
main()  

