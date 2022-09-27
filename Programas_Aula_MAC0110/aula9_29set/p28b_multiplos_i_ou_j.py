# -*- coding: utf-8 -*-
'''
   -------------------------------------------------------
   ---------- Uso do operador lógico "or" (ou) ------------
   -------------------------------------------------------
   Programa P28b
   -------------
   Dados três números inteiros positivos, n, i e j, imprimir 
   em ordem crescente os n primeiros naturais que são 
   múltiplos ou de i ou de j ou de ambos.
   Por exemplo, para n=6, i=2 e j=3 a saída deverá ser:
    0    2    3   4    6    8
'''
'''
   Solução 2  (Compare com Program P28a):
   Mais elaborada. Faz menos iterações que a solução anterior.xs
   A cada iteração imprime um múltiplo de i ou de j. 
'''
# ------------------------------------------------------------

def main():
    print("Imprime os n primeiros múltiplos de i ou de j.")
    
    n = int(input("Digite um inteiro positivo para n: "))
    i = int(input("Digite um inteiro positivo para i: "))
    j = int(input("Digite um inteiro positivo para j: "))
    
    print("\nOs", n, "primeiros naturais múltiplos de", 
           i, "ou de", j, "são:\n")
     
    multi = 0     # múltiplos de i
    multj = 0     # múltiplos de j
    cont = 0      # conta quantos múltiplo já foram impressos
     
    while cont < n:
        if multi < multj:
            #print(multi, end='  ')
            multi = multi + i
        elif multj < multi:
            #print(multj, end='  ')
            multj = multj + j
        else:    # multi == multj
            #print(multj, end='  ')
            multi = multi + i
            multj = multj + j
            
        cont = cont + 1
        
    print()
# ---------------------------------------------------------------
main()

        
        
