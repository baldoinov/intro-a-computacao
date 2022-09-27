"""
  ---- Manipulação de digitos de um número e montagem de novos números
  ------------------------------------------------------------------------
  Programa P31 
  ------------

    Dado um inteiro positivo n, determinar:
    o número de dígitos de n;
    a soma dos dígitos de n;
    o inteiro formado pelos dígitos pares de n na ordem reversa;
    o inteiro formado pelos dígitos ímpares de n na ordem correta
    e verificar se n é um palíndromo.
    Obs. Dizemos que um inteiro não-negativo é um palíndromo se
    ele é igual ao seu reverso. 
"""


def main():
    num = 0
    soma_digitos = 0
    num_digitos = 0
    num_par = 0
    num_impar = 0
    reverso = 0
    potdez = 1

    n = int(input("Insira um número inteiro: "))
    n_copy = n

    while n > 0:

        num = n % 10

        # análise da soma dos digitos e qtd deles
        soma_digitos += num
        num_digitos += 1

        # montagem com números pares e ímpares
        if num % 2 == 0:
            num_par = num_par * 10 + num
        else:
            num_impar = num_impar + num * potdez
            potdez = potdez * 10

        # montagem do reverso
        reverso = reverso * 10 + num

        # descascando n
        n = n // 10

    print(f"O número {n_copy} têm {num_digitos} dígitos.\n"
          f"A soma desses dígitos é {soma_digitos}.\n"
          f"O inteiro formado pelos números pares de {n_copy} na ordem reversa é {num_par}.\n"
          f"O inteiro formado pelos números ímpares de {n_copy} na ordem correta é {num_impar}.")
    if reverso == n_copy:
        print(f"O número {n_copy} é um palíndromo.")
    else:
        print(f"O número {n_copy} não é um palíndromo.")


main()
