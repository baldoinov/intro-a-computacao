"""
 Programa p39  -- p39_binomial.py

 Escreva um programa para calcular os coeficientes binomiais
 Comb(4,2),Comb(5,2) e Comb(10,4).

 Fazer uso de uma função que recebe dois inteiros, n e k como parâmetros, e 
 retorna a combinação de n objetos tomados k a k  = Comb(n,k) =  n!/((n-k)!k!).
 Esta função por sua vez, deve fazer uso da função fatorial (embora não seja 
 a forma mais rápida de calcular Comb(n,k)). 

"""


def main():
    print(f"A combinação de 4 tomado 2 a 2 é {comb(4, 2)}.\n"
          f"A combinação de 5 tomado 2 a 2 é {comb(5, 2)}.\n"
          f"A combinação de 10 tomado 4 a 4 é {comb(10, 4)}.\n")


# ------------------------------
def comb(n, k):
    """
    (int, int) -> int
    recebe dois números inteiros, n e k, e retorna a combinação de n elementos tomados k a k.
    """
    combina = fatorial(n) // (fatorial(n - k) * fatorial(k))
    return combina


# ------------------------------
def fatorial(p):
    p_fat = 1
    cont = 0

    while cont < p:
        cont += 1
        p_fat = p_fat * cont

    return p_fat


# ------------------------------
main()
