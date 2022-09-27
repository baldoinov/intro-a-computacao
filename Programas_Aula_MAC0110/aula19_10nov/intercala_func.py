
####################### new 

'''
   Dados dois inteiros positivos m e n, e duas sequências em ordem 
   crescente, sem repetições, com m e n inteiros, respectivamente, 
   determinar uma única sequência, contendo todos os elementos das 
   sequências originais em ordem crescente e sem repetições. 
'''
# --------------------------------------------------------------------------

def main():
    print("Obs.: Os inteiros nas duas sequências fornecidas pelo usuário")
    print("devem estar em ordem crescente e não ter números repetidos.")

    print("\nDados da primeira sequência: ")
    # seq1 referencia uma lista criada com os elementos da 1a. seq. 
    seq1 = le_seq_int_cria_lista()
    
    print("\nDados da segunda sequência: ")
    # seq2 referencia uma lista criada com os elementos da 2a. seq.
    seq2 = le_seq_int_cria_lista()
    
    print("\nPrimeira lista: ", seq1)
    print("\nSegunda lista: ", seq2)
      
    #  seq referencia uma lista criada intercalando-se os elementos das
    #  listas seq1 e seq2, sem repetições
    seq = intercala_duas_listas(seq1, seq2)
    
    print("\nLista resultante da intercalação das duas listas:")
    print(seq)
        
    print("\nSequência (com %d inteiros) resultante da intercalação das "
          "duas sequências:" %(len(seq)))
    for num in seq: #<===============================
        print(num, end='  ')
    print()
                
#---------------------------------------------------------------------------

def le_seq_int_cria_lista():
    ''' ( ) -> list
   
    Lê do teclado o tamanho n (>0) e os n números inteiros de uma sequência.
    Cria uma lista com esses n inteiros e retorna a lista criada. 
    '''

    n = int(input("Digite o número de inteiros da sequência: "))
    
    lista = []
    for i in range(n):
        num = int(input("Digite um inteiro da sequência: "))
        lista.append(num)   
    
    return lista 

#---------------------------------------------------------------------------

def intercala_duas_listas(listaA, listaB):
    ''' (list, list) -> list
 
    Recebe duas listas de inteiros: listaA e listaB.
    Em cada uma dessas listas, os inteiros estão em ordem crescente e não 
    existem repetições.
    Cria uma lista com os inteiros das duas listas, em ordem crescente e 
    sem repetições. Retorna a lista criada.
    '''
    
    lista = []
    
    compA = len(listaA)
    compB = len(listaB)
    
    i = 0  # i percorre os índices da listaA
    j = 0  # j percorre os índices da listaB
    
    while i < compA and j < compB:
        if listaA[i] == listaB[j]:
            lista.append(listaA[i])
            i += 1
            j += 1
        elif listaA[i] < listaB[j]:
            lista.append(listaA[i])
            i += 1
        else:
            lista.append(listaB[j])
            j += 1

    for k in range(i, compA, 1):
        lista.append(listaA[k])
 
    for k in range(j, compB, 1):
        lista.append(listaB[k])
 
    return lista

#-------------------------------------------------------------------
main()
