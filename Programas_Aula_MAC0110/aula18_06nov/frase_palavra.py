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
    frase = input("Digite uma frase: ")
    palavra = input("Digite uma palavra: ")

    print()
    print("Frase: '%s'" %(frase))
    print("Palavra: '%s'" %(palavra))


    comp_frase = len(frase)  # comprimento da frase 
    comp_pal = len(palavra)  # comprimento da palavra 

    cont = 0  # conta o numero de ocorrencias de palavra na frase
    
    ultimo = comp_frase - comp_pal 
    for i in range(ultimo + 1):  
        # verifica se tem uma ocorrencia de palavra
        # comecando na posicao de indice i da frase
        j = 0
        ocorre = True
        while (j < comp_pal and ocorre):
            if palavra[j] == frase[i+j]:
                j += 1
            else:
                ocorre = False
        if ocorre: 
            cont += 1

    print()
    print("A palavra ocorre %d vezes na frase." %cont)
   
#------------------------------------------------------------------
          
main()
