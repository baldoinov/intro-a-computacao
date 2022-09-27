# -*- coding: utf-8 -*-

'''
   Arquivo: imprima_ordem_inversa_sol2.py
   -------------------------------------

   Dados um inteiro positivo n e uma sequência de n inteiros,
   imprimi-los na ordem inversa à da leitura.

Solucao 2: (comparar com a solução 1 dada em imprima_ordem_inversa_sol1.py)

'''

def main():
    n = int(input("Digite o numero de elementos da sequencia: "))

    x = []  # cria uma lista vazia 

    for i in range(n):
        num = int(input("Digite um termo da sequencia:"))
        x.append(num)                     # <=====  insere num no final da lista x
        
    print("Lista na ordem de entrada:\n", x)

    print("Impressão da lista na ordem inversa à da entrada (com espacos em branco):")
    
    for i in range(n):
        print(x[n-1-i], end='  ') # imprime os elementos na mesma linha deixando 2 espaços em branco
        
    print()
    print("Impressão da lista na ordem inversa à da entrada (com elementos separados por vírgulas):")   
    for i in range(n):
        print(x[n-1-i], end=', ') # imprime os elementos na mesma linha separando por vi'rgulas

    print()

    print("Outra forma de imprimir na ordem inversa (usando índice negativo):")

    for i in range(-1,-n-1,-1):
         print(x[i], end=' , ') #<=== Podemos ter índices negativos!!!!!
         
    # Lembrar que x[-i] corresponde ao i-esimo elemento da lista x,
    # começando do fim para o começo.  começo <---------- fim

    

    print("\n**** Soluções usando ferramentas prontas do Python:")
    
    ############ Exemplos para ver a  diferença entre  reversed(x) e  x.resverse()

    # Seja x = [1, 2, 3, 4, 5]
    # reversed(x) corresponde à uma lista com os elementos de x na ordem inversa.
    # Entao reversed(x) = [5, 4, 3, 2, 1], mas x não se altera.

    # Se execcutarmos  x.reverse() então x ficará com os seus elementos na ordem inversa.
    # Ou seja, x = [5, 4, 3, 2, 1]
    # Poderíamos ter usado isso para fazer a impressão direta de x após a reversão.
    # 
    #
    #### Outra solucao para imprimir os elementos de uma lista na ordem inversa #####
    
    z = [9, 8, 7, 6, 5]
    print("Suponha que z = ",z)
    z.reverse()  #<======================================== a lista z agora está invertida 
    print("impressao de z após ter feito z.reverse():" )
    print("z =", z)

    ############################################################
    #              reversed(x) onde x é uma lista 
    ############################################################
    w = [1, 2, 3, 4, 5]
    print("Considere w =", w)
    print("Impressao dos elementos de w, na ordem inversa, um por linha (usando reversed(w)):") 
    for elemento in reversed(w):
        print(elemento)             # imprime cada elemento numa linha distinta
        
    print("Impressao dos elementos de w, na ordem inversa, na mesma linha (usando reversed(w)), separados por brancos:")
    for elemento in reversed(w):
        print(elemento, end ='  ')  # imprime na mesma linha, separados por 2 espaços em branco

    print()

    # Podemos criar uma nova lista que corresponde à lista w invertida:
    print("w = ", w)
    y = list(reversed(w)) # y aponta  para uma lista com os elmentos de w na ordem inversa  
    print("y=list(reversed(w)) =", y)   
    print("Note que w não foi alterado:")
    print("w = ", w)  ### OBS: a lista w não foi alterada com o reversed(z) 
              
#-----------------
main()


