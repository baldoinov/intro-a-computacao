'''
   Dados dois números reasis  x e epsilon, com 0 < epsilon < 1,
   determinar uma epsilon-aproximação para e^x através da seguinte série infinita:
            e^x = 1 + x + x^2/2! + x^3/3! + ... + x^k/k! +... ,
   incluindo todo termo cujo valor absoluto seja maior ou igual a epsilon.
  
   Adicionalmente a essa epsilon-aproximação (para esse epsilon dado),
   calcular alfa-aproximações, onde alfa toma valores 
   epsilon/(10)^i, onde i=1,..., 5. Ou seja, fazer para 
   alfa=epsilon/10, alfa = epsilon/10^2,..., alfa = epsilon/10^5.
   
'''
import math  # para usar a função math.exp(x)

def main():
     print("Determina uma aproximação para exp(x), com precisão epsilon.\n")

     x = float(input(" Digite um número real para x: "))
     epsilon = float(input(" Digite um número real (>0 e <1) para epsilon: "))

    
     
     ex, ultimok = exponencial (x, epsilon) 
     
     print("\n Aproximacao para exp(%f) com epsilon = %e ====> " %(x, epsilon), ex)
     print(" Último valor de k =", ultimok)
     print(" Valor de exp(%f) obtida pela função math.exp :" %(x), math.exp(x))
     print(" Diferença (valor absoluto) em relação a math.exp:", math.fabs(math.exp(x) - ex))
     
     print("\n Outras aproximações de exp(%f) com epsilons variados:" %(x))

     alfa = epsilon
    
     for i in range(1, 6):
         alfa = epsilon / (10 ** i)  
         ex, ultimok = exponencial(x, alfa) #<============================================ Vejam 
         
         print("\n Aproximacao para exp(%f) com epsilon = %e ====> " %(x, alfa), ex)
         print(" Último valor de k =", ultimok)
         print(" Diferença (valor absoluto) em relação a math.exp:", math.exp(x) - ex)
         print("---------------")
         
     print()

     
#------------------------------------------------------------------------------

def exponencial(x, eps):
    '''  (float, float) -> float, int   <================== Devolve dois valores!

         Recebe dois números reais x e eps, com 0 < eps < 1 e
         retorna uma aproximação de exp(x) com precisão eps, e
         retorna qual o último valor de k que foi ultizado na soma. 
    '''

    soma = 0.0
    termo = 1.0
    k = 0 
    while math.fabs(termo) >= eps:    #<================ math.fabs
        soma = soma + termo
        k = k + 1
        termo = termo * x/k   # termo *= x / k
        print(" soma parcial = ", soma)
     
    return soma, k-1

#------------------------------------------------------------------
main()  

