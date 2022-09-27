
"""
   arquivo: senx.py

   Dados x real e epsilon, com epsilon > 0,  calcular uma aproximação para sen(x) 
   através da série:
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...

   incluindo todos os termos até que  |x^(2k+1)|/(2k+1)! seja menor que epsilon.


   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========
"""
##################################################################################
#######  Solucao nao recomendada: fatorial pode ficar muito grande ##############
#################################################################################


import math # para calcular sen(x) usando a funcao sin(.) do modulo math.  

def main():

    x = float(input("Digite o valor do ângulo x em radianos: "))
    epsilon = float(input("valor de epsilon (bem pequeno):"))
    
    soma = x
    fatorial = 1.0
    num = x   #<== numerador do primeiro termo 

    k = 1
    
    while True:
        num =  - (num * x * x)         #  veja o sinal 
        fatorial = fatorial * (2 * k) * (2 * k + 1);   #  calculo do fatorial aproveitando o fatorial anterior
        k = k+ 1
        print("num=", num)
        print("fatorial = %e"  %(fatorial))

        termo = num/fatorial
        print("termo =", termo)
        termo_abs = math.fabs(termo)
        if termo_abs < epsilon:
            break
        
        soma = soma + termo 
        print("sen(x) =", soma)
       
    print("Aproximação usando a série dada:       sen(%g) = " %(x), soma)
    print("Usando a funcao sin(.) do módulo math: sen(%g) = " %(x), math.sin(x))
    
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
