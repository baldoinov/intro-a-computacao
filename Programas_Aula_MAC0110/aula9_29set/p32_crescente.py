# -*- coding: utf-8 -*-
'''
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

'''
####################################################################################################
#  Solucão 1 -- continua testando mesmo tendo descoberto que a sequência não está em ordem crescente.
####################################################################################################

def main():    
    
    n = int(input("Digite um inteiro positivo para n: "))
    
    crescente = True   # indicador de status
                       # True, se sequência é crescente; False, em cc.
    
    anterior =int(input("Digite o primeiro termo da sequência: "))
    
    conta = 1
    while conta < n:
        atual = int(input("Digite outro termo da sequência: "))
        if atual < anterior:
            crescente = False 
        anterior = atual    
        conta = conta + 1
   
    if crescente:
        print("A sequência está em ordem crescente")
    else:
        print("A sequência não está em ordem crescente")
#------------
main()

'''
###################################################################################################
#  Solucão 2 -- para de testar assim que descobre que a sequência  não está em ordem crescente.
####################################################################################################

def main():    
    
    n = int(input("Digite um inteiro positivo para n: "))
    
    crescente = True   # até prova em contrário, vamos supor que a sequência é crescente.
    
    anterior =int(input("Digite o primeiro termo da sequência: "))    
    conta = 1
    while (conta < n and ........................):
        atual = int(input("Digite outro termo da sequência: "))
        if atual < anterior:
            crescente = False
        anterior = atual    
        conta = conta + 1
   
    if crescente:
        print("A sequência está em ordem crescente")
    else:
        print("A sequência não está em ordem crescente")
#------------
main()
'''

