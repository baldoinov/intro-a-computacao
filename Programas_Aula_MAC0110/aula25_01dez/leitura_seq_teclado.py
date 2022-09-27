
# Como fazer leitura pelo teclado de uma sequência de números inteiros
# --------------------------------------------------------------------
# Estes devem ser fornecidos separados por pelo menos um espaço em branco.
# Dar o ENTER apenas no final

print("Leitura de uma sequencia de números inteiros fornecidos pelo teclado.")
print("Digitar os inteiros separados por pelo menos um espaço em branco (vamos usar o espaço como separador).")
print("Dar o ENTER apenas no final da lista.")

print("A seguinte receita já foi vista em aula:")

entrada = input("Digite uma sequência de números inteiros e dê ENTER no final: \n")
print("entrada = ", entrada)

lista_de_strings = entrada.split()   #<==== os elementos são separados quando há pelo menos um espaço entre eles.
print("lista de strings =", lista_de_strings)

lista_de_inteiros = list(map(int, lista_de_strings))
# map aplica int para cada elemento (string)  que foi dado pelo teclado.
print("lista de inteiros = ", lista_de_inteiros)


# OBS: Se for valores reais, usar float no lugar de int
# s = list(map(float, input("Digite a lista de valores: ").split()))


###############################

print("Outra forma mais direta:")


s = list(map(int,input("Digite a lista de valores: ").split()))  #<===========
# map aplica int para cada elemento (string)  que foi dado pelo teclado.
# Estes foram separados pelo split()

# Ex: vc pode dar os valores -5, 9, 12, -6, -6, -30,  7, 21  (e ENTER no final)

print("sequencia dada = ", s)

n= len(s)

soma = 0
for i in range(n):
    soma  += s[i]
print("Soma dos elementos da sequência = ", soma)

########################################
