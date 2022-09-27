# -*- coding: utf-8 -*-
'''
  Este programa define duas funcoes (para uso em outros programas).

  -  fatorial(n): recebe um inteiro n>=0 e retorna n!
  -  coef_bin(n,k): recebe dois inteiros n e k, com n>=0 e 0<=k<=n,
                    e retorna o coeficiente binomial n!/(k!(n-k)!).
'''
def main():
    print("Testes:")
    print("binomial(5,2)=",coef_bin(5,2))
    print("fatorial(5) = ", fatorial(5))
    
#--------------
def coef_bin(m,k):
    '''
    Recebe dois inteiros não-negativos m e k, com k <= m.
    Retorna o valor da combinação de m, k a k.
    '''
    return fatorial(m) // (fatorial(k) * fatorial(m - k))

#------------------------------------------------------------------------
# definição da função fatorial
   
def fatorial(n):
    ''' (int) -> int

    Recebe um inteiro n, n >= 0, e retorna n!
    '''
    
    fat = 1
    num = n 
    while num > 1:
        fat = fat * num
        num = num - 1

    return fat

#--------------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal 
    main() # chamada da função main
    # se fizer import function, pode-se usar as funcoes aqui definidas
 

