
 #-----------------------------------
 # Programa 12b  -- p12b_fatorial.py
 # ---------------------------------
 # Este programa recebe um inteiro não-negativo n e calcula o fatorial de n.
 # Definição de fatorial de n, denotado por n!
 #
 # 0! = 1
 # n! = n * (n-1)! = n * (n-1) * (n-2) * ... * 2 * 1, se n > 0
 # ................................................
 
def main():
  
  n = int(input("Digite um numero inteiro nao-negativo: "))

  print("Calculo do fatorial de ", n)  # Isso foi feito antes de alterar n
  
  fat = 1
  while n > 0:    
      fat = fat * n
      n = n - 1            # perdemos o valor de n (dado originalmente)
  print("Resposta = ", fat)      
# .................................
main()      
