+# -*- coding: utf-8 -*-
'''
   Arquivo: seq_sem_repeticoes_func.py
   
   Dados um inteiro positivo n e uma sequência de n números inteiros,
   construir uma sequência sem repetições (dos números dados). 
   
'''

def main():
     n = int(input("Digite o numero de elementos da sequência: "))

     # Ler cada numero dado, e
     # inseri-lo na lista seq se ele não estiver na lista
     
     seq = []   # cria a lista (vazia) seq
     
     for i in range(n):   # i variando de 0 a n-1 
           num = int(input("Digite um inteiro da sequência: "))
           if not pertence_lista(num, seq):
               seq.append(num)

     print()
     print("Sequência sem repetições: ", seq)
     print("Comprimento da sequência de termos distintos: ", len(seq))     

#----------------------------------------------------------------

def pertence_lista(item, lista):
    ''' (objeto, list) -> bool 

    Recebe um objeto item e uma lista lista.
    Retorna True se item ocorre na lista,
    caso contrário, retorna False.
    '''
    comp = len(lista)  # comprimento de lista 
    i = 0
    while i < comp:
        if item == lista[i]:
            return True
        else:
            i += 1
      
    return False 
#-------------------------------------------------------------

main()

