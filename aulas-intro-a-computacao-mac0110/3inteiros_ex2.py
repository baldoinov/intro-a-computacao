def main():
    an = 0
    an1 = 0
    an2 = 0
    an3 = 0
    r = 0

    progressao = False
    cont = 1
    t = int(input("Insira quantos termos terá a sequência númerica: "))

    while cont <= t:
        an = int(input(f"Insira o {cont}° termo: "))

        r = an - an1
        an3 = an2
        an2 = an1
        an1 = an

        if an == an3 + 2 * r:
            progressao = True
        else:
            progressao = False

        cont += 1

    if progressao:
        print("É uma progressão aritimética.")
    else:
        print("Não é uma progressão aritimética.")


main()
