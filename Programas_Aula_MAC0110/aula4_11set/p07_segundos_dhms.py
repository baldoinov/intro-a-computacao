"""
   Program 07 - p07_segundos.py
   ----------------------------
   Dado um número inteiro representando uma quantidade de segundos,
   determinar quantos dias, horas, minutos e segundos correspondem
   ao inteiro dado.
"""

# ---------------------------------------------------------------------

segundos = int(input("Digite um inteiro (quantidade de segundos): "))

segundos_dados = segundos           # precisaremos mais tarde
segundos_num_dia = 24 * 60 * 60     # um dia tem 24 horas

dias = segundos // segundos_num_dia 
segundos = segundos % segundos_num_dia   # segundos restantes após descontar os dias inteiros 
               
horas = segundos // 3600     # uma hora tem 3600 segundos
segundos  = segundos % 3600

minutos =  segundos  // 60    # um minuto tem 60 segundos
segundos = segundos % 60

print()
print(segundos_dados, "segundos correpondem a", dias, "dias,",
      horas, "horas,", minutos, "minutos e", segundos, "segundos")

# ---------------------------------------------------------------------
#
#  q = a // b
#  q será o maior inteiro menor ou igual a (a / b)
#
#  r = a % b
#  r será  (a - (a // b) * b)
#
# ---------------------------------------------------------------------
