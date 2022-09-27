
"""
====  Já vimos:  Fatorial usando o comando "while" =====
======== programa p12a =================================

n = int(input("Digite um número inteiro não-negativo: "))
fat = 1
k = 2
while k <= n:
    fat = fat * k
    k = k + 1
        
print("\n O fatorial de", n, "é igual a", fat)
 
"""
#===============================================
#======= fatorial usando o comando "for"
#==============================================

n = int (input("Digite o valor de n: ")) 
fat = 1
for k in range(2,n+1): # [2, 3,...,n]
        fat = fat * k
        # print("k =", k, "fatorial de ", k, " = ", fat)
        
print("fatorial de", n, "=", fat)



      
