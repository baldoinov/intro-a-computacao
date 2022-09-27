'''
   Programa 06a - p06a_operadores.py
   ---------------------------------
   Este programa ilustra o uso de operadores aritméticos 
   
'''
def main():
    a = int(input("Digite um número inteiro:                  "))
    b = int(input("Digite um número inteiro distinto de zero: "))
            
    soma      = a + b    # adição
    diferenca = a - b    # subtração
    produto   = a * b    # multiplicação
    quociente = a // b   # quociente será o maior inteiro menor ou igual a a/b
    resto     = a % b    # resto será  (a - (a // b) * b) 
    exp       = a ** b   # potenciação (exponenciação)

    print(a, "+",  b, "=", soma)
    print(a, "-",  b, "=", diferenca)
    print(a, "*",  b, "=", produto)
    print(a, "//", b, "=", quociente) 
    print(a, "%",  b, "=", resto)     
    print(a, "**", b, "=", exp)        
#----------------------------
main()

# ---------------------------------------------------------------------
#  Operadores // e %
# -------------------
#  q = a // b
#  q será o maior inteiro menor ou igual a (a / b)
#
#  r = a % b
#  r será  (a - (a // b) * b)
#
# ---------------------------------------------------------------------


            
    
