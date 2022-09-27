"""
   Arquivo:  expx1_fabs.py
   
   (Correspondente a expx1.py, porém usando a funçao fabs (valor absoluto do módulo math.)

   Dados dois números reais x e epsilon, com 0 < epsilon < 1,
   determinar uma aproximação para e^x através da seguinte série infinita:
            e^x = 1 + x + x^2/2! + x^3/3! + ... + x^k/k! +... ,
   incluindo todo termo cujo valor absoluto seja  maior ou igual a epsilon.
   (Ou seja, não incluir um termo cujo valor absoluto seja menor do que epsilon.)
"""
import math


def main():
    print("Esse programa cálcula uma aproximação para e^x com precisão epsilon.\n")
    x = float(input("Insira x: "))
    epsilon = float(input("Insira epsilon (0 < epsilon < 1): "))
    
    ex = exponencial(x, epsilon)
    print(f"A aproximação de e^{x} com precisão de {epsilon} é {ex}")
    
def exponencial(x, epsilon):
    """
    (float, float) -> float
    recebe um x e um epsilon e retorna uma aproximação de e^x com precisção epsilon
    através da série infinita.
    """
    termo = 1.0
    ex = 0.0
    k = 0
    
    while math.fabs(termo) >= epsilon:
        ex = ex + termo
        k += 1
        termo = termo * (x/k)
    return ex


main()
