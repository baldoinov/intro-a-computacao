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

import random
random.seed(1)


def main():
    n = int(input("Digite o número de experimentos a ser realizado: "))

    caso1 = 0
    caso2 = 0

    for i in range(0, n):
        face = 0
        jogadas = 0
        face1 = 0

        # teste do caso 1
        while jogadas < 6 and face1 < 1:
            face = random.randint(1, 6)
            if face == 1:
                face1 += 1
                caso1 += 1
            jogadas += 1

        # teste do caso 2
        face = 0
        jogadas = 0
        face2 = 0
        while jogadas < 12 and face2 < 2:
            face = random.randint(1,6)
            if face == 1:
                face2 += 1
            jogadas += 1
        if face2 > 1:
            caso2 += 1

    print(f"O caso 1 ocorreu {caso1} vezes.")
    print(f"O caso 2 ocorreu {caso2} vezes.")

    if caso1 > caso2:
        print("O caso 1 é mais provável.")
    elif caso2 > caso1:
        print("O caso 2 é mais provável.")


main()
        
