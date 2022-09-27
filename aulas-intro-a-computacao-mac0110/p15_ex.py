"""
 programa p15      ---      p15b_mdc.py

 Este programa recebe dois numeros inteiros positivos a, b  e calcula o
 maximo divisor comum (mdc) desses numeros, usando o algoritmo de
 Euclides.
"""

def main():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    a_copy = a
    b_copy = b

    while b != 0:
        resto = a % b
        a = b
        b = resto

    print(f"MDC({a_copy}, {b_copy}) = {a}")


main()
