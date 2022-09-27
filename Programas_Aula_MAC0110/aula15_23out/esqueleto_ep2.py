# -*- coding: utf-8 -*-
"""
    escreva o cabe�alho inicial

"""
# -------------------------------------------------------------------------

import math
# para usar as fun��es sqrt e fabs, e a constante pi
# -------------------------------------------------------------------------

def main():
    """
        ???
    """
   
    # escreva sua fun��o aqui
    
# -------------------------------------------------------------------------

def f(x):
    """ (float) -> float

    Recebe um n�mero real x e se (1.0-x*x) for positivo, retorna  
    a raiz quadrada de (1.0-x*x); em caso contr�rio, retorna 0.
    Obs.: para determinar a raiz quadrada � utilizada a fun��o sqrt do
    m�dulo math.
    """
  
    # escreva sua fun��o aqui
    
# -------------------------------------------------------------------------

def areaMetodoRetangulos(a, b, k):
    """ (float, float, int) -> float

    Recebe dois n�meros reais a e b, com a < b, e um inteiro positivo k.
    Esta fun��o retorna um valor aproximado para a �rea sob a fun��o f(x),
    no intervalo [a, b], calculada pelo m�todo dos ret�ngulos, utilizando
    k ret�ngulos.
    """
  
    # escreva sua fun��o aqui
    
# -------------------------------------------------------------------------

def areaMetodoTrapezios(a, b, k):
    """ (float, float, int) -> float

    Recebe dois n�meros reais a e b, com a < b, e um inteiro positivo k.
    Esta fun��o retorna um valor aproximado para a �rea sob a fun��o f(x),
    no intervalo [a, b], calculada pelo m�todo dos trap�zios, utilizando
    k trap�zios.
    """
  
    # escreva sua fun��o aqui
    
# -------------------------------------------------------------------------

def piSerieWallis(eps):
    """ (float) -> int, float

    Recebe um n�mero real eps, com 0 < eps < 1. 
    Esta fun��o calcula um valor aproximado para pi, piAproxWallis, 
    atrav�s da s�rie de Wallis, incluindo os primeiros termos at�
    que o valor absoluto da diferen�a entre o valor calculado 
    piAproxWallis e o valor da constante math.pi seja menor do que 
    eps. A fun��o retorna o n�mero de termos considerados e o valor
    calculado piAproxWallis.
    Obs.: para determinar o valor absoluto � utilizada a fun��o fabs
    do m�dulo math.
    """
  
    # escreva sua fun��o aqui
    
# -------------------------------------------------------------------------

def piSerieNilakantha(eps):
    """ (float) -> int, float

    Recebe um n�mero real eps, com 0 < eps < 1. 
    Esta fun��o calcula um valor aproximado para pi, piAproxNilakantha,
    atrav�s da s�rie de Nilakantha, incluindo os primeiros termos at� 
    que o valor absoluto da diferen�a entre o valor calculado 
    piAproxNilakantha e o valor da constante math.pi seja menor do que
    eps. A fun��o retorna o n�mero de termos considerados e o valor 
    calculado piAproxNilakantha.
    Obs.: para determinar o valor absoluto � utilizada a fun��o fabs 
    do m�dulo math.
    """
  
    # escreva sua fun��o aqui
    
# -------------------------------------------------------------------------
main()