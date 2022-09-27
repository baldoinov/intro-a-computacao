"""
  Programa p41  --  p41_mdc_varios.py
  -----------------------------------

  Dado um inteiro positivo n>=2 , e uma sequência de n números
  inteiros positivos, calcular o mdc desses numeros.

"""


def main():
    print("Dado um inteiro positivo n>=2 , e uma sequência de n números inteiros positivos, calcular o mdc desses "
          "numeros.")

    n = int(input("Insira um número inteiro n: "))
    num_a = int(input("Insira o primeiro número da sequência: "))
    num_b = int(input("Insira o segundo número da sequência: "))

    result = mdc(num_a, num_b)

    p = 2

    while p < n:
        prox_n = int(input("Próximo número: "))
        result = mdc(result, prox_n)
        p += 1

    print(result)


def mdc(a, b):
    """
      (int, int) -> int
      retorna o mdc de dois números
      """

    resto = a % b

    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b


main()
