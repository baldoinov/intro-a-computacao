"""

   Dado n, calcula o número Harmônico H(k), para k variando de 1 a n.

   H(k) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/k.

"""


def main():
    print("Dado n, calcula o número Harmônico H(k), para k variando de 1 a n.")
    n = int(input("Insira n: "))
    h = 0.0
    for k in range(1, n + 1):
        h = h + (1.0/k)
        print(f"H({k}) = {h}")



main()
