
"""
   arquivo: senx_eps_melhor.py

   Dados x real e epsilon, com epsilon > 0,  calcular uma aproximação para sen(x) 
   através da série:
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...

   incluindo todos os termos até que  |x^(2k+1)|/(2k+1)! seja menor que epsilon.


   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========
"""
#############################################################
## solucao melhor do que senx_eps.py: não calcula fatorial explicitamente
#########################################################################

import math  # para calcular sen(x) usando a funcao sin(.) do modulo math.  
def main():

    x = float(input("Digite o valor do ângulo x em radianos: "))
    epsilon = float(input("valor de epsilon (bem pequeno):"))
    
    soma = x
    fatorial = 1.0
    termo = x   #<== numerador do primeiro termo 

    k = 1
    
    while True:
        termo =  - (termo * x * x) / ((2 * k) * (2 * k + 1))      #  veja o sinal 
        print("termo =", termo)
        if math.fabs(termo) < epsilon:
            break
        soma = soma + termo
        k = k + 1
       
    print("Aproximação usando a série dada:       sen(%g) = " %(x), soma)
    print("Usando a funcao sin(.) do módulo math: sen(%g) = " %(x), math.sin(x))
    
#----
main()

"""
   Geracao dos termos da sequência:

                            k = 1                                k = 2
   termo    -->   termo = - (termo * x * x)/(2*3)  --->  termo = - (termo * x * x)/(4* 5)    -->

   x       -->                   - x^3/3!          --->                x^5/5!               -->  



   denominador fatorial

                                  k = 1                                 k = 2 
   fatorial   ---> fatorial = fatorial * (2 * k) * (2 * k + 1)  --->   .........
      1 

"""
