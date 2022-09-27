 #---------------------------------
 # Progaram 13a  -- p13a_acha_k.py
 # ------------------------------
 #  Este programa determina o menor inteiro positivo k tal que 
 #  a soma 1 + ... + k é  maior que 500.
 # ..........................................

def main():
    soma = 1
    k = 1
    while soma <= 500:      
        k = k + 1
        soma = soma + k 
        print("a soma de 1 até", k, "é ", soma)

    print("O menor inteiro k tal que  1 + ...+ k > 500 é ", k)
# ........
main() 


# Modifique o programa acima, e produza um programa
# que recebe um inteiro n > 1 (no programa acima n = 500),
# e calcula o menor inteiro k tal que 
# a soma 1 + ... + k é maior que n.
