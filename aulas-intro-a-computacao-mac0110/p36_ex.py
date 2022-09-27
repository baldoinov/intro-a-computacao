"""
   Programa p36 ----  p36_dig_menores8.py

   Dado n (um número inteiro positivo), verificar se todos
   os dígitos de n são menores que 8.
   [Resolver usando "indicador de status" (variável booleana)]

"""


def main():
    n = int(input("Digite um número inteiro positivo: "))
    n_copy = n
    under8 = True
    dig = 0
    cont = 0

    while n > 0:
        dig = n % 10
        if dig >= 8:
            under8 = False
            cont += 1
        n = n // 10
    if under8:
        print(f"Todos os dígitos de {n_copy} são menores que 8.")
    else:
        print(f"{n_copy} tem {cont} dígitos maiores que 8.")


main()
