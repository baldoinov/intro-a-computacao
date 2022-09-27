
'''
   Arquivo: roleta.py
  
   Dados um inteiro positivo n, simular n apostas na roleta, 
   escolhendo n vezes um  nu'mero inteiro aleatório entre 0 e 36
   (para isso, usar um gerador de números aleatórios). 
   Para essas n jogadas, determinar 
   (a) o número de ocorrencias de cada um dos 37 valores,
   (b) quais números ocorrem mais frequentemente (indicar todos, se houver empate).
   
'''
import random

def main():
    # Criar uma lista ocorrencia, e inicializá-la com zeros
    ocorrencia = []
    for i in range(37):    # range(37) = [0, 1, 2,...,36]
        ocorrencia.append(0)
        
    #    Outra alternativa equivalente para se criar uma lista ocorrencia com
    #    37 zeros é  utilizar repetição de listas; ou seja, fazer
    #    ocorrencia = [0] * 37 
    
    
    n = int(input("Digite o número de apostas: "))

    # OBS: Para cada i (de 0 a 36), ocorrencia[i] representará o número
    # de ocorrencias de i nas n apostas. (Por isso, inicializamos com zero.)
    
    
    #random.seed(20)
    
    for k in range(n):
        num = random.randint(0, 36)  # randint retorna um  número inteiro aleatório no intervalo 0,...,36
        ocorrencia[num] = ocorrencia[num] + 1     # pode escrever ocorrencia[num] += 1

    for i in range(37):
        print("%2d ocorreu %d vezes" %(i, ocorrencia[i]))
        
    freq_max = max(ocorrencia)       # max(lista) retorna o maior valor que ocorre na lista
    print("Maxima frequencia =", freq_max)

    print("Numeros que ocorrem mais frequentemente (%d vezes):" %(freq_max))
    for i in range(37):
        if ocorrencia[i] == freq_max:
            print("%d" %(i))                

#-----------------------------------------------------------------------------------
main()

========================
Exercício:

x = [ 5  -2  9 -6  -8   12  67  -50   9   8   100 - 5]
             
