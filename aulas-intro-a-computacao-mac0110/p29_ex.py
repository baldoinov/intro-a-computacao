"""
  ---- Manipulação de digitos de um número --------
  -------------------------------------------------
  Programa P29
  ------------
  Dados um inteiro n > 0
  determinar a soma dos digitos de n.

"""


def main():

    soma = 0
    n = int(input("Digite um número inteiro para ver a soma de seus digitos: "))
    n_copy = n

    while n > 0:
        soma += n % 10
        n = n // 10

    print(f"A soma dos digitos de {n_copy} é {soma}.")


main()
