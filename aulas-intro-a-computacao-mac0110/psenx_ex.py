"""
   arquivo: senx.py

   Dados x real e n natural, calcular uma aproximação para sen(x) 
   através dos n primeiros termos da série.
 
    sen x = x/1!  - x^3/3!  + x^5/5! -  ... + (-1)^k x^(2k+1)/(2k +1)! + ...
    
   (Importante: Veja como cuidar da mudança de sinal dos termos.)
   (Importante: Veja como gerar um termo a partir do anterior.)

   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========
"""
import math


def main():
    print("Esse programa calcula uma aproximação para sen(x)" 
          " a partir dos n primeiros termos de uma série.\n")

    x = float(input("Insira um número real x (x ~ 0): "))
    n = int(input("Insira um número para n: "))

    soma = x
    termo = x

    for k in range(1, n):
        termo = -(termo * x * x) / ((2 * k) * (2 * k + 1))
        soma += termo
    
    print(f"A aproximação de sen(x) pelo programa é: {soma}\n"
          f"A aproximação usando math.sin(x) é: {math.sin(x)}")


main()
