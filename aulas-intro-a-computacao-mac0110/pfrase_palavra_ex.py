# -*- coding: utf-8 -*-

'''
   Arquivo: frase_palavra.py
   ------------------------

   Dadas duas sequencias de caracteres, a primeira representando uma frase
   e a segunda representando uma palavra, determinar o número de vezes que
   a palavra ocorre na frase.
   Exemplo:  
   frase: ANA, JANAINA E MARIANA GOSTAM DE BANANA E DE RABANADA. 
   palavra: ANA
   Temos que a palavra ocorre 6 vezes na frase.
'''

def main():
    print("Esse programa determina se uma palavra aparece em uma frase.")
    frase = str(input("Digite a frase (maiúscula e sem acentos): ")).upper()
    palavra = str(input("Digite a palavra procurada (maiúscula e sem acentos): ")).upper()

    comp_frase = len(frase)
    comp_palavra = len(palavra)
    ultimo = comp_frase - comp_palavra
    cont = 0
    
    for i in range(ultimo + 1):
        j = 0
        ocorre = True
        while j < comp_palavra and ocorre:
            if frase[i+j] == palavra[j]:
                j += 1
            else:
                ocorre = False
        if ocorre:
            cont += 1

    print()
    print(f"A palavra '{palavra}' ocorre {cont} vezes na frase dada.")
             

main()
