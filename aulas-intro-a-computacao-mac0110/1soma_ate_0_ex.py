# Dada uma sequencia de inteiros, cujo último termo é um zero,
# determinar a soma dos inteiros que foram dados.
#
# (OBS: o zero é usado para informar que acabou a sequencia.)
# Exemplo: Se for dada a sequencia:  25  30  2  78  10  0
# o seu programa deve imprimir que a soma é 145

def main():
    cont = 0
    n = 1
    while n != 0:
        n = int(input("Insira uma sequência de número inteiros e digite 0 quando quiser somá-los: "))
        cont += n
    print(f"A soma dos números fornecidos é {cont}.")

main()
