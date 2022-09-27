# -*- coding: utf-8 -*-
'''
  Arquivo: soma_arrays.py
  -----------------------
  Dadas duas listas x e y, cada uma com n números inteiros,
  Imprimir uma lista dos n elementos  x[i] + y[i].
'''


def main():
    n = int(input("Digite o número de elementos de cada sequência: "))

    print ("n =",  n)
    
    x = []  # cria uma lista vazia x
    y = []  # cria uma lista vazia y
    
    
    # leitura dos n termos da lista x
    for i in range(n):
        num = int(input())
        x += [num]  # concatena num no final da lista x
                     # equivalente a   x.append(num)

    # leitura dos n termos da lista y    
    for i in range(n):
        num = int(input( ))
        y += [num]  # concatena num no final da lista y
                       # equivalente a  y.append(num)
  
    # termos correspondentes da listas x e y.
    print("x = ", x)
    print("y = ", y)

    z = [ ] # cria lista vazia z
    
    print("Soma de cada elmento da lista x com o correspondente da lista y") 
    for i in range(n):
        z = z + [x[i] + y[i]]
        
        # z = z + [x[i]] + [y[i]] O que acontece? 
        # z.append(x[i]+y[i]) 
    print("z = ", z) 
     
#-----------------
main()
