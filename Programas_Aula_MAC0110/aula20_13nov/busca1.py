# -*- coding: utf-8 -*-

'''
  Arquivo: busca1.py
  
  Dado um inteiro n e uma sequencia com n termos (inteiros),
  verificar se um dado numero x (inteiro) ocorre na sequencia dada.
  
  OBS: Sem ter informação se a sequência está ordenada ou não, 
  temos que comparar x com cada elemento da sequência dada.

  Solucao 1 (compare com a Solucao 2 -- programa busca2.py)

'''

def main():
        n = int(input("Digite o valor de n (numero de termos da sequencia): "))
        seq = []
        for i in range(n):
            num = int(input("\n Digite um termo da sequencia: "))
            seq.append(num)
        print() 
        print("seq=", seq)
        
        x = int(input("\n Digite o numero a ser procurado: "))

        achou = False
        i = 0
        while (i < n and not achou):
            if x == seq[i]:
                achou = True
            i += 1
            
        if achou:
            print("\nO numero %d encontra-se na sequencia." %(x))
        else:
            print("\nO numero %d nao se encontra na sequencia." %(x))

#------------------------------------------
main()
                                                                                                        
