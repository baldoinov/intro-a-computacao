
"""
    Programa 10b -- p10b_soma_n_numeros.py
    ---------------------------------------

    Dado um inteiro positivo n, e a seguir n números inteiros
    (dados um por vez), calcular a soma desses elementos.

    Ex: 5 (valor de n)  e   3  7  9  11  43

"""
# -----------------------------------------------------------------------

print("Este programa calcula a soma de n numeros inteiros, para um dado n.")

n = int(input("Digite um inteiro positivo (valor de n): "))

soma = 0
cont = 0
while cont < n:
    num = int(input("Digite um número inteiro qualquer: "))
    soma = soma + num
    cont = cont + 1 
    print("Soma dos", cont, "primeiros elementos = ", soma)
    
print("Soma dos", n , "numeros dados = ", soma)
# -----------------------------------------------------------------------
