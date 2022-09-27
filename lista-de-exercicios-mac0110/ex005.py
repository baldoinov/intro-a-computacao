import sys

def main():
    d = 1
    diadomes = 1
    menor = -sys.maxsize
    maior = sys.maxsize

    while d <= 31:
        vendas = int(input(f"Insira as vendas do {d}º dia: "))

        if vendas > menor:
            maior = vendas
            menor = vendas
            diadomes = d

        d += 1

    print(f"A maior venda do mês foi de {maior} discos, no dia {diadomes} de março.")


main()
