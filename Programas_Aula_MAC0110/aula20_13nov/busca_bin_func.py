# -*- coding: utf-8 -*-

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
    n = int(input("Forneca o valor de n: "))
    v = []

    print("Fornecer uma sequencia crescente de inteiros:")
    
    for i in range(n):
        num = int(input("\nDigite um elemento da sequencia:"))
        v.append(num)

    print("Sequencia dada: v =", v)

    x = int(input("\nDigite o elemento a ser procurado: "))
    print("\nElemento procurado =", x)

    t = busca_binaria(v, x)   # chamada da funcao busca_binaria

    print() 
    if t >= 0:
        print("Temos v[%d] = %d." %(t,x))
    else:
        print("O elemento %d nao ocorre na sequencia." %(x))

#-----------------------------

def busca_binaria(v, z):
    '''
     (list, int) ---> int
     
     Recebe uma lista crescente v (de numeros inteiros),  
     e um inteiro z; devolve i se v[i] = z; devolve -1  
     se z nao ocorre na lista v.
    '''

    esq = 0         # indice correspondente ao extremo esquerdo da lista a ser examinada
    dir = len(v)-1  # indice correspondente ao ultimo elemento da lista a ser examinada

    while dir >= esq:
        m = (esq + dir) // 2    # indice correspondente ao meio da lista a ser examinada
        if z == v[m]:
            return m            # elemento z foi encontrado na posicao m
        if z < v[m]:              
            dir = m - 1         # para passar   examinar apenas a lista da metade esquerda
        else:
            esq = m + 1         # para passar a examinar apenas a lista da metade direita

    return -1
 #------------------------------
main()

1  2  3  4  5  6  7  8  9  10


0  1  2  3  4  5  6  7  8   9