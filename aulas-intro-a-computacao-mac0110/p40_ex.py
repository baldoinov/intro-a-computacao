"""
   Programa p40 --- p40_coef_expansao.py

   Usando as função coef_bin(.,.) definida no programa p39_ex.py,

   escreva um programa que lê um inteiro n, n >= 0 e imprime os 
   coeficientes da expansão de (x+y) elevado a n.

   !!!! BINÔMIO DE NEWTON

"""


def main():
    import functions

    k = 0
    n = int(input("Insira um inteiro n: "))
    print(f"n = {n}")
    # print("Portanto, os coeficientes são")
    while k <= n:
        resultado = functions.comb(n, k)
        print(f"{resultado} * (x^{n-k}) * (y^{k})")
        k += 1


main()
