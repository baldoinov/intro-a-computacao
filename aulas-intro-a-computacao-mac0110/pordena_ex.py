'''
   Dados um inteiro positivo n e uma sequência de n números inteiros,
   imprimí-los em ordem crescente.
'''

def main():
    n = int(input("Digite o número de elementos da sequência: "))
    seq_inser = []
    seq_sele = []
    seq_eu = []
    for i in range(1, n+1):
        num = int(input(f"Digite o {i}° número da sequência: "))
        seq_sele.append(num)
        seq_inser.append(num)
        seq_eu.append(num)
    
    ordena_selecao(seq_sele)
    ordena_insercao(seq_inser) # está dando errado
    minha_solucao(seq_eu)

    print("\nAs listas ordenadas usando os diferentes métodos são: \n")
    print(seq_sele, seq_inser, seq_eu, sep="\n")


def ordena_selecao(lista):
    '''
    (list) -> NoneType
    Recebe uma lista e a reorganiza em ordem crescente usando o metódo de selecionar o número
    menor e inserir no lugar do maior fora de ordem.
    '''
    n = len(lista)

    for i in range(0, n-1):
        indmenor = i
        for j in range(i+1, n):
            if lista[indmenor] > lista[j]:
                indmenor = j

        if indmenor != i:
            lista[i], lista[indmenor] = lista[indmenor], lista[i]


def ordena_insercao(lista):
    '''
    (list) -> NoneType
    Recebe uma lista e a reorganiza em ordem crescente usando o metódo de selecionar o número
    menor no lugar do maior fora de ordem.
    '''
    n = len(lista)

    for i in range(1, n):
        item = lista[i]
        j = i-1
        while j >= 0 and lista[j] > item:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = item


def minha_solucao(lista):
    '''
    (list) -> NoneType
    Adaptação da ordena_selecao menos eficiente.
    '''
    n = len(lista)
    for k in range(n):
        for i in range(n):
            for j in range(i+1, n):
                if lista[i] > lista[j]:
                    lista[i], lista[j] = lista[j], lista[i]


main()
