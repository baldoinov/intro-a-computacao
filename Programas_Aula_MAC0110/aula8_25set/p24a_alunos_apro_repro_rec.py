# -*- coding: utf-8 -*-

'''
   Programa P24a-----------p24a_alunos_apro_repro_rec.py
   -----------------------------------------------------
   Problema:
   Dados um número inteiro positivo n e uma sequência com n notas
   finais de MAC0110), determinar quantos alunos:
   - estão de recuperação: nota final maior ou igual a 3 e menor do que 5;
   - foram reprovados: nota final menor do que 3;
   - foram aprovados: nota final maior ou igual a 5;
   - tiveram um desempenho excelente: nota maior do que 8.
'''
# --------------------------------------------------------------------------

def main():
    
    n = int(input("Digite a quantidade de alunos: "))
    
    aprovados   = 0
    recuperacao = 0
    reprovados  = 0
    excelentes  = 0
     
    cont = 0
    while cont < n:
        nota = float(input("Digite uma nota (entre 0 e 10): "))
        if nota >= 5.0:
            aprovados = aprovados + 1
            if nota > 8.0:
                excelentes = excelentes + 1
        else:
            if nota >= 3.0:
                recuperacao = recuperacao + 1
            else:
                reprovados = reprovados + 1
        cont = cont + 1
     
    print("\nNúmero de alunos excelentes =", excelentes)
    print("Número de alunos aprovados =", aprovados)
    print("Número de alunos de recuperação =", recuperacao)
    print("Número de alunos reprovados =", reprovados)
    
# ------------------------------------------------------------------------
main()

###########################################################
