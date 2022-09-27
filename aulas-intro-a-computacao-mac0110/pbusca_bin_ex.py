'''                                                                                                                                                                      
   arquivo: busca_bin_func.py
   --- ------------------------                                                                                                                                              
    Este programa recebe uma sequencia crescente de n inteiros                                                                                                            
    e um inteiro x.  Determina se x ocorre na sequencia dada.                                                                                                             
    Faz uso de uma funcao que devolve a posicao da sequencia
    em que x ocorre, se x ocorre na sequencia; e devolve -1 se 
    x nao ocorre na sequencia.

'''

def main():
    print("Este programa determina se um número ocorre na sequência dada.")
    print("A sequência deve ser crescente.\n")
    n = int(input("Qual o tamanho da sequência? "))
    seq = []
    print()
    for i in range(1, n+1):
        num = int(input(f"Digite o {i}° número da sequência: "))
        seq.append(num)
    
    x = int(input("\nQual o número procurado? "))

    t = ocorre(seq, x)

    if t >= 0:
        print(f"\nO elemento ocorre na posião {t} da lista")
    else:
        print("\nO elemento não ocorre na lista.")


def ocorre(lista, x):
    '''
    (list, int) -> int
    '''
    esq = 0
    direita = len(lista) - 1

    while direita >= esq:
        meio = (esq + direita) // 2
        if lista[meio] == x:
            return meio
        elif lista[meio] > x:
            direita = meio - 1
        else:
            esq = meio + 1
    return -1


main()
