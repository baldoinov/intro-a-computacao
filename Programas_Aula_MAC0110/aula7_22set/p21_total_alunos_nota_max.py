# -*- coding: utf-8 -*-
"""
   Programa 19 ---  
   ---------------------
   Problema:  
   Dado n, e a seguir n notas correspondentes aos alunos 1, 2 ,...,n,
   determinar o número de alunos que tiveram a maior nota, e qual é essa nota máxima.

"""

def main():
    #    n :              quantidade de alunos
    #    aluno:           vai de 1 a n
    #    nota     :       nota de um aluno
    #    nota_max :       nota mais alta
    #    quanti_max:      quantidade de alunos com nota máxima

    n = int(input("Digite a quantidade de alunos: ")) 
    aluno = 1 
    nota_max  = -1
    
    while aluno <= n:
        nota  = int(input("Digite a nota do aluno:"))
        print("Nota do aluno", aluno, " ===>  ", nota)
        
        if nota >= nota_max:
            if nota > nota_max:
                quanti_max = 1
                nota_max = nota
            else:                # sabemos que nota == nota_max 
                quanti_max = quanti_max + 1      
        aluno = aluno + 1
        
    print("Quantidade de alunos com nota máxima = ", quanti_max)
    print("Nota máxima =", nota_max)
    
#-------------
main()


        
        
