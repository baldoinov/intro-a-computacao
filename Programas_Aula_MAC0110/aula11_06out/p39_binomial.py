'''
 Programa p39  -- p39_binomial.py
 
 Escreva um programa para calcular os coeficientes binomiais
 Comb(4,2),Comb(5,2) e Comb(10,4).

 Fazer uso de uma função que recebe dois inteiros, n e k como parâmetros, e 
 retorna a combinação de n objetos tomados k a k  = Comb(n,k) =  n!/((n-k)!k!).
 Esta função por sua vez, deve fazer uso da função fatorial (embora não seja 
 a forma mais rápida de calcular Comb(n,k)). 

'''

def main():
    ''' Testes da função coef_bin '''

    print("Combinacao(4,2) =", coef_bin(4,2))      # chamada da funcao coef_bin
    print("Combinacao(5,2) =", coef_bin(5,2))      # chamada da funcao coef_bin
    print("Combinacao(10,4) =", coef_bin(10,4))    # chamada da funcao coef_bin
#--------------------------------
def fatorial(k):
    '''
       (int) -> int
    Recebe um inteiro k > 0  e retorna o valor de k!

    '''
    
    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # o mesmo que cont = cont + 1
        k_fat *= cont   # o mesmo que k_fat = k_fat * cont

    return k_fat

#----------------------------

def coef_bin(n, k):
    '''
     (int, int) -> int
     Recebe dois inteiros n e k, e retorna o valor de n!/((n-k)! k!)
    '''

    return fatorial(n)//(fatorial(n-k)*fatorial(k))

#------------------------------
main()
