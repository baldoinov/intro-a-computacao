# -*- coding: utf-8 -*-
"""
    escreva o cabeçalho inicial

"""
# -------------------------------------------------------------------------

import math
# para usar as funções sqrt e fabs, e a constante pi
# -------------------------------------------------------------------------

def main():
    """
        ???
    """
   
    # escreva sua função aqui
    
# -------------------------------------------------------------------------

def f(x):
    """ (float) -> float

    Recebe um número real x e se (1.0-x*x) for positivo, retorna  
    a raiz quadrada de (1.0-x*x); em caso contrário, retorna 0.
    Obs.: para determinar a raiz quadrada é utilizada a função sqrt do
    módulo math.
    """
  
    # escreva sua função aqui
    
# -------------------------------------------------------------------------

def areaMetodoRetangulos(a, b, k):
    """ (float, float, int) -> float

    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x),
    no intervalo [a, b], calculada pelo método dos retângulos, utilizando
    k retângulos.
    """
  
    # escreva sua função aqui
    
# -------------------------------------------------------------------------

def areaMetodoTrapezios(a, b, k):
    """ (float, float, int) -> float

    Recebe dois números reais a e b, com a < b, e um inteiro positivo k.
    Esta função retorna um valor aproximado para a área sob a função f(x),
    no intervalo [a, b], calculada pelo método dos trapézios, utilizando
    k trapézios.
    """
  
    # escreva sua função aqui
    
# -------------------------------------------------------------------------

def piSerieWallis(eps):
    """ (float) -> int, float

    Recebe um número real eps, com 0 < eps < 1. 
    Esta função calcula um valor aproximado para pi, piAproxWallis, 
    através da série de Wallis, incluindo os primeiros termos até
    que o valor absoluto da diferença entre o valor calculado 
    piAproxWallis e o valor da constante math.pi seja menor do que 
    eps. A função retorna o número de termos considerados e o valor
    calculado piAproxWallis.
    Obs.: para determinar o valor absoluto é utilizada a função fabs
    do módulo math.
    """
  
    # escreva sua função aqui
    
# -------------------------------------------------------------------------

def piSerieNilakantha(eps):
    """ (float) -> int, float

    Recebe um número real eps, com 0 < eps < 1. 
    Esta função calcula um valor aproximado para pi, piAproxNilakantha,
    através da série de Nilakantha, incluindo os primeiros termos até 
    que o valor absoluto da diferença entre o valor calculado 
    piAproxNilakantha e o valor da constante math.pi seja menor do que
    eps. A função retorna o número de termos considerados e o valor 
    calculado piAproxNilakantha.
    Obs.: para determinar o valor absoluto é utilizada a função fabs 
    do módulo math.
    """
  
    # escreva sua função aqui
    
# -------------------------------------------------------------------------
main()