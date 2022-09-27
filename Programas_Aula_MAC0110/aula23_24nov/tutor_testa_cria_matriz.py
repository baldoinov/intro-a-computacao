def main():
    m = int(input("Digite o numero de linhas da matriz: "))
    n = int(input("Digite o numero de colunas da matriz: "))
    matrizA = cria_matriz(m, n, 0)
    print("\n\nLista com os elementos da matriz lida:\n", matrizA)
    print()
    imprime_matriz(matrizA)
    matrizA[0][n-1] = -m
    print("\nPosicao [0][%d] da matriz foi atualizada com %d." %(n-1, -m))   
    print("\nLista com os elementos da matriz apos a alteracao:\n", matrizA)
    imprime_matriz(matrizA)  
    
def cria_matriz(nlin, ncol, valor):
    matriz = []

    for i in range(nlin):
        linha = []
        for j in range(ncol):
            linha.append(valor)    
        matriz.append(linha)
    return matriz
    
def imprime_matriz(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    print("\nMatriz com %d linhas e %d colunas\n" %(nlin, ncol))
    for i in range(nlin):
        for j in range(ncol):
            print("%6d" %(matriz[i][j]), end='')
        print()
    print()

main()

'''
http://pythontutor.com/visualize.html#code=def%20main%28%29%3A%0A%20%20%20%20m%20%3D%20int%28input%28%22Digite%20o%20numero%20de%20linhas%20da%20matriz%3A%22%29%29%0A%20%20%20%20n%20%3D%20int%28input%28%22Digite%20o%20numero%20de%20linhas%20da%20matriz%3A%22%29%29%0A%20%20%20%20matrizA%20%3D%20cria_matria%28m,n,0%29%0A%20%20%20%20print%28%22%5Cn%5CnLista%20com%20os%20elementos%20da%20matriz%20lida%3A%5Cn%22,%20matrizA%29%0A%20%20%20%20print%28%29%0A%20%20%20%20imprime_matriz%28matrizA%29%0A%20%20%20%20matrizA%5B0%5D%5Bn-1%5D%20%3D%20-m%0A%20%20%20%20print%28%22%5CnPosicao%20%5B0%5D%5B%25d%5D%20da%20matriz%20foi%20atualizada%20com%20%25d.%25%28n-1,-m%29%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20print%28%22%22%5CnLista%20com%20os%20elementos%20da%20matriz%20apos%20a%20alteracao%3A%5Cn%22,%20matrizA%29%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20imprime_matriz%28matrizA%29%0A%20%20%20%20%0Adef%20cria_matriz%28nlin,%20ncol,%20valor%29%3A%0A%20%20%20%20matriz%20%3D%5B%5D%0A%20%20%20%20for%20i%20in%20range%28nlin%29%3A%0A%20%20%20%20%20%20%20%20linha%20%3D%20%5B%5D%20%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%28ncol%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20linha.append%28valor%29%0A%20%20%20%20%20%20%20%20matriz.append%28linha%29%0A%20%20%20%20return%20matriz%0A%20%20%20%20%0Adef%20imprime_matriz%28matriz%29%3A%0A%20%20%20%20nlin%20%3D%20lek
n%28matriz%29%0A%20%20%20%20ncol%20%3D%20len%28matriz%5B0%5D%29%0A%20%20%20%20print%28%22%5CnMatriz%20com%20%25d%20linhas%20e%20%25d%20colunas%5Cn%22%20%25%28nlin,%20ncol%29%29%0A%20%20%20%20for%20i%20in%20range%28nlin%29%3A%20%0A%20%20%20%20%20%20%20%20for%20j%20in%20range%28ncol%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22%256d%22%20%25%28matriz%5Bi%5D%5Bj%5D%29,%20end%3D''%29%0A%20%20%20%20%20%20%20%20print%28%29%0A%20%20%20%20print%28%29%0A%20%20%20%20%0Amain%28%29%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''
