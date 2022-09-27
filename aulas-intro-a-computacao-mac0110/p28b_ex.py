"""
   -------------------------------------------------------
   ---------- Uso do operador lógico "or" (ou) ------------
   -------------------------------------------------------
   Programa P28b
   -------------
   Dados três números inteiros positivos, n, i e j, imprimir 
   em ordem crescente os n primeiros naturais que são 
   múltiplos ou de i ou de j ou de ambos.
   Por exemplo, para n=6, i=2 e j=3 a saída deverá ser:
    0    2    3   4    6    8
"""


def main():
    mi = 0
    mj = 0
    cont = 0

    n = int(input("Digite quantos números você quer ver: "))
    i = int(input("Digite o primeiro número: "))
    j = int(input("Digite o segundo número: "))

    while cont < n:
        if mi < mj:
            print(mi)
            mi += i
        elif mj < mi:
            print(mj)
            mj += j
        else:
            print(mi)
            mi += i
            mj += j

        cont += 1


main()
