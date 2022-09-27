'''
 * Este programa determina todos os primos menores que n, para um dado n.
 * Para isso, usa o metodo conhecido como o Crivo de Eratóstenes.
 *
 * O programa faz uso de um vetor a[0..n-1] que é inicializado com 1.
 * (Note que os índices 1..n-1 sao exatamente os números que desejamos 
 *  descobrir se são primos ou não.)
 * 
 * No final, as entradas desse vetor serão 0 ou 1, sendo que 
 *   a[i] = 1 indica que i é primo e
 *   a[i] = 0 indica que i não é primo.
 * 
 *
'''

def main():
    n = int(input("Dê um valor para n < 10000: "))
    a = [1]* (n + 1)

    a[0] = a[1] = 0
    raizn = int(n**(1/2))
    
    for i in range(2, (raizn+1)):
        if a[i] == 1:
            for j in range(2, (n//i + 1)):
                a[i * j] = 0
        
    cont = 0
    print("Os números primos menores que n são: ", end="")
    for i in range(2, n):
        if a[i] == 1:
            print(i, end=" ;")
            cont += 1

    print(f"\n\nO total de número primos menores que n é {cont}")


main()
