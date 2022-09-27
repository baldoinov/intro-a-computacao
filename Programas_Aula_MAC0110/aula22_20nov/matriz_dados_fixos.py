'''
  arquivo:  matriz_dados_fixos.py 
   
  Construir uma matriz inteira com m linhas e n colunas,
  cujas entradas devem ser todas iguais um valor dado pelo 
  usuário.

  Ler m, n e valor.

  Imprimir a matriz construída.

'''


def main():

    m = int(input("Digite o numero de linhas da matriz:"))
    n = int(input("Digite o numero de colunas da matriz:"))
                   
    print ("imprime uma matriz %d por %d  cujos valores sao iguais a um dado valor", n, m)

    valor = int(input("Que valor a matriz deve conter?:"))
    
    b = cria_matriz(n, m, valor)

    print(b)
# --------------

def cria_matriz(nlin, ncol, valor_inicial):
    
    '''(int, int, valor) --> matriz listas de listas
       Cria e retorna uma matriz com nlin linhas e ncol colunas,
       e inicialize esta matriz com o valor valor_inicial
    '''
    matriz = [] # lista vazia
    linha = [valor_inicial] * ncol  # cria uma linha (lista) com um total de ncol entradas iguais a valor_incial

    print("linha = ",  linha)
    
    for i in range(nlin):
          matriz.append(linha)

    return matriz

#-------------
main()
