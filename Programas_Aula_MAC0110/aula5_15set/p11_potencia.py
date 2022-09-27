
 # ----------------------------------
 # Programa 11  --  p11_potencia.py
 # ---------------------------------
 # Este programa recebe dois inteiros a e n (n>=0) e calcula
 # o valor de a elevado à potência n, 
 # Definição:
 #
 # a^0 = 1  qualquer que seja o valor de a
 # a^n = a * (a^(n-1)), se n > 0                 1 * a * a * a ... * a
 # ................................................

def main():
    a = int(input("Digite o valor da base (um inteiro a): "))
    n = int(input("Digite o valor do expoente (um número inteiro não-negativo n): "))
    
    pot = 1  # <=========== 
    cont = 0
    
    while cont < n:
        pot = pot * a
        cont = cont + 1
        print(pot, end=" ")  # imprimir sem mudança de linha
        
    print("\n O valor de", a, "elevado à potência", n, "é igual a", pot)      
# .............      
main()      


# Por que não começamos com pot = a e controlamos n-1 repetições?
# Resposta:................................
