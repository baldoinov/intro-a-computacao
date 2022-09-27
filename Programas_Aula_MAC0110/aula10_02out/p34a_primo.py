# -*- coding: utf-8 -*-
'''
   Programa p34a  ------------p34a_primo.py
   
   Dado n (inteiro positivo), testar se n é primo.
   Def: um inteiro positivo n é primo se tem exatamente dois divisores: o 1 e o próprio n.
   (1 não é primo; 2 é primo; 3 é primo; 4 não é primo; 5 é primo,...)
'''
'''
def main():
    #  n	    número a ser testado se é primo
    #  d	    candidato a divisor 
    #  is_prime	    variável booleana (True/False) p/  indicar se n é primo ou não    
    #               Queremos: is_prime tem valor True  <==>  n é primo 
  
    n = int(input("Digite um numero inteiro positivo (n)  ===> "))
    print("Inteiro dado = %d \n" %n)

    d = 2
    is_prime = True  # Começamos supondo que n é primo;
                     # se acharmos um divisor próprio, mudamos para "False"
    
    if n <= 1:
        is_prime = False

    while d <= n // 2:
        if n % d  == 0:
            is_prime = False
        d = d + 1     
    
    if (is_prime):
        print("%d é primo \n" %n)
    else:
        print("%d não é primo" %n)
# -----
main()
'''
################################

def main():
    #  n	    número a ser testado se é primo
    #  d	    candidato a divisor 
    #  is_prime	    variável booleana (True/False) p/ indicar se n é primo ou não    
    #               Convencao: No final, is_prime = True   se n é primo 
  
    n = int(input("Digite um numero inteiro positivo (n)  ===> "))
    print("Inteiro dado = %d \n" %n)
   
    d = 2
    is_prime = True   # até prova em contrário vamos supor que n é primo
    
    if n <= 1:
        is_prime = False

    while (d <= n // 2  and is_prime):    
        if n % d  == 0:
            is_prime = False
        d = d + 1     
    
    if (is_prime):
        print("%d é primo \n" %n)
    else:
        print("%d não é primo \n" %n)
# -----
main()
