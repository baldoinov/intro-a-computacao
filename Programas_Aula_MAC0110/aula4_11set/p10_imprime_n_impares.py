
"""
    Programa 10 -- p10_imprime_n_impares.py
    ---------------------------------------

    Dado um inteiro positivo n, imprimir os n primeiros inteiros 
    positivos ímpares.

"""
# -----------------------------------------------------------------------

print("Este programa imprime os n primeiros inteiros positivos ímpares.")

n = int(input("Digite um inteiro positivo para n: "))

print()
print("Os", n, "primeiros inteiros positivos ímpares são:")

impar = 1   # impar armazena os inteiros positivos ímpares
cont = 0    # cont representa a quantidade de ímpares impressos
while cont < n:
    print(impar)
    impar = impar + 2
    cont = cont + 1
    
# -----------------------------------------------------------------------
