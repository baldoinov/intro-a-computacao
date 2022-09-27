
import math   #< Precisa porque vamos usar a funcao sqrt(.)  da biblioteca math 


def main():
    print("Solucao aproximada de Pi, usando a fórmula de Ramanujan:") 
    print("Valor aproximado de Pi =", aproximacao_pi()) #<=  chamada da função aproximacao_pi)
    print() 
#-----------------------------
     
def fatorial(n):
    '''
     (int) --> int 
     Calcula o fatorial de n e devolve esse valor
    '''
    fat = 1
    for k in range(1,n+1):
        fat = fat * k
    return fat

#-----------------------------

def aproximacao_pi():
    '''
      (none) --> float 
    Calcula uma aproximacao para a constante pi, de acordo com a Fórmula 
    devido a Srinivasa Ramanujan; somando os termos até que este seja menor do que 1e-15 

    Veja a fórmula em http://en.wikipedia.org/wiki/Pi
    '''
    
    total = 0
    k = 0
    fator = 2 * math.sqrt(2) / 9801     #<=== uso da funcao pré-definida sqrt(.)
    while True:
        num = fatorial(4*k) * (1103 + 26390*k)
        den = fatorial(k)**4 * 396**(4*k)
        term = fator * num / den
        
        print("k =", k)
        print("term=", term)

        total += term
        
        print("total=", total)
        print("1/total =", 1/total)
        print()
        
        if term  < 1e-15:  
            break
        k += 1

    return 1 / total
#-------------------------------
main()

########### Veja o uso do comando
# while True:
# combinado com o uso do comando "break"
######################################
