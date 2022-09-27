# -*- coding: utf-8 -*-
"""
   Programa P23b ------------p23b_ordena3.py
   -----------------------------------------
   ---- Uso do operador booleano (lógico)  "and"  -- Uso de "elif"

   ==============================================================
   Duas solucoes equivalentes. Compare "Trecho 1" com o "Trecho 2"
  =========================================================================
"""
############################################################################
#   Programa 23b  -- p23b_ordena3.py
#  -----------------------------------
#   Problema: dados 3 numeros inteiros, imprimi-los em ordem crescente.
#  ---------------------------------------

def main():
    
    print("Vamos ordenar 3 numeros em ordem crescente.")
    
    x = int(input("Forneca o primeiro numero:"))           
    y = int(input("Forneca o segundo numero:"))
    z = int(input("Forneca o terceiro numero:"))
    
    #  Solucao para mostrar uso do operador lógico "and" 
    print("--- Resultado do Trecho 1:")

    if ((x <= y) and (y <= z)):
        print("Temos %d <= %d <= %d\n" %(x, y, z))
    elif ((x <= z) and (z <= y)):
        print("Temos %d <= %d <= %d\n" %(x, z, y))
    elif ((y <= x) and (x <= z)):
        print("Temos %d <= %d <= %d\n" %(y, x, z))
    elif ((y <= z) and (z <= x)):
        print("Temos %d <= %d <= %d\n" %(y, z, x))
    elif ((z <= x) and (x <= y)):
        print("Temos %d <= %d <= %d\n" %(z, x, y))
    else:
        print("Temos %d <= %d <= %d\n" %(z, y, x))
 
#  =====================================================
#  Solução sem uso de operadores booleanos
# ======================================================
    print("--- Resultado do Trecho 2:")

    #  Solucao diferente: veja como ficou a condição:

    if ((x <= y <= z)):
        print("Temos %d <= %d <= %d\n" %(x, y, z))
    elif ((x <= z <= y)):
        print("Temos %d <= %d <= %d\n" %(x, z, y))
    elif ((y <= x <= z)):
        print("Temos %d <= %d <= %d\n" %(y, x, z))
    elif ((y <= z <= x)):
        print("Temos %d <= %d <= %d\n" %(y, z, x))
    elif ((z <= x <= y)):
        print("Temos %d <= %d <= %d\n" %(z, x, y))
    else:
        print("Temos %d <= %d <= %d\n" %(z, y, x))
#--------------
main() 
