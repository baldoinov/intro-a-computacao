"""
   Programa 09a  -- p09a_imprime_paq.py
   ------------------------------------

   Dados dois inteiros p e q, com p <= q, imprimir todos os inteiros
   k tais que p <= k <= q. (Se p > q não imprimir nada.)
   
"""
#----------------------------------------------------------------------
# layout sem uso de def main():
# ---------------------------------------------------------------------

print("Este programa imprime todos os inteiros entre p e q (dados).")

p = int(input("Digite um inteiro para p: "))
q = int(input("Digite um inteiro para q (>= p): "))

print()
print("Os inteiros entre", p, "e", q, "são:")  
  
num = p
while num <= q:
    print(num)
    num = num + 1
print("-----------------") # este é o comando seguinte ao comando while

# ---------------------------------------------------------------------
