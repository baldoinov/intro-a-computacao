"""
  --------------------------------------------------------------------
  -------------- Comando "if" 
  -------------------------------------------------------------------

Programa 16b -- p16b_soma_par_total_par.py

  Dados um inteiro positivo n e uma sequência com n números inteiros,
  determinar a soma dos inteiros PARES da sequência, e a quantidade 
  de números pares da sequência.

 --------------------------------------------------------------------
  Veja o programa abaixo, dado na aula..... 
  Vamos modificá-lo para resolver o problema acima.


  Programa 10b -- p10b_soma_n_numeros.py
  ---------------------------------------

    Dado um inteiro positivo n, e a seguir n números inteiros
    (dados um por vez), calcular a soma desses elementos.

    Ex: 5 (valor de n)  e   3  7  9  11  43

   - - - - - - - - 

print("Este programa calcula a soma de n números inteiros, para um dado n.")

n = int(input("Digite um inteiro positivo (valor de n): "))

soma = 0
cont = 0
while cont < n:
    num = int(input("Digite um número inteiro qualquer: "))
    soma = soma + num
    cont = cont + 1 
    print("--- Soma parcial dos números pares = ", soma)
    
print("*** Soma dos números pares = ", soma)

 
"""
#--------------------------------------------------------------
# -----  p16a_soma_par_total_par.py    ----------------------

print("\n Dada uma sequência de n números inteiros, calcular \n a soma dos números pares dessa sequência.\n")

n = int(input("Digite um inteiro positivo (valor de n): "))

soma = 0
cont = 0
cont_par = 0

while cont < n:
    num = int(input("Digite um número inteiro qualquer: "))
    if num % 2 == 0: 
        soma = soma + num
        cont_par = cont_par + 1
        print("--- Soma parcial dos números pares dados = ", soma)
    cont = cont + 1     
    
print("*** Soma dos números pares da sequência  = ", soma)
print("*** Quantidade de números pares da sequência  = ", cont_par)



