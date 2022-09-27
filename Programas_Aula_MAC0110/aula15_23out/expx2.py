
# -*- coding: utf-8 -*-

"""
 Arquivo: expx2.py
-----------------   
(Outro critério de parada)

 Dado x (no. real) e epsilon (no. real bem pequeno), calcular uma aproximacao para exp(x):
                 exp (x) = 1 + x + x^2/2! + x^3/3! + ...

 Fazer a somatória enquanto a soma está mudando.
 Ou seja, quando nao fizer mais diferenca, parar a iteração.

 Calcular o valor de exp(x) usando a funcao exp() do módulo math.
 Verificar se a aproximacao obtida é boa. 

"""

import math

def main():
    x = float(input("Digite o valor de x (real positivo): "))
    termo = 1.0
    soma = 0.0
    k = 1
    
    while soma != soma + termo:
        soma = soma + termo
        termo = termo * x / k
        k = k + 1 
        print("soma parcial = ", soma)
        
    print("Valor aproximado de exp(x) = ", soma)
    print("Valor de exp(x) usando a funcao math.exp():", math.exp(x))
    print("Diferença no valor aproximado:", math.fabs(math.exp(x) - soma))

# -----
main() 


