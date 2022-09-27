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
    print("Esse programa cálcula uma aproximação para e^x.\n")
    x = float(input("Insira um número real x: "))
    termo = 1
    soma = 0
    k = 0

    while soma != soma + termo:
        soma += termo
        k += 1
        termo = termo * (x/k)
    
    print(f"O valor aproximado de e^x usando o programa é: {soma}\n"
          f"O valor aproximado de e^x usando math.exp() é: {math.exp(x)}\n"
          f"A diferença entre eles é: {math.fabs(math.exp(x)-soma)}")


main()
