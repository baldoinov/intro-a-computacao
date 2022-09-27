'''
  Programa p38   --- p38_fatorial.py

  Escreva um programa que calcula o fatorial de 0, 5, 17 e 20. 
  O programa deve definir uma função chamada fatorial e fazer uso dela.
'''

def main():
    # testes da função fatorial
    print("0! =", fatorial(0))
    print("5! =", fatorial(5))
    print("17! =", fatorial(17))
    print("20! =", fatorial(20))

#-----------------------------------------------------
def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k >= 0  e retorna o valor de k!
    '''

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # o mesmo que cont = cont + 1
        k_fat *= cont   # o mesmo que k_fat = k_fat * cont

    return k_fat

#-----------------------------------------------------
main()
