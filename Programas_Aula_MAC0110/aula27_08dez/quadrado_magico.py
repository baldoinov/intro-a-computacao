
# -*- coding: utf-8 -*-

'''
   Arquivo: quadrado_magico.py
   -------------------------------------

        Dada uma matriz inteira A (nxn), verifica se A 
	é um quadrado mágico.

	Dizemos que uma matriz quadrada inteira é um quadrado mágico
	se a soma dos elementos de cada linha,
	a soma dos elementos de cada coluna e
	a soma dos elementos das diagonais principal e secundária
	são todas iguais.

         
       Exemplo: a matriz dada a seguir é um quadrado mágico de ordem 3.

                 8    0   7        ===>        1    2    3   4   5   6   7    8   9
                 4    5   6                          
                 3   10   2       
'''
                 

def main():

    nomeArqEntrada = input("Digite o nome de um arquivo de entrada: ")
    arqEntra = open(nomeArqEntrada, 'r')
 
    nomeArqSaida = input("Digite o nome de um arquivo para saida: ")
    arqSai =  open(nomeArqSaida, 'w')
                 
    
    # linha = arqEntra.readline()  # lê a primeira linha do arquivo (que tem dois números separados por pelo menos um branco)
    #  lista = linha.split()        # lista = ['3', '4']
    # nlin = int(lista[0])         # nlin = int('3') = 3    int transforma a string '3' no inteiro 3
    # ncol = int(lista[1])         # ncol = int('4') = 4
   

    n = int(input("De o numero de linhas da matriz:"))
    nlin = ncol = n 

    A = []
    for i in range(nlin):
        linha = arqEntra.readline()  # No exemplo, quando i = 0 no arquivo de entrada dados.txt temos 1   2   3   4   5 
        lista = linha.split()        # No exemplo, quando i = 0, obtemos lista =['1', '2', '3', '4', '5']

        listaA = []
        for j in range(ncol):
            listaA.append(int(lista[j]))  # aqui cada string em lista[j] é transformada num inteiro e concatenada a listaA
        A.append(listaA)

    print("Matriz A =", A)

    

    arqSai.write("\nMatriz A tem  %d linhas e %d colunas\n\n" %(nlin, ncol))
    for i in range(nlin):
        arqSai.write("\t") 
        for j in range(ncol):
             arqSai.write("%4d   " %(A[i][j]))  ### Veja no arquivo saida.txt o que o formato %4d  produziu 
        arqSai.write("\n")

     
    magico = True
    
    # Teste das linhas de A   
    soma = sum(A[0])   #<===========A[0] = [ 8, 0 , 7 ]  ---  sum(lista)
    print("soma = ", soma)

    for i in range(1, n):
        if sum(A[i]) != soma:
            magico = False

    # Teste das colunas
    j = 0
    while (j < n and magico):
           somacol = 0
           for i in range(n):
               somacol = somacol + A[i][j]
           if (somacol != soma):
               magico = False
           j += 1
         
                
    # Teste da diagonal principal
    while(magico):
        somadiag = 0 
        for i in range(n):
             somadiag += A[i][i]
        if somadiag != soma:
             magico = False
        break
    

    # Teste da diagonal secundaria
    while(magico):
        somadiag_sec = 0 
        for i in range(n):
             somadiag_sec += A[i][n-i-1]
        if somadiag_sec != soma:
           magico = False
        break
         
    if magico:
        print("A matriz A é um quadrado mágico")
    else:
        print("A matriz A não é um quadrado mágico")
        
    
#-----------
main()


   
        
        
