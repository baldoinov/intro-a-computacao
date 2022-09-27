"""
  ---- Manipulação de digitos de um número --------
  -------------------------------------------------
  Programa p33 ---------- p33_dig_consec_iguais.py
  ------------------------------------------------

  Dado um inteiro n > 0, verificar se em n há (pelo menos) 2 dígitos consecutivos iguais.

"""

def main():
    n = int(input("Insira um número inteiro: "))
    n_copy = n
    dig_atu = 0
    digitos_csc = False

    dig_ant = n % 10
    n = n // 10

    while n > 0 and not digitos_csc:
        dig_atu = n % 10

        if dig_atu == dig_ant:
            digitos_csc = True

        dig_ant = dig_atu
        n = n // 10

    if digitos_csc:
        print(f"O número {dig_atu} aparece consecutivamente em {n_copy}.")
    else:
        print(f"Não há dígitos consecutivos iguais em {n_copy}.")


main()
