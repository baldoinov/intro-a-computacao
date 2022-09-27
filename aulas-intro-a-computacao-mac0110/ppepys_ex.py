"""
Arquivo: Pepys.py

PROBLEMA 1:

Em 1693, Samuel Pepys perguntou a Isaac Newton qual dos dois casos é mais provável:
    Caso 1:  Obter "1" pelo menos 1 vez quando se joga um dado honesto 6 vezes;
    Caso 2:  Obter "1" pelo menos 2 vezes quando se joga um dado honesto 12 vezes.

Escreva um programa em Python que decide qual resposta Newton deveria dar.
Seu programa deve fazer um total de N experimentos, onde
N é um número inteiro (grande) a ser lido.


========================================================================
Dica 1: Usar a função  randint (do módulo random)  para geral um número aleatório
         inteiro no intervalo [1,6] para simular as jogadas de um dado
         (com faces 1, 2,.., 6).

Dica 2: Usar a função seed (do módulo random) para poder reproduzir o experimento.

OBS: Faça testes mudando a semente (no programa abaixo foi usado a semente 1);
     faça testes sem usar semente (para isso, remova o comando "random.seed(1)").

=============================================================================
"""
# esse programa não vai bater com os resultados fornecidos pela prof,
# mas ele não está errado

import random
random.seed(1)


def main():
    n = int(input("Insira o número de experimentos a ser realizado: "))    # número de experimentos
    situa1 = caso1(n)
    situa2 = caso2(n)
    print(f"O Caso 1 ocorreu {situa1} vezes.")
    print(f"O Caso 2 ocorreu {situa2} vezes.")


def caso1(n):
    """"
    (int) -> int
    recebe o número de vezes que vai executar o teste
    e retorna quantas vezes a situação desejada ocorreu
    """
    total = 0
    face = 0

    for experimentos in range(0, n):
        for jogadas in range(0, 6):
            face = random.randint(1, 6)
            if face == 1:
                total += 1
                break
    return total


def caso2(n):
    """
    (int) -> int
    recebe o número de vezes que vai executar o teste
    e retorna quantas vezes a situação desejada ocorreu
    """
    cont = 0
    face = 0
    total = 0

    for experimentos in range(0, n):
        for jogadas in range(0, 12):
            face = random.randint(1, 6)
            if face == 1:
                cont += 1
                if cont > 2:
                    break
        if cont > 2:
            total += 1
    return total


main()
