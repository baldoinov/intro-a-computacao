import math

def main():
    print(f"-" * 74)
    print("ALGUMAS APROXIMAÇÕES PARA O VALOR DE PI:")
    print("(utilizamos math.pi que é 3.141592653589793)")
    print("-" * 74)

    pi = math.pi

    # Método 1 ----------------------------------

    print("\nMétodo 1 - Valor aproximado para PI utilizando o Método dos Retângulos")
    eps = float(input("Digite um número (> 0 e < 1) para epsilon: "))
    i = 0
    k = 2**i

    piAproxRetangulos = 4 * areaMetodoRetangulos(0.0, 1.0, k)

    while math.fabs(piAproxRetangulos - pi) >= eps:
        i += 1
        k = 2**i
        piAproxRetangulos = 4 * areaMetodoRetangulos(0.0, 1.0, k)
    print(f"Número de retângulos considerados para o cálculo da última área: {k}")
    print(f"Valor aproximado para pi: {piAproxRetangulos}\n")

def f(x):
    """ (float) -> float
    Recebe um numero real x e se (1.0-x*x) for positivo, retorna
    a raiz quadrada de (1.0-x*x); em caso contrario, retorna 0.
    Obs.: para determinar a raiz quadrada é utilizada a funcao sqrt do
    modulo math.
    """
    if (1.0 - x * x) > 0:
        return math.sqrt(1.0 - x * x)
    else:
        return 0

# -------------------------------------------------------------------------

def areaMetodoRetangulos(a, b, k):
    """ (float, float, int) -> float

    Recebe dois numeros reais a e b, com a < b, e um inteiro positivo k.
    Esta funcao retorna um valor aproximado para a area sob a funcao f(x),
    no intervalo [a, b], calculada pelo metodo dos retangulos, utilizando
    k retangulos.
    """

    delta_x = (b-a)/k
    area_função = 0.0
    i = 0
    p = 2**i
    while p < k+1:
        area_função += f(a + p*delta_x) * delta_x
        i += 1
        p = 2** i
    return area_função

main()