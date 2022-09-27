# 

'''
   arquivo: Exemplo_Entrada_Saida_arquivo.py

   Programa para ilustrar como fazer a leitura de dados de um arquivo,
   e também como salvar os resultados em outro arquivo. 
   Este programa lê uma matriz (de um arquivo) e salva
   (em outro arquivo).

    --  O arquivo de entrada de dados contém na primeira linha
        o número de linhas e o número de colunas de uma matriz. Cada uma das linhas
        seguintes desse arquivo contém os números inteiros de cada uma das linhas da matriz.

    --  O arquivo de saída deve ter os dados da matriz
        (no formato bidimensional).
'''

def main():
    nomeArqEntrada = input("Digite o nome de um arquivo de entrada: ")

    # Por exemplo, vc pode fornecer o nome dados.txt
    # Neste caso, vc deve ter no mesmo diretorio um arquivo com esse nome
    # e com os dados que vc quer ler.
    # Por exemplo, se vc quer fornecer uma matriz 4x5 como abaixo,
    # vc pode fornecer os valores 4 e 5 (número de linhas e número de colunas) na primeira linha,
    # e a seguir cada uma das 4 linhas da matriz. (O alinhamento não precisa estar perfeito na entrada.)
    #   4   5
    #   1     2     3     4      5
    #   6     7     8     9    10
    #  11    12    13   14    15
    #  16   17    18    19     20 

    arqEntra = open(nomeArqEntrada, 'r')
    # open:  abre o arquivo nomeArqEntrada para leitura ("r = read")

    nomeArqSaida = input("Digite o nome de um arquivo para saida: ")
    
    # Por exemplo, vc pode fornecer o nome saida.txt
    # Tal arquivo vai ser criado durante a execucao do programa.
    # Quando terminar a execução, no diretório vai aparecer um
    # arquivo chamado saida.tx  (Verifique se isso ocorre.)

    arqSai =  open(nomeArqSaida, 'w')
    # open:  abre o arquivo nomeArqSaida para escrita ("w = write")
           
    # readline() -  lê a linha corrente de um arquivo e
    #               retorna uma string (cadeia) com o conteúdo dessa linha
    # OBS: o caractere de nova linha é incluído no final da string
    
    linha = arqEntra.readline()  # lê a primeira linha do arquivo (que tem dois números, no ex, 4 e 5)
    lista = linha.split()        # lista = ['4', '5']
    nlin = int(lista[0])         # nlin = int('4') = 4    int transforma a string '4' no inteiro 4
    ncol = int(lista[1])         # ncol = int('5') = 5
    
    # imprimindo linha e lista (na tela) só para exemplificar (e conferir):
    
    print()
    print("> dados da linha:", linha)
    print("> lista = ", lista)
    print("> num linhas =", nlin, "  num colunas =", ncol)

    # cada uma das seguintes nlin linhas do arquivo contém os números
    # da linha correspondente da matriz
    
    matrizA = []
    for i in range(nlin):
        linha = arqEntra.readline()  # No exemplo, quando i = 0 no arquivo de entrada dados.txt temos 1   2   3   4   5 
        lista = linha.split()        # No exemplo, quando i = 0, obtemos lista =['1', '2', '3', '4', '5']

        # imprimindo linha e lista (na tela) só para exemplificar
        print()
        print("> dados da linha", i,  "--->", linha)
        print("> lista = ", lista)
        
        listaA = []
        for j in range(ncol):
            listaA.append(int(lista[j]))  # aqui cada string em lista[j] é transformada num inteiro e concatenada a listaA
        matrizA.append(listaA)

    arqEntra.close()  # para fechar o arquivo de entrada dados.txt

    print("\nMatriz dada:")
    
    imprime_matriz(matrizA)   # imprime na tela (veja a funcao imprime_matriz()

    # salvar no arquivo a matriz lida:
    
    arqSai.write("\nMatriz com %d linhas e %d colunas\n\n" %(nlin, ncol))
    for i in range(nlin):
        arqSai.write("\t") 
        for j in range(ncol):
             arqSai.write("%4d   " %(matrizA[i][j]))  ### Veja no arquivo saida.txt o que o formato %4d  produziu 
        arqSai.write("\n")
        
     #  faça outro teste usando o formato "%04d   "
    
    arqSai.close()   # para fechar o arquivo de saida saida.txt

#-----------------------------------------------------------------
    
def imprime_matriz(matriz):
    ''' (matriz) ->

    Recebe e imprime (na tela) uma matriz de inteiros.
    '''
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    print("\nMatriz com %d linhas e %d colunas\n" %(nlin, ncol))
        
    for i in range(nlin):
        # imprimir os elementos da i-esima linha de matriz 
        for j in range(ncol):
            print("%6d" %(matriz[i][j]), end='')
        print()
    print()
#---------------------------------------------------------------
main()
