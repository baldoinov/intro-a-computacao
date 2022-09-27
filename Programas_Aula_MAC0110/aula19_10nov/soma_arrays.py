# -*- coding: utf-8 -*-
'''
  Arquivo: soma_arrays.py
  -----------------------
  Dadas duas listas x e y, cada uma com n números inteiros,
  Imprimir uma lista dos n elementos  x[i] + y[i].
'''


def main():
    n = int(input("Digite o número de elementos das sequências: "))

    x = []  # cria uma lista vazia x
    y = []  # cria uma lista vazia y
    
    
    # leitura dos n termos da lista x
    for i in range(n):
        num = int(input("Digite um termo da lista x:"))
        x += [num]  # concatena num no final da lista x
                     # equivalente a   x.append(num)

    # leitura dos n termos da lista y    
    for i in range(n):
        num = int(input("Digite um termo da lista y:"))
        y += [num]  # concatena num no final da lista y
                       # equivalente a  y.append(num)
  
    # termos correspondentes da listas x e y.
    print("x = ", x)
    print("y = ", y)

    print("Soma de cada elmento da lista x com o correspondente da lista y") 
    for i in range(n):
        print(x[i] + y[i], end=', ')
        # Cuidado: nao podemos fazer z[i] = x[i] + y[i], mesmo após
        # ter criado uma lista vazia z = [ ].
        # Se quisermos guardar numa lista z, precisamos criar z, e inicializá-la
     
#-----------------
main()
