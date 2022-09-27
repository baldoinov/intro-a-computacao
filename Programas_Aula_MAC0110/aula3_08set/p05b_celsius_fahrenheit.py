# -*- coding: utf-8 -*-
'''
   Programa 05b -- p05b_celsius_fahrenheit.py
   ------------------------------------------ 
   Problema:
   Dado um número representando uma temperatura em graus Celsius,
   determinar o correspondente em graus Fahrenheit.
'''
# -----------------------------------------------------------------------------

def main():
    graus_C = float(input("\n Digite uma temperatura em graus Celsius: "))

    graus_F = 9/5 * graus_C + 32
    
    print("\n", graus_C, "graus Celsius correspondem a", graus_F, "graus Fahrenheit")
        
    print("\n", graus_C,"\u00b0C", "correspondem a", graus_F,"\u00b0F\n")  # novidade! 
        
# -----------------------------------------------------------------------------
main()

# Para entender mais sobre \u00b0 (codigo para o caractere de grau), veja em: 
# https://www.rapidtables.com/code/text/unicode-characters.html
