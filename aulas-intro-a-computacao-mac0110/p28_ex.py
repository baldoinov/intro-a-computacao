"""
   -------------------------------------------------------
   ---------- Uso do operador lógico "or"(ou) ------------
   -------------------------------------------------------
   Programa P28a
   -------------
   Dados três números inteiros positivos, n, i e j, imprimir
   em ordem crescente os n primeiros naturais que são
   múltiplos ou de i ou de j ou de ambos.
   Por exemplo, para n=6, i=2 e j=3, a saída deverá ser:
    0    2    3   4    6    8
"""

def main():
    m = 0
    cont = 0

    n = int(input("Digite quantos números você quer ver: "))
    i = int(input("Digite o primeiro número: "))
    j = int(input("Digite o segundo número: "))
    print(f"\nOs {n} primeiros naturais múltiplos de {i} e {j} são: ")

    while cont < n:
        if m % i == 0 or m % j == 0:
            print(m)
            cont += 1
        m += 1


main()
