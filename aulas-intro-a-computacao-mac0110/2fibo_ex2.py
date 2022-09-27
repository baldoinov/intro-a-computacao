def main():
    n2 = 0    # F(0); F(n-2)
    n1 = 1    # F(1); F(n-1)
    cont = 0

    k = int(input("Insira um inteiro k para ver F(k) da sequência Fibonacci: "))

    while cont < k - 1:
        n = n1 + n2    # F(n) = F(n-1) + F(n-2)
        n2 = n1
        n1 = n
        cont += 1
    print(f"F({k})= {n}")

main()
