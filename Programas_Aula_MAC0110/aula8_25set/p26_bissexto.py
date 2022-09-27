
"""
   Programa P26:           p26_bissexto.py
   -------------------
   Este programa recebe um ano como entrada e determina se ele é bissexto.
   Def: Um ano é bissexto se ele é divisível por 4, 
   e não é divisivel por 100; ou quando ele é divisível por 400.  

def main():
    
    ano = int(input("Forneca o ano a ser testado: "))
  
    if (((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0)):
        print("O ano %d é bissexto.\n" %ano)
    else:
        print("O ano %d não é bissexto.\n" %ano)
# -------------
main()
 
"""
#   -------------------------------------------------
#   O programa abaixo resolve o problema acima e fornece uma 
#   mensagem (justificativa) quando o ano não é bissexto.

def main():
    
    ano = int(input("Forneca o ano a ser testado: "))
  
    if (((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0)):
        print("O ano %d é bissexto.\n" %ano)
    else:
        print("O ano %d não é bissexto." %ano)
        if (ano % 4 != 0):
            print("Razão: ", ano, "não é divisível por 4")
        else:
            print("Razão: ", ano, "é divisível por 100 e não é divisível por 400")
        
# ---------------------
main()
