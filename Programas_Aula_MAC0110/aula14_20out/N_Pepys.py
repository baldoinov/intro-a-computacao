'''
Arquivo: Pepys.py

PROBLEMA 1:

Em 1693, Samuel Pepys perguntou a Isaac Newton qual dos dois casos é mais provável:
    Caso 1:  Obter "1" pelo menos 1 vez quando se joga um dado honesto 6 vezes;
    Caso 2:  Obter "1" pelo menos 2 vezes quando se joga um dado honesto 12 vezes.

Escreva um programa em Python que decide qual resposta Newton deveria dar.
Seu programa deve fazer um total de N experimentos, onde
N é um número inteiro (grande) a ser lido.


========================================================================
Dica 1: Usar a função  randint (do módulo random)  para geral um número aleatório
         inteiro no intervalo [1,6] para simular as jogadas de um dado
         (com faces 1, 2,.., 6).

Dica 2: Usar a função seed (do módulo random) para poder reproduzir o experimento.

OBS: Faça testes mudando a semente (no programa abaixo foi usado a semente 1);
     faça testes sem usar semente (para isso, remova o comando "random.seed(1)").

=============================================================================
'''

import random #<=== Novidade!

def main():

    total1_geral = 0
    total2_geral = 0
    
    for N in range(500, 1000): ## para N = 500,...,999
          i = 0
          total1 = 0 # contagem de ocorrencias do caso 1 
          total2 = 0 # contagem de ocorrencias do caso 2
    
          random.seed(1)   # <========= Vejam !!!! (experimente executar 2 vezes assim e veja as respostas)
                           #     Depois, comente o comando random.seed(1) e execute 2 ou 3 vezes, e veja as respostas)
    
          for i in range (0, N):  #faz N experimentos
                # teste do Caso 1  <============
                num_face1 = 0 
                jogadas = 0
                while (jogadas < 6 and num_face1 < 1):
                      face = random.randint(1,6)  # <==== gera um no. de a 6 aleatoriamente
                      if face == 1:
                            num_face1 = num_face1 + 1
                            total1 = total1 + 1
                      jogadas = jogadas + 1      
         
                # teste do Caso2:  <=============
                num_face1 = 0
                jogadas = 0 
                while (jogadas < 12 and num_face1 < 2):
                      face = random.randint(1,6)
                      if face == 1:
                            num_face1 = num_face1 + 1
                      jogadas = jogadas + 1        
                         
                if num_face1 > 1:
                      total2 = total2 + 1 

          print("Para %d, o caso 1 aconteceu %d vezes" %(N, total1))
          print("Para %d, o caso 2 aconteceu %d vezes" %(N, total2))
          
          if total1 > total2:
                  total1_geral = total1_geral + 1
          else:
                  total2_geral = total2_geral + 1
             
          print("Caso1 melhor até agora = ", total1_geral)  
          print("Caso2 melhor até agora = ", total2_geral)
        
        
#---------
main()
