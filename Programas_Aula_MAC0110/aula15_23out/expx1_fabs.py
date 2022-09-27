
'''
   Arquivo:  expx1_fabs.py
   
   (Correspondente a expx1.py, porém usando a funçao fabs (valor absoluto do módulo math.)

   Dados dois números reais x e epsilon, com 0 < epsilon < 1,
   determinar uma aproximação para e^x através da seguinte série infinita:
            e^x = 1 + x + x^2/2! + x^3/3! + ... + x^k/k! +... ,
   incluindo todo termo cujo valor absoluto seja  maior ou igual a epsilon.
   (Ou seja, não incluir um termo cujo valor absoluto seja menor do que epsilon.)
'''


import math  # para usar a função math.exp(x) e math.fabs()

def main():
     print("Determina uma aproximação para e elevado a x, com precisão epsilon.\n")

     x = float(input("Digite um número real para x: "))
     epsilon = float(input("Digite um número real (>0 e <1) para epsilon: "))

     ex = exponencial(x, epsilon)
     print("\nUma aproximacao para a exponencial de %f :" %(x), ex)
    
     print("\nExponencial de %f obtida pela função math.exp :" %(x), math.exp(x))
     print()
#------------------------------------------------------------------------------

def exponencial(x, eps):
    '''  (float, float) -> float

         Recebe dois números reais x e eps, com 0 < eps < 1 e
         retorna uma aproximação de exp(x) com precisão eps.
    '''

    ex = 0.0
    termo = 1.0
    k = 0
    while math.fabs(termo) >= eps: 
        ex = ex + termo        
        print("termo = ", termo)
        print("soma parcial = ", ex)
        k = k + 1 
        termo = termo * x/k          
    return ex

#-----------------------------------------
main()  

