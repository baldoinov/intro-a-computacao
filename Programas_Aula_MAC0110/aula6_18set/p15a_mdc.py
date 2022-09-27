
 # programa p15a  --   p15a_mdc.py
 # 
 # Este programa recebe dois numeros inteiros positivos a, b
 # e calcula o maximo divisor comum (mdc) desses numeros, usando o 
 # algoritmo de Euclides.
 # 

def main():

    # a e b : numeros inteiros dados para calcularmos mdc(a,b)
    
    a = int(input("Forneca o primeiro numero: "))
    b = int(input("Forneca o segundo numero: "))

    print("a = ", a)
    print("b = ", b)
    print()
    
    resto = a % b  # resto da divisao inteira de a por b
    
    while resto != 0:
        a = b
        b = resto
        print("a = ", a)  # coloque como comenta'rio, se não quiser imprimir
        print("b = ", b)  # coloque como comenta'rio, se não quiser imprimir
        print()
        resto = a % b
        
    print("mdc(a, b) = ", b)
# ..............................
main()                             


