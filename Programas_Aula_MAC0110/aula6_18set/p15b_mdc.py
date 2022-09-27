
 # programa p15b      ---      p15b_mdc.py 
 # 
 # Este programa recebe dois numeros inteiros positivos a, b  e calcula o
 # maximo divisor comum (mdc) desses numeros, usando o algoritmo de
 # Euclides.
 # 

def main():

    # a e b  : numeros inteiros dados para calcularmos mdc(a,b)
    
    a = int(input("Forneca o primeiro numero (inteiro positivo): "))
    b = int(input("Forneca o segundo numero (inteiro positivo): "))

    print("a= ", a)
    print("b = ", b)
          
    while b!= 0:
        resto = a % b
        print("resto = ", resto)  # coloque como comenta'rio, se nao quiser imprimir
        a = b
        print("a = ", a)  # coloque como comenta'rio, se não quiser imprimir
        b = resto
        print("b = ", b)  # coloque como comenta'rio, se não quiser imprimir
                
    print("mdc(a,b) = ", a)
# ---------------------------
main()                             


# Compare este programa com o programa p15a_mdc.py 

# PERGUNTA 1: Este programa funciona para o caso em que A < B ?
# Execute o seu programa com A > B  e com A < B, veja o que acontece.

# PERGUNTA 2: Se for dado A > 0 e B = 0, o que acontece?

# PERGUNTA 3: Se for dado A = 0 e B > 0, o que acontece?
# Compare sua resposta com a da PERGUNTA 2

# OBS: Se A> 0 entao mdc(A,0) = mdc(0,A) = A
# OBS: Nao se define mdc(0,0).

##################################################

