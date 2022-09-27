# -*- coding: utf-8 -*-
'''
   Programa p37 --  p37_ocorr_dig.py
   
   Dado um inteiro positivo n, verificar quantas vezes cada um dos dígitos 
   0, 1,..., 9 ocorre em n. Usar obrigatoriamente uma função

     conta_dig(num, dig)

   que retorna o número de vezes que dig ocorre em num.


Ex: se n = 1345689088855433001119, a solução seria:

digito 0 ocorre 3 vezes
digito 1 ocorre 4 vezes
digito 2 ocorre 0 vezes
digito 3 ocorre 3 vezes
digito 4 ocorre 2 vezes
digito 5 ocorre 3 vezes
digito 6 ocorre 1 vezes
digito 7 ocorre 0 vezes
digito 8 ocorre 4 vezes
digito 9 ocorre 2 vezes

'''

def main():
    n = int(input("Digite o valor de n: "))
    dig = 0
    while dig <= 9:
        total = conta_dig(n,dig)
        print("digito", dig, "ocorre", total, "vezes em", n)
        dig = dig + 1
        
#-------------------------------       
def conta_dig(num,dig):
    ''' 
       (int, int) --> int   # significa que os parâmetros num e dig são inteiros;
                            # e a função retorna um número inteiro.
       Retorna um valor int correspondente a quantas vezes dig ocorre em num.
    '''
    conta = 0 
    while num > 0:
        if num % 10 == dig:
            conta = conta + 1
        num = num // 10
    return conta

#--------------------------
main()
    
