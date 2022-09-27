"""
   -------------------------------------------------------------
   -- Uso de variável booleana (lógica) para indicar status ---
   -------------------------------------------------------------
   Programa P32
   ------------

   Dado n (inteiro positivo), e uma sequência de n números inteiros, verificar 
   se esta sequência está em ordem crescente.  

   Solucao 1 -- lê a sequência toda, mesmo descobrindo que ela não está em ordem.
   Solucao 2 -  Se descobrir que a sequência não está em ordem, o programa 
                pára de continuar testando novos números da sequência. 

   OBS: Veja A duas soluções abaixo --- comentar uma delas para poder executar.

"""

# Só farei a solução 2

def main():
    k1 = 0
    k2 = 0
    cont = 1
    progressao = True
    n = int(input("Insira o número de termos da sequência: "))
    # k = int(input(f"Insira o 1° termo da sequência: "))

    while cont <= n and progressao:
        k = int(input(f"Insira o {cont}° termo da sequência: "))
        k2 = k1
        k1 = k

        if k2 > k1:
            progressao = False

        cont += 1

    if progressao:
        print("A sequência é crescente.")
    else:
        print("A sequência não é crescente. ")


main()
