# -*- coding: utf-8 -*-
'''
  Arquivo: busca2.py
  
  Dado um inteiro n e uma sequência com n termos (inteiros),
  verificar se um dado número x (inteiro) ocorre na sequência dada.
  
  Solução 2: (aproveitando a Solução 1 -- mas faz uso de "sentinela".

  O número procurado x é colocado no final da sequência dada.
  Dessa forma, sabe-se que x encontra-se na sequência estendida.
     Se x for encontrado antes do fim da sequência estendida,
     significa que x pertence à sequencia original; caso contrário, sabemos que 
     x não pertencia à sequência original.

  Note que no comando while não precisamos nos preocupar com o crescimento de i.
  (No pior caso, quando  i = n, teremos que achou = True).
  
  Veja depois a Solução 3 (busca3.py) (não faz uso da variável booleana achou). 

'''

def main():
        n = int(input("Digite o valor de n (número de termos da sequência): "))
        seq = []  
        for i in range(n):
            num = int(input("\n Digite um termo da sequência: "))
            seq.append(num)

        x = int(input("\n Digite o numero a ser procurado: "))

        print("\nSequência dada:")
        print(seq)
        
        seq.append(x) # Acrescentamos x no final da sequencia seq. (Vai ficar na posicao n)

        print("Sequência estendida artificialmente:")
        print(seq)
        
        achou = False
        i = 0
        while not achou:
            if x == seq[i]:
                achou = True
            else:                 # aqui usamos o else para que o valor de i  
                i += 1            # ao sair do 'while' seja exatamente a posicao onde x foi encontrado.
                
        if i < n: # i indica a posicao onde x foi encontrado 
            print("\n O número %d encontra-se na sequência." %(x))
        else:
            print("O numero %d nao se encontra na sequência." %(x))

#------------------------------------------
main()
                                                                                                        

   
