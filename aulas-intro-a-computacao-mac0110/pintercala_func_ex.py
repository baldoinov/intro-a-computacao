'''
   Dados dois inteiros positivos m e n, e duas sequências em ordem 
   crescente, sem repetições, com m e n inteiros, respectivamente, 
   determinar uma única sequência, contendo todos os elementos das 
   sequências originais em ordem crescente e sem repetições. 
'''

def main():
   print("Esse programa intercala duas listas em ordem crescente, sem repetição.")
   print("Os inteiros fornecidos pelo usuário devem estar em ordem estritamente crescente.\n")

   m = int(input("Digite o tamanho da 1° lista: "))
   seq_1 = []
   for k in range(1, m+1):
      num = int(input(f"Digite o {k}° número da lista: "))
      seq_1.append(num)

   print()

   n = int(input("Digite o tamanho da 2° lista: "))
   seq_2 = []
   for j in range(1, n+1):
      nun = int(input(f"Digite o {j}° número da lista: "))
      seq_2.append(nun)

   i = 0
   j = 0
   seq_all = []

   while i < m and j < n:
      if seq_1[i] == seq_2[j]:
         seq_all.append(seq_1[i])
         i += 1
         j += 1
      elif seq_1[i] < seq_2[j]:
         seq_all.append(seq_1[i])
         i += 1
      else:
         seq_all.append(seq_2[j])
         j += 1
   
   for j in range(j, n):
      seq_all.append(seq_2[j])

   for i in range(i, m):
      seq_all.append(seq_1[i])

   print(f"Sequência resultante: {seq_all}")


main()
