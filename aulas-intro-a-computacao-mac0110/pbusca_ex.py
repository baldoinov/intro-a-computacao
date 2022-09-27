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
    n = int(input("Digite o tamanho da sequência: "))
    seq = []

    for i in range(1, n+1):
        num = int(input(f"Digite o {i}° termo da sequência: "))
        seq.append(num)

    x = int(input("\nQual o número procurado? "))
    seq.append(x)

    i = 0
    while x != seq[i]:
        i +=1

    if i < n:
        print(f"O número {x} está na sequência.")
    else:
        print(f"O número {x} não está na sequência.")


main()
