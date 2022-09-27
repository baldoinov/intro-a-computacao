"""
   Programa p37 --  p37_ocorr_dig.py

   Dado um inteiro positivo n, verificar quantas vezes cada um dos dígitos
   0, 1,..., 9 ocorre em n. Usar obrigatoriamente uma função

     conta_dig(num, dig)

   que retorna o número de vezes que dig ocorre em num.

Ex: se n = 1345689088855433001119, a solução seria:

digito 0 ocorre 3 vezes
digito 1 ocorre 4 vezes
digito 2 ocorre 0 vezes
digito 3 ocorre 3 vezes
digito 4 ocorre 2 vezes
digito 5 ocorre 3 vezes
digito 6 ocorre 1 vezes
digito 7 ocorre 0 vezes
digito 8 ocorre 4 vezes
digito 9 ocorre 2 vezes

"""


def main():
    n = int(input("Digite um número inteiro: "))
    cont = 0

    while cont <= 9:
        total = conta_dig(n, cont)
        print(f"Dígito {cont} ocorre {total} vezes em {n}.")
        cont += 1


# ------------------------------------


def conta_dig(p, m):
    """
    (int, int) -> (int)
    recebe o número p e conta quantas vezes o dígito m aparece nele
    """
    font = 0

    while p > 0:
        if p % 10 == m:
            font += 1
        p = p // 10
    return font


# ------------------------------------
main()
