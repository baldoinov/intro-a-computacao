# -*- coding: utf-8 -*-
'''
  ------------------------------------------------------
   --------------- Uso de função -----------------------
  ------------------------------------------------------ 
  programa:  p35b_soma_de_primos.py  
  ---------------------------------
  Dado um inteiro positivo n, verifica se n é soma de dois números primos. 
  
  OBS: O programa deve fazer uso de uma funcao que verifica se um numero é primo
  Compare a função primo(n) abaixo com a do programa p35a_soma_de_primos.py
  
'''
def main():
    n = int(input("Digite um numero inteiro positivo (n): ")) 

    k = 2 
    achou = False
    
    while (k <= n // 2 and not achou):
            if (primo(k) and primo(n-k)):
                achou = True
                print ("%d = %d + %d" %(n, k, n-k))
                print("%d e %d são números primos" %(k, n-k))
            else:
                k = k + 1
    if not achou:
        print(n, "não é soma de dois números primos")
                
# ---------------

def primo(n):
    '''
        (int) --> bool   # Significa que o parâmetro n é um número inteiro; e retorna 
                         # um valor booleano (True ou False)
        Verifica se n é primo. Se sim, retorna o valor True;
                               em c.c. retorna o valor False.
    '''
    ##################
    # usar o programa p34e_primo.py (o mais eficiente)
    # para definir aqui a funcao primo (n).
    # Veja o programa p35a_soma_de_primos.py para ver como
    # usar return para retornar os valores True ou False.
    #################
    
 #----------------------------------------
main()
