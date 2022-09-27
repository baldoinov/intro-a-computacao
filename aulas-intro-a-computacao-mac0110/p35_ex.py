# -*- coding: utf-8 -*-
"""
  ------------------------------------------------------
   --------------- Uso de função -----------------------
  ------------------------------------------------------
  programa:  p35a_soma_de_primos.py
  --------------------------------
  Dado um inteiro positivo n, verifica se n é soma de dois números primos.

  OBS: O programa deve fazer uso de uma funcao que verifica se um numero é primo

"""

def main():
    print("\nEsse programa verifica se n é a soma de dois números primos.\n")
    n = int(input("Insira um número positivo para n: "))

    p = 0
    k = 0
    k1 = 0
    k2 = 0

    while p < n:
        if primo(p) and primo(n-k):
            k2 = k1
            k1 = p
            k = k1 + k2
            if k == n and k != 2:
                print(f"{n} é a soma de dois números primos.\n"
                      f"{n} = {k1} + {k2}")
                break
        p += 1

    if k != n or k == 2:
        print(f"{n} não é a soma de dois números primos")


def primo(m):
    """
    (int) -> bool
    :param m: (int)
    :return: bool

    essa função recebe um número inteiro e retorna se ele é primo (True) ou não (False).
    """
    lim_divisor = m**(1/2)
    d = 3

    if m <= 1 or (m != 2 and m % 2 == 0):
        return False

    while d <= lim_divisor:
        if m % d == 0:
            return False
        d += 2
    return True


main()

