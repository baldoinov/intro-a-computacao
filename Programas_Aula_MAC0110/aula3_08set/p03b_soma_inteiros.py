"""
   Programa 03b --  p03b_soma_inteiros.py
   --------------------------------------
   Problema:
   Dados dois números inteiros, determinar a sua soma.
"""
# --------------------------------------------------------

def main():   # definicao da funçao main 
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input('Digite o segundo número inteiro: '))
    
    soma = a + b
    
    print("A soma de", a, "com", b, "é igual a", soma)
    print()
    print(a, "+", b, "=", soma)

# --------------------------------------------------------
# ----------início da execução do programa ---------------
main()   # chamada da funcao main 
