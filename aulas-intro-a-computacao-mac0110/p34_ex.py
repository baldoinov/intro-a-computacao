"""
    Programa p34 ----------- 34(a;b;c;d;e)_primo.py
   --------------------------------------------------

   Dado n (inteiro positivo), testar se n é primo.
   Def: um inteiro positivo n é primo se tem exatamente dois divisores: o 1 e o próprio n.
  (1 não é primo; 2 é primo; 3 é primo; 4 não é primo; 5 é primo,...)
   
   Há diversas soluções para esse problema, farei a mais eficiente
"""

from math import sqrt

def main():
    n = int(input("Insira um número inteiro positivo: "))
    d = 3
    lim_d = sqrt(n)
    e_primo = True

    if n <= 1 or (n != 2 and n % 2 == 0):  # n <= 1 ou n par
        e_primo = False
    else:  # n = 2 ou n >= 3
        e_primo = True

    while d <= lim_d and e_primo:
        if n % d == 0:
            e_primo = False

        d += 2

    if e_primo:
        print(f"{n} é um número primo.")
    else:
        print(f"{n} não é um número primo.")


main()
