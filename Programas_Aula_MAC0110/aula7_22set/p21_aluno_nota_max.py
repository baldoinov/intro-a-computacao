# -*- coding: utf-8 -*-
"""
   Programa 20 --- 
  
   Problema:  
   Dado n, e a seguir n notas correspondentes aos alunos 1, 2 ,...,n,
   determinar o número de um  aluno que teve a maior nota, e qual foi sua nota.
   (Se tiver vários alunos com nota máxima, basta indicar um deles.)

"""

def main():
    #    n             :   quantidade de alunos
    #    aluno         :   vai de 1 a n
    #    nota          :   nota de um aluno
    #    nota_max      :   nota mais alta
    #    aluno_nota_max:   número do aluno com nota máxima

    n = int(input("Digite a quantidade de alunos: ")) 
    aluno = 1 
    nota_max  = -1
    aluno_nota_max = 0 
    
    while aluno <= n:
        nota  = int(input("Digite a nota do aluno: "))
        print("Nota do aluno", aluno, " ===>  ", nota)
        if nota > nota_max:
            nota_max = nota
            aluno_nota_max = aluno 
        aluno = aluno + 1
        
    print("Número do aluno com nota máxima = ", aluno_nota_max, "  nota máxima = ", nota_max)
    
#-------------
main()


        
        
