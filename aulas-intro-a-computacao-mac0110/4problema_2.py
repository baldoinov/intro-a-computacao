"""
PROBLEMA 2 - notas acima da média

   Dados um inteiro positivo n e uma lista de n notas 
   (números reais entre 0 e 10), determinar quantas notas
   estão acima da média.
"""

def main():
    print("Esse programa pega um lista de notas e diz quantas estão acima da média.")
    n = int(input("Insira a quantidade de notas: "))
    x = []
    acumulado = 0
    cont = 0

    for i in range(n):
        nota = int(input("Digite a nota (entre 0 e 10): "))
        x.append(nota)
        acumulado += nota
    
    media = acumulado/n

    for p in range(n):
        if x[p] > media:
            cont += 1
    print(f"A média é {media}")
    print(f"Há {cont} notas acima da média.")

    
main()
