'''
   Programa 06b - p06b_operadores.py
   --------------------------------
   Este programa ilustra o uso de operadores aritméticos.
   (Veja o uso de / e o uso de // visto em p06a_operadores.py) 
'''

def main():
    a = float(input("Digite um número em ponto flutuante: "))
    b = float(input("Digite um número em ponto flutuante: "))
            
    soma      = a + b    # adição
    diferenca = a - b    # subtração
    produto   = a * b    # multiplicação
    quociente = a / b    # quociente da divisao de a por b
    quoc      = a // b   # será o maior inteiro menor ou igual à divisão de a por b.
                         # Ou seja, floor(a/b) = chao(a/b)
    exp       = a ** b   # potenciacao (exponenciacao)

    print(a, "+",  b, "=", soma)
    print(a, "-",  b, "=", diferenca)
    print(a, "*",  b, "=", produto)
    print(a, "/",  b, "=", quociente)
    print(a, "//",  b, "=", quoc)
    print(a, "**", b, "=", exp)        
#----------------------------
main()


            
    
