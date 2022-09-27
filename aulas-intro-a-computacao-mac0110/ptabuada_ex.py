"""
  arquivo: Tabuada.py
   --------------------
  Imprime 10 colunas correspondentes às tabuadas de  1 a 10
  Cada coluna i tem os valores correspondentes a
  1 * i = i,  2 * i = 2*i,  ...,  10 * i = 10*i
"""
# obs: juntei as duas versões


def main():
    tabuada()
    tabuada_resumida()


def tabuada():
    for linha in range(1, 11):
        print()
        for coluna in range(1, 11):
            valor = linha * coluna
            print(f"|{coluna} x {linha} = {valor}|", end=" ")


def tabuada_resumida():
    print("\n\n")
    for k in range(1, 11):
        print(k, end="  ")
    print()
    print('_'*27 + "___")

    for linha in range(1, 11):
        print()
        for coluna in range(1, 11):
            valor = linha * coluna
            print(f"|{valor}|", end=" ") 


main()
