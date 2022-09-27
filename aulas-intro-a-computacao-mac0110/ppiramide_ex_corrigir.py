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
   print("Pirâmide de 10 linhas.\n")
   linhas = 0
   brancos = 9

   for linhas in range(1,11):
      print()
      for i in range(0, brancos):
         print("   ", end="")
      for coluna in range(1, 2 * linhas):
         print(f"{coluna:3d}")
      print("\n")
      brancos -= 1


main()       
