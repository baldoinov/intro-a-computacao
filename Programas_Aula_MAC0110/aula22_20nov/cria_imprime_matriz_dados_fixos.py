
'''
  arquivo:  cria_imprime_matriz_dados_fixos.py 
   
  Construir uma matriz inteira com m linhas e n colunas,
  cujas entradas devem ser todas iguais um valor dado pelo 
  usuário.

  Ler m, n e valor.

  Imprimir a matriz construída (linha a linha)

'''


def main():

    m = int(input("Digite o numero de linhas da matriz:"))
    n = int(input("Digite o numero de colunas da matriz:"))
                   
    print ("imprime uma matriz %d por %d  cujos valores sao iguais a um dado valor" %(n, m))

    valor = int(input("Que valor a matriz deve conter?:"))
    
    b = cria_matriz_inicializada(m, n, valor)

    imprime_matriz(b)
    
    # d = cria_matriz_inicializada(5, 6, 8)

    # imprime_matriz(d)
    
# -------------

def cria_matriz_inicializada(nlin, ncol, valor):
    '''(int, int, valor) --> matriz 
       Cria e retorna uma matriz com nlin linhas e ncol colunas
       em que cada elemento é igual ao valor dado.
    '''
    matriz = [] # lista vazia
    
    linha = [valor] * ncol  # cria uma linha (lista) com um total de ncol entradas iguais a valor

             # linha = [valor, valor, valor,.....]
           
    print("linha = ",  linha)
    
    for i in range(nlin):
          matriz.append(linha)
          
    #print(matriz)
    return matriz

#----------------
def imprime_matriz(c):
    '''
     (matriz) --> Nonetype
     Recebe e imprime uma matriz de inteiros (linha a linha) 
    ''' 
    nlin = len(c)
    ncol = len(c[0])

    for i in range(nlin):
        for j in range(ncol):
            print ("%5d" %(c[i][j]), end=' ') ## formato para numeros de poucos digitos; mudar, se necessario.
        print()    
#--------------------------------------------------

main()            
