# -*- coding: utf-8 -*-

'''
   Arquivo: intercala_sequencias_dados.py
   
   Dados dois inteiros positivos m e n, e duas sequências em ordem
   crescente, sem repetições, com m e n inteiros, respectivamente,
   determinar uma única sequência, contendo todos os elementos das
   sequências originais em ordem crescente e sem repetições. 

   OBS: Para executar na linha de comando com o arquivo dados.txt, dê o comando:

   python intercala_sol_dados.py < dados.txt

   Se quiser que a saida (os print) sejam gravados num arquivo (por exemplo, saida.txt), dê o comando:

   python intercala_sol_dados.py < dados.txt  > saida.txt

   OBS: Note o direcionmento: dados.txt é a entrada; e saida.txt é o nome do arquivo de saida.

'''

def main():
    print("AVISO: Os inteiros em cada uma das sequências fornecidas pelo ")
    print("usuário devem estar em ORDEM ESTRITAMENTE CRESCENTE.")
    
    # Criar uma lista seq1 com os elementos da 1a. seq.
    m = int(input())
    seq1 = []    
    for i in range(m):
        num = int(input())
        seq1.append(num)   
    
        
    # Criar uma lista seq2 com os n elementos da 2a. seq.

    n = int(input())
    seq2 = []
    for i in range(n):
        num = int(input())
        seq2.append(num)


    print() 
    print("Primeira sequencia: ")
    print(seq1)
    print() 
    print("Segunda sequencia: ")            
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
        
    print()
    print("Sequência resultante da intercalação das duas sequências."
          "Seus %d inteiros são: " %(len(seq)))  
    print(seq)
    print()
    
    print("Sequência (com %d inteiros) resultante da "
          "intercalação das duas sequências:" %(len(seq)))
    for num in seq:               #<========== Veja!!!
        print(num, end='  ')      #<=========  Veja!!! 
    print()
#........................................
main()
