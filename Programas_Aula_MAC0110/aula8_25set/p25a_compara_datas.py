"""
   Escreva um programa que determina a data cronologicamente maior
   entre duas datas fornecidas pelo usuário. Cada data deve ser 
   fornecida por três números inteiros, onde o primeiro representa 
   um dia, o segundo um mês e o terceiro um ano.
"""
#  Solução 1: Sem o uso de operadores lógicos
# -------------------------------------------------------------------

def main():
    # Primeira data.
    d1 = int(input("Dia: "))
    m1 = int(input("Mês: "))
    a1 = int(input("Ano: "))
    # Segunda data.
    d2 = int(input("Dia: "))
    m2 = int(input("Mês: "))
    a2 = int(input("Ano: "))
    print()
    
    if a1 > a2:
        print("Data1 é maior!")
    elif a1 == a2:
        if m1 > m2:
            print("Data1 é maior!")
        elif m1 == m2:
            if d1 > d2:
                print("Data1 é maior!")
            elif d1 == d2:
                print("Datas são iguais!")
            else:
                print("Data2 é maior!")
        else:
            print("Data2 é maior!")
    else:
        print("Data2 é maior!")

# -------------------------------------------------------------------
main()
