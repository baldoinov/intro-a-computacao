# -*- coding: utf-8 -*-
'''
   Programa p36 ----  p36_dig_menores8.py

   Dado n (um número inteiro positivo), verificar se todos
   os dígitos de n são menores que 8. 
   [Resolver usando "indicador de status" (variável booleana)]

'''

def main():
    n = int(input("Digite o valor de n: "))
    ok  = True # indica que os digitos são menores que 8
    
    n_copia = n
   
    
    while (n > 0 and ok):
        dig = n % 10
        if dig >= 8:
            ok = False
        n = n // 10

    if ok:
        print("Todos os dígitos de %d são menores que 8" %(n_copia))
    else:
        print("%d tem dígitos maiores ou iguais a 8" %(n_copia))
       
#--------------------------
main()
    
