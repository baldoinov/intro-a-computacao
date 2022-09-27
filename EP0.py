# -*- coding: utf-8 -*-

"""
     Nome do aluno: Vitor Domingos Baldoino dos Santos
     Número USP: 11766857
     Curso: Ciências Econômicas
     Disciplina: MAC0110 Introdução à Computação
     Turma 47
     Exercício-Programa EP - 0

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
    k3 = -1  # F(k-3)
    k2 = 1  # F(k-2)
    k1 = 0  # F(k-1)
    k = 0   # F(k), k <= 0
    cont = 0

    n = int(input("Insira um inteiro n (n >= 0) para ver o T(n) da sequência de Trinacci: "))

    while cont <= n:    # Soluçao usada no fibo_ex2 para imprimir somente F(n)
        k = k3 + k2 + k1
        k3 = k2
        k2 = k1
        k1 = k
        cont += 1

    print(f"T({n}) = {k}")


main()
