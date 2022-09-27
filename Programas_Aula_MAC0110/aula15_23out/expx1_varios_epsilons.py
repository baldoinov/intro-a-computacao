'''
   Dados dois números reasis  x e epsilon, com 0 < epsilon < 1,
   determinar uma epsilon-aproximação para e^x através da seguinte série infinita:
            e^x = 1 + x + x^2/2! + x^3/3! + ... + x^k/k! +... ,
   incluindo todos os termos cujo valores absolutos sejam  maiores ou iguais a epsilon.
   (Não incluir termo com valor absoluto menor do que epsilon.)
  
   Adicionalmente a essa epsilon-aproximação (para esse epsilon dado),
   calcular alfa-aproximações, onde alfa toma valores 
   epsilon/(10)^i, onde i=1,...,5

   
'''
import math  # para usar a função math.exp(x)

def main():
     print("Determina uma aproximação para exp(x), com precisão epsilon.\n")

     x = float(input(" Digite um número real para x: "))
     epsilon = float(input(" Digite um número real (>0 e <1) para epsilon: "))

    
     ex = exponencial(x, epsilon)   #<================================================= 1a. chamada da funcao
     
     print(" Aproximacao para a exp(%f) com epsilon = %e ====> " %(x, epsilon), ex)
    
     print(" Valor de exp(%f) obtida pela função math.exp :" %(x), math.exp(x))
     print(" Diferença (valor absoluto) no valor aproximado:", math.fabs(math.exp(x) - ex))
     print("-----------------")
     print(" Outras aproximações de exp(%f)  com epsilons variados:" %(x))

     alfa = epsilon
    
     for i in range(1, 6):
         alfa = epsilon / (10 ** i)  
         ex = exponencial(x, alfa)
        
         print("\n Aproximacao para exp(%f) com epsilon = %e ====> " %(x, alfa), ex)
         print(" Diferença no valor aproximado:", math.exp(x) - ex)
         
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
    while math.fabs(termo) >= eps:    #<================ math.fabs
        soma = soma + termo
        k = k + 1
        termo = termo * x/k   
            
    return soma

#------------------------------------------------------------------
main()  

