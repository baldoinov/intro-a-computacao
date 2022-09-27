"""
   Programa 04 - Tempo em segundos  -- p04_tempo_em_segundos.py
   --------------------------------------------------------------
   Dados três números inteiros não negativos horas, minutos e segundos,
   representando o tempo gasto para uma tarefa,
   determinar o tempo correspondente em segundos. 

   Ex: Dados: 13   42  e 15, correspondentes a 
       13 horas, 42 minutos e 15 segundos, 
       temos que 13 x 3600 + 42 x 60 + 15 = 49335 segundos.
"""

# ---------------------------------------------------------------------------
def main():
    horas = int(input("Digite um inteiro para horas: "))
    minutos = int(input("Digite um inteiro < 60 para minutos: "))
    segundos = int(input("Digite um inteiro < 60 para segundos: "))
    
    total_segundos = horas * 3600 + minutos * 60 + segundos

    print()
    print(horas, "horas,", minutos, "minutos e", segundos,  
          "segundos correspondem a", total_segundos, "segundos.")
    
# ----------------------------------------------------------------------------    
main()
