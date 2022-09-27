# -*- coding: utf-8 -*-
'''
   Arquivo: seq_sem_repeticoes.py
   
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

           # verifica se num está na lista seq

           comp_seq = len(seq)    # comprimento da lista seq (*)         
           achou = False
           j = 0
           while (j < comp_seq and not achou):
               if num == seq[j]:
                   achou = True
               else:
                   j += 1
                     
           if not achou:
               seq.append(num)

     print()
     print("Sequência sem repetições: ", seq)
     print("Comprimento da sequência de termos distintos: ", len(seq))


#----------------------------------------------------------------
main()
