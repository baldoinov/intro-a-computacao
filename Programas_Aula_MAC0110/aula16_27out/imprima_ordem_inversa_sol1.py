# -*- coding: utf-8 -*-
'''
   Arquivo: imprima_ordem_inversa_sol1.py
   ---------------------------------

   Dados um inteiro positivo n e uma sequência de n inteiros,
   imprimi-los na ordem inversa à da leitura.

Solucao 1:

'''

def main():
    n = int(input("Digite o numero de elementos da sequencia: "))

    x = []  # cria uma lista vazia 

    for i in range(n):
        num = int(input("Digite um termo da sequencia:"))
        x += [num]  # x = x + [num]      concatena num no final da lista x 
                    # tem outra forma equivalente (que tem o mesmo efeito) - veja abaixo
                    # Ex: se for dado num = 5,2,8,4,1, criamos x =[5, 2, 8, 4, 1]
    print("x =", x)  
    print(x)
    
    for i in range(n):
        print(x[n-1-i], end ='  ') # imprime os valores na mesma linha 
        
    print("\n")
    
    for i in range(n-1,-1, -1):
        print(x[i])        # imprime cada valor numa nova linha 

#-----------------
main()


