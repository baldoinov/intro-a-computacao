# -*- coding: utf-8 -*-
'''
   Dada uma frase, determinar a frequência relativa de
   vogais na frase.
'''

def main():
    print("Esse programa determina a frequência de vogais em uma frase.\n")
    frase = str(input("Digite a frase: ")).upper()
    vogais = "AÁÀÃÂEÉÈÊIÍÌÎOÓÒÕÔUÚÙÛÜ"
    cont = 0

    for i in range(len(frase)):
        if frase[i] in vogais:
            cont += 1
    
    print(f"A frase dada apresenta {cont} vogais.")


main()
