
'''
   Arquivo: lista_reversa.py
   ---------------------------------
   Dados um inteiro positivo n e uma sequência de n inteiros,
   criar uma lista x com esses elementos (na ordem dada) e 
   depois fazer com que x seja essa lista dada, mas na 
   ordem inversa. 

   Veja o uso de 
                 x.reverse()   
                 list(reversed(x))
'''


def main():
    n = int(input("Digite o numero de elementos da sequencia: "))

    x = []  # cria uma lista vazia 

    for i in range(n):
        num = int(input("Digite um termo da sequencia:"))
        x += [num]  

    print("x dado   =  ", x) 

    # Construcao de x reverso:
    
    meio = n//2
    for k in range(meio):
        aux = x[k]
        x[k] = x[n-1-k]
        x[n-1-k] = aux
        
    print("x reverso construído = ", x)

    #################
    print("------------------------------")
    
    print("Reversão de x usando x.reverse():")
    x = [2, 4, 6, 8]
    print("Suponha que x=", x)
    print("Fazendo x.reverse() e imprimindo x depois, obtemos:")
    x.reverse()  # para reverter a lista x 
    print("x =", x)

    print("-----------------------------")
    
    ##################################

    print("Fazendo y = list(reversed(x)); imprimindo y depois; e imprimindo x em seguida:")
    y = list(reversed(x))      
    print("y =", y)
    print("x =", x, "<====== x não foi alterado")
    
#-----------------
main()

