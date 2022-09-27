
################## new ##################

'''
   Dados um inteiro positivo n e uma sequência de n números inteiros,
   imprimí-los em ordem crescente.
'''
#------------------------------------------------------------------------

def main():
    n = int(input("Digite o número de elementos da sequência: "))
    
    seq = []  

    for i in range(n):
        num = int(input("\nDigite um inteiro da sequência: "))
        seq.append(num)    
    
    print("\nLista de inteiros na ordem lida: \n", seq)

    # os elementos da lista seq serão rearranjados para que fiquem em ordem crescente
    ordenacao_por_selecao(seq)
    
    print("\nLista de inteiros em ordem crescente: \n", seq)

    print("\nSequência de inteiros em ordem:")
    print(seq)

#------------------------------------------------------------------------

def ordenacao_por_selecao(lista):
    ''' (list) -> NoneType
       
    Recebe uma lista com todos os valores de mesmo tipo.
    Rearranja os elementos de lista em ordem crescente; ou seja,
    de modo que satisfaçam: lista[0] <= lista[1] <= ...
    '''

    print()
    print("----------lista =", lista)   # apenas para teste
    n = len(lista)
    for i in range(0, n-1, 1):
        # determina índice do menor elemento em lista[i ... n-1]    
        indmenor = i
        for j in range(i+1, n, 1):
            if lista[indmenor] > lista[j]:
                indmenor = j
            
        if indmenor != i:
            # troque lista[i] com lista[indmenor]       
            aux = lista[i]
            lista[i] = lista[indmenor]
            lista[indmenor] = aux
 
            #  as três linhas acima podem ser substituídas por:
            #  lista[i], lista[indmenor] = lista[indmenor], lista[i]

        # neste ponto, lista[0 ... i] está em ordem crescente
        print("i = %2d -- lista = %s" %(i, lista)) # apenas para teste   
            
#------------------------------------------------------------------------
main()
#------------------------------------------------------------------------


