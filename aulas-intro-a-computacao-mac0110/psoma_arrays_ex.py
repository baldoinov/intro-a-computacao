'''
  Arquivo: soma_arrays.py
  -----------------------
  Dadas duas listas x e y, cada uma com n números inteiros,
  Imprimir uma lista dos n elementos  x[i] + y[i].
'''

def main():
    print("Esse programa recebe duas listas e imprime a soma dos termos das duas.\n")
    n = int(input("Digite o tamanho das listas: "))
    print()
    x = []
    y = []
    z = []

    for i in range(1, n+1):
        nux = int(input(f"Digite o {1}° termo da lista x: "))
        x.append(nux)

    print()

    for i in range(1, n+1):
        nuy = int(input(f"Digite o {1}° termo da lista y: "))
        y.append(nuy)

    print("\nA soma dos termos de x e y é: \n")

    for i in range(n):
        print(f"{x[i]} + {y[i]} = {x[i] + y[i]}")
        z.append(x[i]+y[i])

    print("\nOu seja: \n")
    print(f"z = {z}")


main()
