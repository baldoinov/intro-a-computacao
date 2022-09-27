
"""
   Programa 08a -   p08a_imprime1a30.py
   Problema:
   Imprimir todos os inteiros de 1 a 30 separando-os de 3 em 3 por linha
   (e com  ** entre eles).
   
"""

# -----------------------------------------------------

print("Este programa imprime os inteiros de 1 a 30.")
      
num = 1

while num <= 30:
    print(num, num+1, num+2, sep=" ** ") 
    num = num + 3
print()    
# -----------------------------------------------------


