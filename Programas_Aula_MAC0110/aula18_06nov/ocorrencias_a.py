# -*- coding: utf-8 -*-

'''
   Dada uma frase, determinar o numero de ocorrencias
   da letra 'a' ou 'A' na frase.
'''

def main():
    frase = input("Digite uma frase: ")
    
    print("Frase lida:", frase)
    print("Frase lida: '%s'" %(frase))
    
    n = len(frase)  # len vem de length (que significa comprimento)
    print("comprimento da frase =", n)
    
    conta = 0
    
    for i in range(n):
        if frase[i] == 'a' or frase[i] == 'A':
            conta += 1

    print()
    print ("A letra 'a' (ou 'A') ocorreu %d vezes na frase." %(conta))
    
#-----------------------------------------------------------------------

main()
