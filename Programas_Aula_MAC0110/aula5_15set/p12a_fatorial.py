
 # ----------------------------------
 # Programa 12a  --  p12a_fatorial.py
 # ---------------------------------
 # Este programa recebe um inteiro não-negativo n e calcula o fatorial de n.
 # Definição de fatorial de n, denotado por n!
 #
 # 0! = 1
 # n! = n * (n-1)! = n * (n-1) * (n-2) * ... * 2 * 1,   se n > 0
 # ................................................

def main():
    n = int(input("Digite um número inteiro não-negativo: "))
    fat = 1
    k = 2
    while k <= n:
        fat = fat * k
        k = k + 1
        
    print("\n O fatorial de", n, "é igual a", fat)
    print()
# .............
      
main()      
