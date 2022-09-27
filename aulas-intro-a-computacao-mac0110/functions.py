def comb(n, k):
    """
    (int, int) -> int
    recebe dois números inteiros, n e k, e retorna a combinação de n elementos tomados k a k.
    """
    combina = fatorial(n) // (fatorial(n - k) * fatorial(k))
    return combina


# ------------------------------
def fatorial(p):
    """
        (int) -> int
    """
    p_fat = 1
    cont = 0

    while cont < p:
        cont += 1
        p_fat = p_fat * cont

    return p_fat


# ------------------------------
def mdc(a, b):
    """
    (int, int) -> int
    essa função recebe dois inteiros (a e b) e retorna o máximo divisor comum deles
    """

    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a
