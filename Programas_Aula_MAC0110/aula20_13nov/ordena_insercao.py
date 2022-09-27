
######################### new 

'''
   Dados um inteiro positivo n e uma sequência de n números inteiros,
   imprimi-los em ordem crescente.
'''
#-----------------------------------------------------------------------

def main():
    n = int(input("Digite o número de elementos da sequência: "))
    
    seq = []  

    for i in range(n):
        num = int(input("Digite um inteiro da sequência: "))
        seq.append(num)    
    
    print("\nLista de inteiros na ordem lida: \n", seq)

    #  os elementos da lista seq serão rearranjados para que fiquem em ordem crescente
    ordenacao_por_insercao(seq)
    
    print("\nLista de inteiros em ordem crescente: \n", seq)

    print("\nSequência de inteiros em ordem crescente:")
    for num in seq:
        print(num, end='  ')   
    print()

#------------------------------------------------------------------------

def ordenacao_por_insercao(lista):
    ''' (list) -> NoneType
       
    Recebe uma lista com todos os valores de mesmo tipo.
    Rearranja os elementos de lista em ordem crescente; ou seja,
    de modo que satisfaçam: lista[0] <= lista[1] <= ...
    '''
    
    print()
    print("----------lista =", lista)   # apenas para teste
    n = len(lista)
    for i in range(1, n, 1):
        # 'Insere', ou seja, posiciona lista[i] em lista[0...i]
        # de modo que lista[0] <= ... <= lista[i]
        item = lista[i]
        j = i-1 
        while j >= 0 and lista[j] > item:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = item
        print("i = %2d -- lista = %s" %(i, lista)) # apenas para teste   
        
#------------------------------------------------------------------------
main()
