# -*- coding: utf-8 -*-
"""
  -----------------------------------------------
  Comando  "if-else"  --- uso de elif = else+if ---   "if-elif"  
  -------------------------------------------------------------
  Programa P27a 
  -------------
   A Confederação Brasileira de Natação promoverá eliminatórias
   para o próximo campeonato mundial e divulgou a tabela a seguirg
   classificando as categorias de acordo com a idade do atleta.
     CATEGORIA            IDADE
     Infantil             5 a 10 anos
     Juvenil              11 a 17 anos
     Sênior               Maior ou igual a 18 anos

   Dados o número n de nadadores e as idades de n nadadores,
   imprimir a idade e a categoria em que cada nadador irá competir,
   de acordo com a tabela acima.

"""
# ------------------------------------------------------------------

def main():
    n = int(input("Digite o número de nadadores: "))

    cont = 1
    while cont <= n:
        idade = int(input("Digite a idade de um nadador: "))
        
        print("Idade:", idade)
        
        if idade < 5:
            print("Não existe categoria para essa idade.")
        else:
            # neste ponto sabemos que idade >= 5
            if idade <= 10:
                # neste ponto sabemos que idade >= 5 e <= 10
                print("Categoria: Infantil")
            else:
                # neste ponto sabemos que idade > 10
                if idade <= 17:
                    # neste ponto sabemos que idade > 10 e <= 17
                    print("Categoria: Juvenil")
                else:
                    # neste ponto sabemos que idade > 17
                    print("Categoria: Sênior")
                    
        cont = cont + 1
           
#----------------------------------------------------------------------------
main()
