'''
  arquivo:  cria_matriz.py 
   
  Construir uma matriz inteira com m linhas e n colunas,
  cujas entradas são dadas linha a linha (em cada linha na ordem das colunas).

  Ler m, n  e os valores da matriz.

  Imprimir a matriz construída.

'''

def main():
    print("Esse programa cria uma matriz com m linhas e n colunas.\n")
    m = int(input("Insira o número de linhas: "))
    n = int(input("Insira o número de colunas: "))
    print()
    b = cria_matriz(m, n)       #[[1, 0], [0, 1]]
    print()

    for i in range(len(b)):
        for j in range(len(b[0])):
            print("%5d" %(b[i][j]), end="")
        print()
    print()
            

def cria_matriz(m, n):
    '''
    (int, int) -> (list)
    Recebe dois inteiros, m e n, e retorna uma matriz com m linhas e n colunas.
    '''
    matriz = []

    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            num = int(input(f"Digite um inteiro para a posição {i}x{j}: "))
            linha.append(num)
        matriz.append(linha)
    return matriz


main()
