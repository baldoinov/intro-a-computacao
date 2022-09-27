"""
   Programa 05a -- p05a_celsius_fahrenheit.py
   ------------------------------------------
   Dado um número representando uma temperatura em graus Celsius,
   converter essa temperatura em graus Fahrenheit.

""" 
# -----------------------------------------------------------------------------

def main():
    graus_C = float(input("Digite uma temperatura em graus Celsius: "))

    graus_F = 9/5 * graus_C + 32

    print()
    print(graus_C, "graus Celsius correspondem a", graus_F, "graus Fahrenheit \n")
        
# -----------------------------------------------------------------------------
main()


