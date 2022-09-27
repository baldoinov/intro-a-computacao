def main():
    n = int(input("Insira um número na base decimal para ver sua forma binária: "))
    k = bin(n)

    print(f"{n} em base binária é {k[2:]}.")


main()
