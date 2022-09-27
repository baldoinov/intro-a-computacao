"""
    arquivo: tabela_triangular.py
    ------------------------
    Este programa imprime uma tabela triangular como a seguinte:

    0 
    0  1 
    0  1  2 
    0  1  2  3 
    0  1  2  3  4 
    0  1  2  3  4  5 
    0  1  2  3  4  5  6 
    0  1  2  3  4  5  6  7 
    0  1  2  3  4  5  6  7  8 
    0  1  2  3  4  5  6  7  8  9 
    0  1  2  3  4  5  6  7  8  9 10 

 """ 

 
def main():
    for linha in range(0, 11):
        print()
        for coluna in range(0, linha + 1):
            print(coluna, end=" ")

            
main()