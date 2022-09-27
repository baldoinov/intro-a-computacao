'''
  arquivo:  cria_imprime_matriz_dados_fixos.py 
   
  Construir uma matriz inteira com m linhas e n colunas,
  cujas entradas devem ser todas iguais um valor dado pelo 
  usuário.

  Ler m, n e valor.

  Imprimir a matriz construída (linha a linha)

'''

def main():
    print("Esse programa cria uma matriz com m linhas e n colunas com todos os elementos iguais.\n")
    m = int(input("Insira o número de linhas: "))
    n = int(input("Insira o número de colunas: "))
    k = int(input("Insira o valor desejado: "))
    print()

    b = cria_matriz(m, n, k)

    print()

    imprime_matriz(b)


def cria_matriz(m, n, k):
    '''
    (int, int, int) -> list
    '''
    linha = [k] * n
    matriz = []
    for i in range(m):
        matriz.append(linha)
    return matriz


def imprime_matriz(lista):
    '''
    (list) -> NoneType
    '''
    m = len(lista)
    n = len(lista[0])
    for i in range(m):
        for j in range(n):
            print("%6d" %(lista[i][j]), end="")
        print()
    print()


main()
