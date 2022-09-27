# -*- coding: utf-8 -*-
'''
   -------------------------------------------------------
   ---------- Uso do operador lógico "or"(ou) ------------
   -------------------------------------------------------
   Programa P28a
   -------------
   Dados três números inteiros positivos, n, i e j, imprimir 
   em ordem crescente os n primeiros naturais que são 
   múltiplos ou de i ou de j ou de ambos.
   Por exemplo, para n=6, i=2 e j=3, a saída deverá ser:
    0    2    3   4    6    8
'''
'''
   solução 1
   Testa os números 0, 1, 2, ... verificando e imprimindo quais
   são múltiplos de i ou de j, até que n múltiplos sejam impressos. 
'''
# ------------------------------------------------------------------

def main():    
    print("\nImprime os n primeiros múltiplos de i ou de j")
    
    n = int(input("Digite um inteiro positivo para n: "))
    i = int(input("Digite um inteiro positivo para i: "))
    j = int(input("Digite um inteiro positivo para j: "))
    
    print("\nOs", n, "primeiros naturais múltiplos de", 
           i, "ou de", j, "são:\n")
     
    cont = 0     # conta quantos múltiplos já foram impressos
    nat = 0      # candidatos a múltiplos de i ou de j 
    while cont < n:
        if (nat % i == 0  or  nat % j == 0):
            # print(nat, end='  ')
            cont = cont + 1
        nat = nat + 1
    print()
# ------------------------------------------------------------------
main()
       
