# -*- coding: utf-8 -*-
"""
   Programa P22a ------------p22_compara2.py
   -----------------------------------------
   Comando  "if-else"  --- uso de elif = else+if ---   "if-elif"  
   
    Comparar 2 números, e dizer qual a relação de ordem entre eles.

    (Compare o TRECHO 1 com o TRECHO2)
    (são equivalentes: o TRECHO 2 ficou mais conciso e claro)
"""

######################
#      TRECHO 1
######################

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

print("x = ", x, "   y = ", y)

print ("---------------------------------")
print ("Resultado do Trecho 1:\n")

if x < y:
    print("x é menor do que y")
    print("%d é menor do que %d" %(x,y))
else:  # x >= y 
    if x > y:
        print("x é maior do que y")
        print("%d é maior do que %d" %(x,y))
    else:
        print("x e y são iguais")
        print( x, " e ", y,  "são iguais")


##############################################
        #  TRECHO 2
#############################################
print ("----------------------------------")

print("Resultado do Trecho 2:\n")

if x < y:
    print("x é menor do que y")
    print("%d é menor do que %d" %(x,y))
elif x > y:
    print("x é maior do que y")
    print("%d é maior do que %d" %(x,y))
else:
    print("x e y são iguais")
    print("%d e %d são iguais" %(x,y))

