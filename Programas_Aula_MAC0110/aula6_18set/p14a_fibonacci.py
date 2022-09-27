""" 
     Programa 14a  --- p14a_fibonacci.py
     ----------------------------------
     Dado n, inteiro não-negativo, este programa determina F(n), 
     o n-ésimo termo da sequência de Fibonnaci.
     
     Definicão da sequência de Fibonacci:

     F(0)=0; F(1)=1;
     F(n) = F(n-2) + F(n-1), para n>=2.  
"""
def main():
    
    n = int(input("Digite o valor de n (inteiro >=0) para calcular F(n)): "))
  
    penultimo  = -1 # definido artificialmente para ser F(-2)
    ultimo  = 1     # definido artificialmente para ser F(-1)
    cont = 0
    
    while (cont <= n):
        atual  = penultimo + ultimo
        print("Número de Fibonacci F(%d) = %d" %(cont, atual)) 
        penultimo = ultimo
        ultimo = atual
        cont  = cont + 1
    print()     
    print("Número de Fibonacci F(%d) = %4d\n" %(n,atual))
#----------------
main()

#    penultimo    ultimo      atual= penultimo + ultimo   
#    
#  
#   Inicializacao artificial para a definição valer a partir de F(0):
#    -1    1    0    1    1    2    3  .....
#   Os dois primeiros termos - 1 e 1 são artificiais (é como se
#   fossem F(-2) e F(-1) .
#   Foram definidos como os termos que antecedem F(0)
#   para que a fórmula recursiva valha para n>=0
#
#  Podemos fazer sem usar este artifício (veja o programa solucao_fibo_ex2.py)


# OBS: o programa acima imprime todos os termos da sequência até F(n),
# para n dado. Se quiséssemos imprimir apenas F(n), basta eliminar,
# ou comentar o primeiro comando print. 
# 
