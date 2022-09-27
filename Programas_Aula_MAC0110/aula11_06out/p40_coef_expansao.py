'''
   Programa p40 --- p40_coef_expansao.py
   
   Usando as função coef_bin(.,.) definida no programa function.py,

   escreva um programa que lê um inteiro n, n >= 0 e imprime os 
   coeficientes da expansão de (x+y) elevado a n.

'''
import function   # no programa function está definido a funcao coef_bin(.,.)

def main():
    n = int(input("Digite um inteiro positivo (n>=0): ")) 
    print("n = ",n) 
    
    k = 0
    while k <= n:
        print("Coeficiente de x^%d y^%d: %d"%(n-k, k, function.coef_bin(n, k)))
        k += 1
    
main()


