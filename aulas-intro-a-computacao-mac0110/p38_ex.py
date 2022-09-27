"""
  Programa p38   --- p38_fatorial.py

  Escreva um programa que calcula o fatorial de 0, 5, 17 e 20. 
  O programa deve definir uma função chamada fatorial e fazer uso dela.
"""


def main():
    print(f"O fatorial de 0 é {fatorial(0)}.\n"
          f"O fatorial de 5 é {fatorial(5)}.\n"
          f"O fatorial de 17 é {fatorial(17)}.\n"
          f"O fatorial de 20 é {fatorial(20)}.\n")


def fatorial(n):
    """
    (int) -> int
    """
    n_fat = 1
    cont = 0
    while cont < n:
        cont += 1
        n_fat = n_fat * cont
    return n_fat


main()