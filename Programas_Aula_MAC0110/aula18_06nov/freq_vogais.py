# -*- coding: utf-8 -*-
'''
   Dada uma frase, determinar a frequência relativa de
   vogais na frase.
'''

def main():
    frase = input("Digite uma frase: ")
    print("Frase lida: '%s'" %(frase))
    
    n = len(frase)
    cont = 0

    for i in range(n):
        if eh_vogal(frase[i]):
            cont += 1

    print ("\nFrequência relativa de vogais na frase = %d/%d = %f"
            %(cont, n, cont/n))  

#....................................................................

def eh_vogal(s):
    ''' (str) -> bool
    
    Recebe um caractere s e retorna True, se s for uma vogal,
    e False, em caso contrário.
    '''

    vogais = 'aeiouAEIOUáÁéÉ' # pode acrescentar outras vogais acentuadas
    
    n = len(vogais)
    achou = False
    i = 0
    while (i < n and not achou):
        if s == vogais[i]:
            achou = True
        else:
            i += 1
        
    return achou

#------------------------------------------------------------------------

main()
