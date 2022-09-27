'''
   Arquivo: soma_matrizes.py
   Dada uma matriz A (mxn) e uma matriz B (mxn), ambos com núemros inteiros,
   calcular e imprimir a matriz C = A+B.
   Inicialmente, ler os valores de n e m, depois ler as entradas de A e depois as de B.
   Fazer uso de funcoes para leitura de matriz, impressao de matriz, e para calcular a soma.
'''
def main():
    print("Vamos realizar uma soma de matrizes.\n"
          "Lembre-se que as matrizes devem ser da mesma ordem.\n")

    a = cria_matriz(1)
    b = cria_matriz(2)
    z = soma_matriz(a, b)

    print("A soma das matrizes é:")
    imprime_soma_matriz(a, b, z)

def cria_matriz(k):
    '''
    (int) -> list
    Essa função cria uma matriz e a devolve como uma lista de listas.
    '''
    m = int(input(f"Insira o número de linhas da {k}° matriz: "))
    n = int(input(f"Insira o número de colunas da {k}° matriz: "))
    print()
    matriz = []
    
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            num = int(input(f"Insira o elemento {i}x{j} da matriz: "))
            linha.append(num)
        matriz.append(linha)
    print()
    return matriz


def soma_matriz(a, b):
    '''
    (list, list) -> list
    '''
    m = len(a)
    n = len(a[0])
    matriz = []

    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(a[i][j] + b[i][j])
        matriz.append(linha)
    return matriz
    

def imprime_soma_matriz(a, b, z):
    '''
    (list, list, list) -> NoneType
    Imprime três matrizes de forma alinhada.
    '''
    m = len(a)
    n = len(a[0])
    listas = [a, b, z]

    for i in range(m):
        for j in range(n-1):
            print("|%d%3d| + |%d%3d| == |%d%3d|" %(a[i][j], a[i][j+1], b[i][j], b[i][j+1], z[i][j], z[i][j+1]), end="")
        print()
    print()
        

main()