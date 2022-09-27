# -*- coding: utf-8 -*-
'''
  Programa p41  --  p41_mdc_varios.py
  -----------------------------------

  Dado um inteiro positivo n>=2 , e uma sequência de n números
  inteiros positivos, calcular o mdc desses numeros.

'''

def main():
    n = int(input("Digite o total de termos da sequência (n>=2): ")) 
    num_a= int(input("Primeiro número da sequência: "))
    num_b= int(input("Segundo número da sequência: "))
    
    result = mdc(num_a,num_b)
    print("Até aqui o mdc é %d" %(result))
    
    conta =  2
    while conta < n:
        num_c = int(input("Próximo número da sequência: "))
        result = mdc(result, num_c)
        print("Até aqui  o mdc é %d" %(result))
        conta = conta + 1
    print("O mdc dos números dados é: %d" %(result))
# --------------------
def mdc(a,b):
    ''' (int, int) --> int
        calcula o mdc de a e b e retorna esse valor
    '''
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b
#------------------------------
main()

""" mdc   25    45     90    120  
        =======
           5         90    120 
           ===========
                5          120
                 ============
                       5 """
