"""
  Calcular a soma
       1 - 1/2  + 1/3  - 1/4  + ... + 1/9999 - 1/10000

a) adição dos termos da direita para a esquerda

b) adição dos termos da esquerda para a direita

c) adição separada dos termos positivos e dos termos negativos da esquerda para a direita

d) adiçao separada dos termos positivos e dos termos negativos da direita para a esquerda
    
Compare e discuta os resultados obtidos.

"""
def main():
    a()
    b()
    c()
    d()


# a) adição dos termos da direita para a esquerda
def a():
    num = -1
    soma_a = 0
    for k in range(10000, 0, -1):
        soma_a = soma_a + (num/k)
        num = - num
    print(f"Soma dos termos da direita para a esquerda: {soma_a}")


# b) adição dos termos da esquerda para a direita
def b():
    num = 1
    soma_b = 0
    for k in range(1, 10001):
        soma_b = soma_b + (num/k)
        num = - num
    print(f"A soma dos termos da esquerda para a direita: {soma_b}")


# c) adição separada dos termos positivos e dos termos negativos da esquerda para a direita
def c():
    soma_p = 0
    soma_n = 0
    for k in range(1, 10000, 2):
        soma_p += (1/k)
    for i in range(2, 10001, 2):
        soma_n += (1/i)
    soma_c = soma_p - soma_n
    print(f"A soma separada dos termos positivos e negativos da esquerda para a direita: {soma_c}")


# d) adiçao separada dos termos positivos e dos termos negativos da direita para a esquerda
def d():
    soma_p = 0
    soma_n = 0
    for k in range(9999, 0, -2):
        soma_p += (1/k)
    for i in range(10000, 1, -2):
        soma_n += (1/i)
    soma_d = soma_p - soma_n
    print(f"A soma separada dos termos positivos e negativos da direita para a esquerda: {soma_d}")


main()
