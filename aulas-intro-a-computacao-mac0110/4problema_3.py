"""
PROBLEMA 3 - Apostas na roleta (números de 0 a 36)
========
   Dados um inteiro positivo n, simular n apostas na roleta, 
   escolhendo n vezes um  número inteiro aleatório entre 0 e 36
   (para isso, usar um gerador de números aleatorios). 
   Para essas n jogadas, determinar 
   (a) o número de ocorrencias de cada um dos 37 valores,
   (b) quais números ocorrem o maior número de vezes.
"""
import random as r
r.seed(1)


def main():
   print("Esse programa trabalha com apostas na roleta.\n")
   n = int(input("Insira o número de experimentos: "))

   ocor_num = [0] * 37
   for i in range(n):
      num = r.randint(0, 36)
      ocor_num[num] += 1
   
   freq_max = max(ocor_num)

   for i in range(37):
      print(f"O número {i} ocorre {ocor_num[i]} vezes.")
   for i in range(37):
      if ocor_num[i] == freq_max:
         print(f"O número que ocorre mais vezes é {i}")


main()