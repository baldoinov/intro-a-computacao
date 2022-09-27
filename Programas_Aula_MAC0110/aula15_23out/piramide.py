
'''
    arquivo: piramide.py
    ------------------------
    Este programa imprime uma pirâmide (de 10 linhas) como a seguinte:
  
                                1

                             1  2  3

                          1  2  3  4  5

                       1  2  3  4  5  6  7

                    1  2  3  4  5  6  7  8  9

                 1  2  3  4  5  6  7  8  9 10 11

              1  2  3  4  5  6  7  8  9 10 11 12 13

           1  2  3  4  5  6  7  8  9 10 11 12 13 14 15

        1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17

     1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
     
'''

def main():
    print("Piramide de 10 linhas \n")
    num_brancos = 9  # para pular esse total de  espaços em branco em cada linha
                    # antes de começar a imprimir
    for linha in range(1, 11):  
        for i in range(0, num_brancos): 
                print("   ", end='') # pula num_brancos espaços (corresp. 3 posições) 
        for coluna in range (1, 2*linha):
                print("%3d" %(coluna), end= '')
        print("\n")
        num_brancos = num_brancos - 1
#. . . . . . . . . . . . . . . . . . . 

main()

# OBS:
# ("   ") corresponde a 3 posições em branco 
# ("...") 
