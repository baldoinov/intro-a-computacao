def main():
    an = 0
    an_1 = 0
    an_2 = 0
    r = 0
    k = 0
    progressao = True
    cont = 1

    n = int(input("Insira quantos termos terá a sequência númerica (2+): "))
    if n >= 2:
        an_1 = int(input("Insira o 1º termo: "))
        an_2 = int(input("Insira o 2º termo: "))
        r = an_2 - an_1
        k = an_2
        cont += 2

    while cont <= n:
        an = int(input(f"Insira o {cont}º termo: "))
        if an != k + r:
            progressao = False

        k = an
        cont += 1

    if progressao:
        print("É uma progressão aritímetica!")
    else:
        print("Não é uma progressão aritímetica!")

main()
