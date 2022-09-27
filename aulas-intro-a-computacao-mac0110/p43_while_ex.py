"""

   Dado n, calcula o número Harmônico H(k), para k variando de 1 a n.

   H(k) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/k.

"""


def main():
    print("Dado n, calcula o número Harmônico H(k), para k variando de 1 a n.")
    n = int(input("Insira n: "))
    k = 1
    h = 0

    while k < n:
        h += (1/k)
        k += 1
        print(f"H({k}) = {h}")


main()