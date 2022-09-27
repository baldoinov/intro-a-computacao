# -*- coding: utf-8 -*-
'''
  ---- Manipulação de digitos de um número e montagem de novos números
  ------------------------------------------------------------------------
  Programa P31 
  ------------

    Dado um inteiro positivo n, determinar:
    o número de dígitos de n;
    a soma dos dígitos e n;
    o inteiro formado pelos dígitos pares de n na ordem reversa;
    o inteiro formado pelos dígitos ímpares de n na ordem correta
    e verificar se n é um palíndromo.
    Obs. Dizemos que um inteiro não-negativo é um palíndromo se
    ele é igual ao seu reverso. 
'''

#----------------------------------------------------------------------------
# n            - inteiro positivo dado
# n_copia      - cópia de n 
# num_digitos  - número de dígitos de n
# soma_digitos - soma dos dígitos de n
# num_par      - inteiro formado pelos dígitos pares de n na ordem reversa
# num_impar    - inteiro formado pelos dígitos ímpares de n na ordem correta
# reverso      - inteiro formado pelos dígitos de n na ordem reversa
# potdez       - potências de 10
# dig          - cada dígito de n
#-----------------------------------------------------------------------------

def main():
        
    n = int(input("Digite um inteiro positivo: "))
    n_copia = n
       
    num_digitos = 0   
    soma_digitos = 0  
    num_par = 0       
    num_impar = 0
    reverso = 0
    potdez = 1
    
    while n > 0:
        dig = n % 10
        num_digitos = num_digitos + 1
        soma_digitos = soma_digitos + dig
                
        if dig % 2 == 0:
            num_par = num_par * 10 + dig
        else:
            num_impar = num_impar + dig * potdez 
            potdez = potdez * 10

        reverso = reverso * 10 + dig
        n = n // 10
        
    print()
    print("Com relação ao inteiro", n_copia, "temos:")
    print("Número de dígitos =", num_digitos) 
    print("Soma dos dígitos =", soma_digitos)
  
    if num_par == 0:
        print("Não existem dígitos pares diferentes de zero.")
    else:
        print("Número formado pelos dígitos pares na ordem reversa =",
               num_par)

    if num_impar == 0:
        print("Não existem dígitos ímpares.")
    else:
        print("Número formado pelos dígitos ímpares na ordem correta =",
               num_impar)
        
    print("Reverso =", reverso)
    if reverso == n_copia:
        print(n_copia, "é um palíndromo.")
    else:
        print(n_copia, "não é um palíndromo.")

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
main()
