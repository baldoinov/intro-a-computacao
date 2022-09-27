"""
   arquivo: cosx.py
   ---------------

   Dados x real e n natural, calcular uma aproximação para cos(x) 
   através dos n primeiros termos da série.
 
    cos x = 1 - x^2/2!  + x^4/4!  - x^6/6!  + ... + (-1)^k x^(2k)/ (2k)! + ...

   OBS: Aproximacao é boa em torno do zero. Forneça x pequeno (em radianos)  <=========

"""
from math import cos

def main():
    print("Esse programa calcula uma aproximação para cos(x)")
    x = float(input("Insira um valor para x: "))
    n = int(input("Insira uma valor para n (natural): "))

    soma = 1
    termo = 1
    for i in range(1, n+1):
        termo = -(termo*x*x)/((2*i-1)*(2*i))
        soma += termo
    print(f"A aproximação de cos({x}) pelo programa é {soma}")
    print(f"A aproximação de cos({x}) pelo módulo math é {cos(x)}")


main()
