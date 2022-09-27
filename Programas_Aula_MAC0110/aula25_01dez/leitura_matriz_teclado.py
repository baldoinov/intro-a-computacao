

# arquivoL leitura_matriz_teclado.py
#
# leitura de uma matriz fornecendo os valores pelo teclado
# Vamos fornecer pelo teclado as dimensoes da matriz, e depois as linhas da matriz
#
# (Na verdade, desse jeito, pode-se ler linhas de diferentes comprimentos)


print("OBS: Todos os dados devem ser dados separados por pelo menos um espaço em branco.")

lincol= list(map(int, input("Digite o numero de linhas seguido do no. de colunas da matriz: ").split()))
nlin = lincol[0]
ncol = lincol[1] # nem vamos usar esse valor

matriz = []
print("De as entradas da matriz, cada linha por vez: ")

for i in range(nlin):
    print("De as entradas da linha", i, "da matriz")
    linha  = list(map(int, input().split())) #[ 1, 2, 3, 4]
    matriz.append(linha)

    
print("matriz = ", matriz)

### E se quiséssemos colocar uma moldura de -1 em torno dessa matriz???

                                     
                                 LAB
  
     1  2  3  4          -1  -1  -1  -1  -1  -1
     5  6  7  8   ->     -1   1   2   3   4  -1
     9  9  9  9          -1   5   6   7   8  -1
                         -1   9   9   9   9  -1
                         -1  -1  -1  -1  -1  -1 


##############################################################################
