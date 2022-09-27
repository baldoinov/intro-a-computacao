"""
    Aproximação para pi usando a formula de Ramanujan
"""

from math import sqrt, pi


def main():
    print("Aproximação para pi usando a formula de Ramanujan")

    print(f"Pela formula de ramnujan usada aqui temos: {aproximação()}")
    print(f"Pela aproximação de math.pi temos: {pi}")


def fatorial(m):
    """
    (int) -> int
    recebe um número m e retorna m!
    """

    fat = 1
    for p in range(1, m + 1):
        fat = fat * p
    return fat


def aproximação():
    """
    (none) -> float
    faz o cálculo de pi usando a fórmula de Ramanujan; e somando os termos até que ele fique
    menor que 1e-15

    """
    k = 0
    constante = (2 * sqrt(2)) / 9801
    total = 0

    while True:
        soma_num = fatorial(4 * k) * (1103 + (26390 * k))
        soma_den = (fatorial(k) ** 4) * (396 ** (4 * k))
        parcial = constante * soma_num / soma_den
        total += parcial

        if parcial < 1e-15:
            break

        k += 1
    pi_a = 1 / total
    return pi_a


main()
