
'''
   Hamonic_com_for.py

   Dado n, calcula o número Harmônico H(k), para k variando de 1 a n.

   H(k) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/k.
   
   Compare os dois programas abaixo. O primeiro, que está
   comentado usa o comando "while", o segundo, usa o comando "for"
'''

"""
def main():
    n = int(input("Digite o valor de n (inteiro positivo): "))
    H = 0.0 
    k = 1
    while k<=n:
        H = H + 1.0/k
        k = k + 1
        print ("H(%d) = %f" %(k,H))
# -----
main() 

"""

def main():
    n = int(input("Digite o valor de n (inteiro positivo): "))
    H = 0.0
    for k in range(1, n+1):  # k vai variar de 1 a n (com passo 1, como é positivo,
                             # o limite superior é excluído)
        H = H + 1.0/k
        print ("H(%d) = %f" %(k,H))
# -----

main() 




