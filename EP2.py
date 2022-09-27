# -*- coding: utf-8 -*-

"""
     Nome do aluno: Vitor Domingos Baldoino dos Santos
     Número USP: 11766857
     Curso: Ciências Econômicas
     Disciplina: MAC0110 Introdução à Computação
     Turma 47
     Exercício-Programa EP - 2

     DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.
     DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
     SERÃO TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA
     DISCIPLINA.
"""

import math

def main():
    print("-" * 74)
    print("ALGUMAS APROXIMAÇÕES PARA O VALOR DE PI:")
    print("(utilizamos math.pi que é 3.141592653589793)")
    print("-" * 74)

    pi = math.pi

    # Método 1 ----------------------------------

    print("\nMétodo 1 - Valor aproximado para PI utilizando o Método dos Retângulos")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    i = 0
    k = 2**i

    piAproxRetangulos = 4 * areaMetodoRetangulos(0.0, 1.0, k)

    while math.fabs(piAproxRetangulos - pi) >= eps:
        i += 1
        k = 2**i
        piAproxRetangulos = 4 * areaMetodoRetangulos(0.0, 1.0, k)
    print(f"Número de retângulos considerados para o cálculo da última área: {k}")
    print(f"Valor aproximado para pi: {piAproxRetangulos}\n")

    # Método 2 ----------------------------------

    print("-" * 74)
    print("\nMétodo 2 - Valor aproximado para PI utilizando o Método dos Trapézios")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    i = 0
    k = 2**i

    piAproxTrapezios = 4 * areaMetodoTrapezios(0.0, 1.0, k)

    while math.fabs(piAproxTrapezios - pi) >= eps:
        i += 1
        k = 2**i
        piAproxTrapezios = 4 * areaMetodoTrapezios(0.0, 1.0, k)
    print(f"Número de trapézios considerados para o cálculo da última área: {k}")
    print(f"Valor aproximado para pi: {piAproxTrapezios}\n")

    # Método 3 ----------------------------------

    print("-" * 74)
    print("\nMétodo 3 - Valor aproximado para PI utilizando a Série de Wallis")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))

    termos, piAproxWallis = piSerieWallis(eps)

    print(f"Número de termos da série incluidos no cálculo: {termos}")
    print(f"Valor aproximado para pi: {piAproxWallis}\n")

    # Método 4 ----------------------------------

    print("-" * 74)
    print("\nMétodo 4 - Valor aproximado para PI utilizando a Série de Nilakantha")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))

    termos, piAproxNilakantha = piSerieNilakantha(eps)

    print(f"Número de termos da série incluidos no cálculo: {termos}")
    print(f"Valor aproximado para pi: {piAproxNilakantha}\n")

# -------------------------------------------------------------------------

def f(x):
    """ (float) -> float
    Recebe um numero real x e se (1.0-x*x) for positivo, retorna
    a raiz quadrada de (1.0-x*x); em caso contrario, retorna 0.
    Obs.: para determinar a raiz quadrada é utilizada a funcao sqrt do
    modulo math.
    """
    if (1.0 - x * x) > 0:
        return math.sqrt(1.0 - x * x)
    else:
        return 0

# -------------------------------------------------------------------------

def areaMetodoRetangulos(a, b, k):
    """ (float, float, int) -> float

    Recebe dois numeros reais a e b, com a < b, e um inteiro positivo k.
    Esta funcao retorna um valor aproximado para a area sob a funcao f(x),
    no intervalo [a, b], calculada pelo metodo dos retangulos, utilizando
    k retangulos.
    """

    delta_x = (b-a)/k
    area_função = 0.0
    for p in range(1, k+1):
        area_função += f(a + p*delta_x) * delta_x
    return area_função

# -------------------------------------------------------------------------

def areaMetodoTrapezios(a, b, k):
    """ (float, float, int) -> float

    Recebe dois numeros reais a e b, com a < b, e um inteiro positivo k.
    Esta funcao retorna um valor aproximado para a area sob a funcao f(x),
    no intervalo [a, b], calculada pelo metodo dos trapezios, utilizando
    k trapezios.
    """

    delta_x = (b-a)/k
    area_função = 0.0
    for i in range(1, k+1):
        area_função += ((f(a+(i - 1)*delta_x) + f(a + i*delta_x))*delta_x)/2
    return area_função
    
# -------------------------------------------------------------------------

def piSerieWallis(eps):
    """ (float) -> int, float

    Recebe um numero real eps, com 0 < eps < 1. 
    Esta funcao calcula um valor aproximado para pi, piAproxWallis, 
    atraves da serie de Wallis, incluindo os primeiros termos ate
    que o valor absoluto da diferenca entre o valor calculado 
    piAproxWallis e o valor da constante math.pi seja menor do que 
    eps. A funcao retorna o numero de termos considerados e o valor
    calculado piAproxWallis.
    Obs.: para determinar o valor absoluto e utilizada a funcao fabs
    do modulo math.
    """
    pi = math.pi
    num = 2
    den = 1
    piAproxWallis = 2 * (num / den)
    cont = 0
    termos = 1

    while math.fabs(piAproxWallis - pi) >= eps:
        if cont % 2 == 0:
            den += 2
        else:
            num += 2
        piAproxWallis = piAproxWallis * (num / den)
        termos += 1
        cont += 1
    return termos, piAproxWallis

# -------------------------------------------------------------------------

def piSerieNilakantha(eps):
    """ (float) -> int, float

    Recebe um numero real eps, com 0 < eps < 1. 
    Esta funcao calcula um valor aproximado para pi, piAproxNilakantha,
    atraves da serie de Nilakantha, incluindo os primeiros termos ate 
    que o valor absoluto da diferenca entre o valor calculado 
    piAproxNilakantha e o valor da constante math.pi seja menor do que
    eps. A funcao retorna o numero de termos considerados e o valor 
    calculado piAproxNilakantha.
    Obs.: para determinar o valor absoluto e utilizada a funcao fabs 
    do modulo math.
    """
    pi = math.pi
    piAproxNilakantha = 3
    a = 2
    sinal = 1
    ter = 4.0/(a*(a+1)*(a+2))   # termo da soma
    termos = 1

    while math.fabs(piAproxNilakantha - pi) >= eps:
        piAproxNilakantha = piAproxNilakantha + sinal * ter
        sinal = - sinal
        a += 2
        ter = 4.0/(a * (a+1) * (a+2))
        termos += 1
    return termos, piAproxNilakantha


# -------------------------------------------------------------------------
main()
