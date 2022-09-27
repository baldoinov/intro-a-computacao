# -*- coding: utf-8 -*-
"""
   Programa P23a ------------p23a_ordena3.py
   -----------------------------------------

   Comando "if-else"   e    "if-elif"  (elif= else+if)
  ============================================================================
   Duas solucoes juntas (para facilitar a comparacao e entender o uso de elif)
   Compare "Trecho 1" com o "Trecho 2"
  =========================================================================
"""
############################################################################
#  Programa 23a   ----  p23a_ordena3.py
#  ----------------------
#   Problema: dados 3 numeros inteiros, imprimi-los em ordem crescente.
#  ------------------------------------------------------------------
	    
print("Vamos ordenar 3 numeros em ordem crescente.")
    
x = int(input("Digite o primeiro número: "))           
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: ")) 
# ---------------------------------------------------
print("-- Resultado do Trecho 1:")

if x <= y:
    if y <= z:
        print("Temos %d <= %d <= %d\n" %(x, y, z))
    else: # y > z 
        if x <= z:
            print("Temos %d <= %d <= %d\n" %(x, z, y))
        else: # x > z 
            print("Temos %d <= %d <= %d\n" %(z, x, y))
else: # x > y 
    if x <= z:
        print("Temos %d <= %d <= %d\n" %(y, x, z))
    else:
        if y <= z:
            print("Temos %d <= %d <= %d\n" %(y, z, x))
        else:
            print("Temos %d <= %d <= %d\n" %(z, y, x))
            
#------------------------------------------------------
print("-- Resultado do Trecho 2:")

if x <= y:
    if y <= z:
        print("Temos %d <= %d <= %d\n" %(x, y, z))
    elif x <= z:
        print("Temos %d <= %d <= %d\n" %(x, z, y))
    else:
        print("Temos %d <= %d <= %d\n" %(z, x, y))
elif x <= z: 
    print("Temos %d <= %d <= %d\n" %(y, x, z))
elif y <= z:
    print("Temos %d <= %d <= %d\n" %(y, z, x))
else:
    print("Temos %d <= %d <= %d\n" %(z, y, x))

#  Parabens se voce conseguiu entender que o uso do elif
#  elif =  else+if
#---------------------------------------------------------  
