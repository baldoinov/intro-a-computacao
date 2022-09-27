
import math   #< Precisa porque vamos usar a funcao sqrt(.)  da biblioteca math 

def main():
    print("Solucao aproximada de Pi, usando a fórmula de Ramanujan:") 
    print("Valor aproximado de Pi =", aproximacao_pi()) #<= chamada da função aproximacao_pi()
    print() 
#-----------------------------
     
def fatorial(n):
    '''
     (int) --> int 
     Calcula o fatorial de n e devolve esse valor
    '''
    fat = 1
    for k in range(1, n+1):
        fat = fat * k
    return fat

#-----------------------------

def aproximacao_pi():
    '''
      (none) --> float 
       Calcula uma aproximacao para a constante pi, de acordo com a fórmula devido a
       Srinivasa Ramanujan; e somando os termos até que o termo fique menor do que e 1e-15 
       OBS:  1e-15 é notacao (científica) em Python referente a 1 x 10 ^(-5) = 0.00001  
     
       Veja a fórmula em http://en.wikipedia.org/wiki/Pi
       ou veja o arquivo aprox_pi_screen.pdf 
    '''
    
    total = 0
    k = 0
    fator = 2 * math.sqrt(2) / 9801     #<=== uso da funcao pré-definida sqrt(.)
    while True:
        num = fatorial(4*k) * (1103 + 26390*k)
        den = fatorial(k)**4 * 396**(4*k)
        term = fator * num / den
        total += term
        if term  < 1e-15  
            break
        k += 1

    return 1 / total
#-------------------------------
main()
