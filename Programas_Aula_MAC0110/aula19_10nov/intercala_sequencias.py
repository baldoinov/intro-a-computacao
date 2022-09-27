# -*- coding: utf-8 -*-
'''
   Arquivo: intercala_sequencias.py
   
   Dados dois inteiros positivos m e n, e duas sequências em ordem
   crescente, sem repetições, com m e n inteiros, respectivamente,
   determinar uma única sequência, contendo todos os elementos das
   sequências originais em ordem crescente e sem repetições. 
'''

def main():
    print("AVISO: Os inteiros em cada uma das sequências fornecidas pelo ")
    print("usuário devem estar em ORDEM ESTRITAMENTE CRESCENTE.")
    print()
    
    # Criar uma lista seq1 com os elementos da 1a. seq.
    m = int(input("Digite o número de elementos da 1a. sequência: "))
    seq1 = []    
    for i in range(m):
        num = int(input("Digite um inteiro da 1a. sequência: "))
        seq1.append(num)   
    
        
    # Criar uma lista seq2 com os n elementos da 2a. seq.

    n = int(input("Digite o número de elementos da 2a. sequência: "))
    seq2 = []
    for i in range(n):
        num = int(input("Digite um inteiro da 2a. sequência: "))
        seq2.append(num)
        
    print("\n Primeira sequencia: ")
    print(seq1)
    
    print("\n Segunda sequencia: ")            
    print(seq2)
          
    #  Criar uma lista seq com os elementos das listas seq1 e seq2,
    # em ordem estritamente crescente (sem repetições)
    seq = []   
    i = 0  # percorre a lista seq1
    j = 0  # percorre a lista seq2
    while i < m and j < n:
        if seq1[i] == seq2[j]:
            seq.append(seq1[i])
            i += 1
            j += 1
        elif seq1[i] < seq2[j]:          
            seq.append(seq1[i])
            i += 1
        else:
            seq.append(seq2[j])
            j += 1 

    while i < m:   # copia o restante de seq1 a partir de i 
        seq.append(seq1[i])
        i += 1

    while j < n:  # copia o restante de seq2 a partir de j
        seq.append(seq2[j])
        j += 1               
        
    print("\n Sequência resultante da intercalação das duas sequências.")
    print("Seus %d inteiros são: " %(len(seq)))  
    print(seq)

    print("\n Sequência (com %d inteiros) resultante da "
          "intercalação das duas sequências:" %(len(seq)))
    for num in seq:               #<========== Veja!!!
        print(num, end='  ')      #<=========  Veja !!
    
#........................................
main()
