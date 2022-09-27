"""
  ---- Manipulação de digitos de um número --------
  -------------------------------------------------
  Programa P30 
  ------------
  Dados um inteiro n > 0  e um digito d (0<=d<=9)
  determinar quantas vezes d ocorre em n.

"""


def main():
    n = int(input("Digite um número inteiro: "))
    d = int(input("Digite o dígito a ser procurado: "))
    n_copy = n
    cont = 0

    while n > 0:
        if n % 10 == d:
            cont += 1
        n = n // 10

    print(f"O número {d} aparece {cont} vezes em {n_copy}.")


main()
