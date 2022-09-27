
"""
   arquivo: senx.py

   Dados x real e epsilon, com epsilon > 0,  calcular uma aproximação para sen(x) 
   através da série:
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...

   incluindo todos os termos até que  |x^(2k+1)|/(2k+1)! seja menor que epsilon.


   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========
"""


import math  #para fazer o calculo de cos(x) usando a funcao cos(.)
             # do modulog math.  
def main():

    x = float(input("Digite o valor do ângulo x em radianos: "))
    epsilon = float(input("valor de epsilon (bem pequeno):"))
    
    senx = x
    fatorial = 1.0
    num = x   #<== numerador do primeiro termo 

    k = 1
    
    while True:
        num =  - (num * x * x)         #  veja o sinal 
        fatorial = fatorial * (2 * k) * (2 * k + 1);   #  calculo do fatorial aproveitando o fatorial anterior
        k = k+ 1
        print("num=", num)
        print("fatorial =", fatorial)
        
        termo = math.fabs(num)/fatorial
        print("termo=", termo)
        
        if termo < epsilon:
            break
        
        senx = senx + num/fatorial
        print("sen(x) =", senx)
       
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
