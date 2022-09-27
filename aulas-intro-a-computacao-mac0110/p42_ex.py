"""
======= Já vimos:  Fatorial usando o comando "while" =======
======================= programa p12a ======================
========= Este é o fatorial usando o comando "for" =========
"""


def main():
    n = int(input("Digite um número para ver seu fatorial: "))
    fat = 1

    for k in range(1, n + 1):
        fat = fat * k
    print(f"{n}! = {fat}")


main()
