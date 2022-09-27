# -*- coding: utf-8 -*-

'''
   Arquivo: raiz_quadradaA.py 
   
   Dados dois números reais positivos x e eps (0 < eps < 1),
   determinar uma aproximação da raiz quadrada de x através da
   sequência de números a seguir:
       r(0) = x 
   e   r(n) = (r(n-1) + x/r(n-1))/2, para n>=1.   Ou seja,    
      
       r_atual = (r_anterior + x/r_anterior)/2 

   A aproximação será o primeiro valor r(n) para o qual |r(n)-r(n-1)| < eps.
   Imprimir o total de iterações feitas. 
   OBS:  Definir e usar uma funcao que calcula a raiz quadrada usando a sequência acima,
         e retorna também o número de iterações feitas. 

   
'''

import math  # para usar a função math.sqrt(x) e math.fabs

def main():
    print("Determina uma aproximação para a raiz quadrada de x, com precisão eps.\n")

    x = float(input("Digite um número real positivo para x: "))
    eps = float(input("Digite um número real (>0 e <1) para eps: "))
    
    raiz, n_iteracoes  = raiz_quadrada(x, eps) #<==  Veja como atribuir a variáveis os dois valores retornados pela função raiz_quadrada(.,.)
    
    print()
    print("Número de iterações feitas para ter a aproximação desejada:", n_iteracoes)
    print("Raiz quadrada aproximada de", x, " é     ", raiz)
    print("Raiz quadrada de", x, "usando math.sqrt é", math.sqrt(x))

#------------------------------------------------------------------------

def raiz_quadrada(x, eps):
    '''  (float, float) -> float, int 
         
         Recebe dois números reais positivos x e eps, com 0 < eps < 1 e
         retorna uma aproximação da raiz quadrada de x com precisão eps.
         Também retorna um valor inteiro correspondente ao número de iterações feitas.
    '''
    
    anterior = x
    atual = (x + 1) / 2
    n = 1 
    
    print("valor atual = ", atual)  # para ver o valor de r(1)
    
    while math.fabs(atual - anterior) >= eps:  #<=== Se quiséssemos comparar com o valor calculado pela funcao sqrt do Python.
        anterior = atual
        atual = (anterior + x / anterior) / 2
        n = n + 1 
        print("valor atual = ", atual)  # para ver os valores de r2, r3, ...
        
    return atual, n 

#-----------------------------------------
main()  


