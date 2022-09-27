def main():
    n = int(input("Insira um número n para exibir os n primeiros números impares: "))
    k = 1
    cont = 0

    while cont < n:
        print(k)
        cont += 1
        k = k + 2


main()
