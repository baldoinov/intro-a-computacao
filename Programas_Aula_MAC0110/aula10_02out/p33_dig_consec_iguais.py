# -*- coding: utf-8 -*-
'''
  ---- Manipulação de digitos de um número --------
  -------------------------------------------------
  Programa p33 ---------- p33_dig_consec_iguais.py
  ------------------------------------------------

  Dado um inteiro n > 0, verificar se em n há (pelo menos) 2 dígitos consecutivos iguais.

'''

def main():
       # n             : inteiro positivo dado
       # n_copia       : cópia de n 
       # dig_anterior  : digito de n obtido anteriormente
       # dig_atual     : digito de n obtido no passo atual 

    
    n = int(input("Digite o valor de n: "))
    n_copia = n      ## guardar uma copia, porque n vai ser alterado 
    
    dig_anterior = n % 10         # no início dig_anterior é o dígito mais à direita (casa da unidade)
    n = n // 10                   # n é atualizado removendo-se o seu último dígito
    tem_consec_iguais = False     
 
    while (n > 0 and not tem_consec_iguais):  #   equival: (n > 0 and tem_consec_iguais == False)
        dig_atual = n % 10
        if dig_atual == dig_anterior:
            tem_consec_iguais = True           
        dig_anterior = dig_atual     
        n = n // 10 
        
    if tem_consec_iguais:  
        print("O digito %d aparece consecutivamente em %d." %(dig_atual,n_copia))
    else:
        print("Nao há digitos consecutivos iguais em %d." %(n_copia)) 
        
#-------------------
main()

