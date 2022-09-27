'''
   Arquivo: notas_acima_media.py
   ---------------------------------

   Dados um inteiro positivo n e uma sequência de n notas 
   (números reais entre 0 e 10), determinar quantas notas
   estão acima da média. 

'''

def main():
    n = int(input("Digite o numero de notas da lista: "))

    x = []  # cria uma lista vazia 
    for i in range(n):
        nota = float(input("Digite uma nota da lista:"))
        x = x + [nota]  # ou equivalentemente,  x.append(nota)

    print("x =", x)
    
    
    soma = 0.0
    for i in range(n):
        soma = soma + x[i]
    
    media = soma/n 
    total = 0

    for i in range(n):
       if x[i]> media:
           total +=  1
    
    print("Media = ", media)
    print("Total de notas acima da média = ", total)

#-----------------
main()

