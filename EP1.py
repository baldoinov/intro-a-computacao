# -*- coding: utf-8 -*-

"""
     Nome do aluno: Vitor Domingos Baldoino dos Santos
     Número USP: 11766857
     Curso: Ciências Econômicas
     Disciplina: MAC0110 Introdução à Computação
     Turma 47
     Exercício-Programa EP - 1

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


def main():
    print("Este programa verifica se n é soma de três números primos consecutivos.\n")
    n = int(input("Digite um inteiro positivo para n: "))
    print()

    p = 0
    k = 0  # Soma dos últimos 3 números primos: k1 + k2 + k3
    k1 = 0
    k2 = 0
    k3 = 0

    while p < n and k < n:
        if primo(p):
            k3 = k2
            k2 = k1
            k1 = p
            k = k1 + k2 + k3
            if k == n and k != 5:
                print(f"{n} é a soma de 3 primos.\n"
                      f"{n} = {k3} + {k2} + {k1}")
                break
        p += 1

    if k != n or k == 5:
        print(f"{n} não é a soma de 3 números primos consecutivos.")


# ------------------------------------------------------------------

def primo(m):
    """
    (int) -> bool

    Recebe um inteiro m e retorna se ele é primo (True) ou não (False).
    """

    lim_divisor = m ** (1 / 2)
    d = 3

    if m <= 1 or (m != 2 and m % 2 == 0):  # n <= 1 ou n par
        return False

    while d <= lim_divisor:
        if m % d == 0:
            return False
        d += 2

    return True


# ------------------------------------------------------------------

main()
