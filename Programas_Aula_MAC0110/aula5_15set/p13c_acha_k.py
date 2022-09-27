 #---------------------------------
 # Programa 13c  -- p13c_acha_k.py
 # ------------------------------
 #  Este programa resolve o seguinte problema:
 #
 #  Dado um inteiro positivo n, determinar
 #  o menor inteiro positivo k tal que 
 #  a soma 1 + ... + k é maior que n 
 # ..........................................

def main():
    n = int(input("Digite um número inteiro positivo (n): "))
            
    soma = 1
    k = 1
    while soma <= n:      
        k = k + 1
        soma = soma + k 
        # print("a soma de 1 até", k, "é ", soma)
        print("a soma de 1 até %3d  é  %4d"  %(k, soma))

    # print("O menor inteiro k tal que  1 + ...+ k >", n, "é", k)
    print("O menor inteiro k tal que  1 + ...+ k > %3d é %4d"  %(n, k))
    
# ........
main() 


# Veja o uso de especificação de formato %kd  para inteiros,
# onde k é o número de dígitos desejados
# Veja a ausência de vírgula antes de %(k, soma)
# Veja a ausência de vírgula antes de %(n, k)
