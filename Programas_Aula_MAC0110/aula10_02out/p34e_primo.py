# -*- coding: utf-8 -*-
'''
    Programa p34e ----------- 34e_primo.py
   --------------------------------------------------

   Dado n (inteiro positivo), testar se n é primo.
   Def: um inteiro positivo n é primo se tem exatamente dois divisores: o 1 e o próprio n.
  (1 não é primo; 2 é primo; 3 é primo; 4 não é primo; 5 é primo,...)
   
   Solução que não testa os divisores pares. Para isso, testa antes se n é par.
'''


def main():
    #  n	    número a ser testado 
    #  d	    candidato a divisor 
    #  is_prime	    variável booleana (True/False) p/  indicar se n é primo ou não    
    #               Convencao: No final, is_prime = True   se n é primo 
    #                                    is_prime = False  se n não é primo       
   
    n = int(input("Digite um número inteiro positivo (n): ")) 
    print("Número dado = %d \n" %n)

    if (n <= 1 or (n != 2 and n % 2 == 0)):
        is_prime = False      # nenhum número inteiro <= 1 ou par > 2 é primo 
    else:
        is_prime = True   #  se n = 2  ou  n é ímpar, n>=3, até prova em contrário, is_prime = True

    # Até aqui, is_prime = True indica que ainda não achamos um divisor de n que
    # comprova que n não é primo. 
    
    d = 3
    while (d * d <= n  and is_prime):  # <=========== Testa enquanto d <= raiz quadrada de n 
        if (n % d == 0):      
            is_prime = False       # achamos um divisor, então n não é primo 
        d = d + 2                  # os candidatos a divisor são ímpares: 3, 5, 7...
    
    if (is_prime):
        print("%d é primo \n" %n)
    else:
        print("%d não é primo \n" %n)    
# ---------------
main()
