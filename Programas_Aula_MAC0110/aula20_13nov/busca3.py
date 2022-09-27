# -*- coding: utf-8 -*-
'''
  Arquivo: busca3.py
  
  Dado um inteiro n e uma sequencia com n termos (inteiros),
  verificar se um dado numero x (inteiro) ocorre na sequencia dada.
  
  Solucao 3: (mais simples e elegante que a Solucao 1  e a Solucao 2)

  
  O número procurado x é colocado no final da sequência dada.
  Dessa forma, sabe-se que x encontra-se na sequência estendida.
     Se x for encontrado antes do fim da sequência estendida,
     significa que x pertence à sequencia original; caso contrário, sabemos que 
     x não pertencia à sequência original.

  Note que no comando while nao precisamos nos preocupar com o crescimento de i.
  Podemos simplesmente verificar em qual momento x é  encontrado (sabemos que vai 
  ser encontrado).  Nem precisamos fazer uso da variavel booleana "achou". 
  (Veja como o while ficou simples).
 
 '''

def main():
        n = int(input("Digite o valor de n (numero de termos da sequencia): "))
        seq = []  
        for i in range(n):
            num = int(input("\n Digite um termo da sequencia: "))
            seq.append(num)

        
        print("\nSequência dada:")
        print(seq)
        
        x = int(input("\n Digite o numero a ser procurado: "))
        seq.append(x)               # Colocamos x no final da sequencia. (Vai ficar na posicao n)

        print("sequencia estendida artificialmente:")
        print(seq)
        
        i = 0
        while x != seq[i]:
            i += 1
                        
        if i < n:     # i indica a posicao onde x foi encontrado 
            print("O número %d encontra-se na sequência." %(x))
        else:
            print("O número %d não se encontra na sequência." %(x))

#------------------------------------------
main()
                                                                                                        
