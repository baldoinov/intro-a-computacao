 # -*- coding: utf-8 -*-
""" 
  -------------------------------------------
                   Comando "if" 
  -------------------------------------------
  Programa 18 -    p18_nota_max_min.py
  ------------------------------------
  
  Programa: dado um inteiro positivo n e 
  dadas n notas (inteiros entre 0 e 100), determinar
  a maior nota e a menor nota.

""" 

def main():
    n = int(input("Digite o total de notas (n): "))

    nota_max = 0     # veja bem a inicializaçãde nota_max
    nota_min = 100   # veja bem a inicialização de nota_min 

    i = 0  # contador (para saber quantas notas foram lidas)

    while i < n:
        nota = int(input("Digite uma nota: "))
 
        if nota > nota_max:
            nota_max = nota

        if nota < nota_min:
            nota_min = nota

        i = i + 1;

    print("A nota máxima é ", nota_max)
    print("A nota mínima é ", nota_min)
# ----------------------
main() 
