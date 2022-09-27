def main():
    n = str(input("Insira um número natural na base binária para ver ele na forma de base decimal: "))
    k = int(n, 2)    # int() só faz a conversão caso o 1º parâmetro seja str

    print(f"{n} na base decimal é {k}.")


main()
