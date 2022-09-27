def main():
    # F(n) = F(n-1) + F(n-2)
    n2 = 0  # F(0); F(n-2)
    n1 = 1  # F(1); F(n-1)
    cont = 0

    k = int(input("Digite um inteiro k para imprimir os primeiros k termos da sequência de Fibonacci: "))

    while cont < k:
        print(f"F({cont}) = {n2}", end="; ")
        n = n1 + n2
        n2 = n1
        n1 = n
        cont += 1
main()