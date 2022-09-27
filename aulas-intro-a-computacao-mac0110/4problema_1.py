"""
PROBLEMA 1 - imprimir na ordem inversa

Dados um inteiro positivo n e uma sequência (lista) de n inteiros,
imprimi-los na ordem inversa à da leitura.
"""

def main():
    print("Esse programa pega uma lista de números e os imprime na ordem reversa.")

    x = []
    n = int(input("Digite a quantidade de termos da lista: "))
    for i in range(0, n):
        num = int(input("Digite um número para a lista: "))
        x.append(num)
    
    print("A lista em ordem reversa é: ")
    for i in range(n-1, -1, -1):
        print(x[i])


main()
