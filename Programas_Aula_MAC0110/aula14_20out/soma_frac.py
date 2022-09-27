

"""
  Calcular a soma
       1 - 1/2  + 1/3  - 1/4  + ... + 1/9999 - 1/1000

ä) adição dos termos da direita para a esquerda

b) adição dos termos da esquerda para a direita

c) adição separada dos termos positivos e dos termos negativos da esquerda para a direita

d) adiçao separada dos termos positivos e dos termos negativos da direita para a esquerda
    
Compare e discuta os resultados obtidos.

"""

def main():

    print("Soma da direita para a esquerda:")
    soma_a = 0.0
    sinal = -1
    for k in range(10000, 0, -1):
        soma_a = soma_a + sinal * (1/k)
        sinal = -sinal
    print("soma_a = ", soma_a)

    print()
    #-----------------------
    
    print("Soma da esquerda para a direita:")
    soma_b = 0.0
    sinal = 1
    for k in range(1, 10001):
        soma_b = soma_b  + sinal * (1/k)
        sinal = -sinal
    print("soma_b = ", soma_b)
    print()
    #----------------------
    
    print("Soma separada dos posit e negat da esquerda para a direita:")  
    soma_p = soma_n = 0
    
    for k in range(1, 10000, 2):
        soma_p = soma_p + 1/k
    print("soma_p=", soma_p)
    for k in range(2, 10001, 2):
        soma_n= soma_n + 1/k
    print("soma_n =", soma_n)
    print("soma_c= ", soma_p - soma_n)
    print()
    #----------------------
    
    print("Soma separada dos posit e negat da direita para a esquerda:")  
    soma_p = soma_n = 0
    
    for k in range(9999, 0, -2):
        soma_p = soma_p + 1/k
    print("soma_p =", soma_p)
    for k in range(10000, 1, -2):
        soma_n= soma_n+ 1/k
    print("soma_n =", soma_n)
    print("soma_d = ", soma_p - soma_n)
    print()

main()

        
        
