'''
   Dada uma matriz inteira com n linhas e n colunas,
   verificar se ela é simétrica. 
   Exemplo: a matriz a seguir é simétrica.
   
   Matriz com 4 linhas e 4 colunas

     1     2     3     4
     2     0     5     8
     3     5     6     7
     4     8     7     0
 
   Esta matriz será representada como uma lista de listas:
   [ [1, 2, 3, 4], [2, 0, 5, 8], [3, 5, 6, 7], [4, 8, 7, 0] ]
   
'''

def main():
    print("Esse programa verifica se uma matriz é simétrica.\n"
          "Vamos criar a matriz: \n")

    matriz = []
    p = int(input("Digite o número de linhas (=colunas) da matriz: "))
    print()
    
    for m in range(1, p+1):
        linha = []
        for n in range(1, p+1):
            num = int(input(f"Digite o elemento {m}x{n}: "))
            linha.append(num)
        matriz.append(linha)
    
    print("\nA matriz dada foi a seguinte: \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"{matriz[i][j]}", end=" ")
        print()
    print()

    simetrica = True
    i = 1
    while i < n:
        j = 0
        while j < i and simetrica:
            if matriz[i][j] != matriz[j][i]:
                simetrica = False
            else:
                j +=1
        i += 1  

    if simetrica:
        print("A matriz dada é simétrica.")
    else:
        print("A matriz dada não é simétrica.")


main()
