'''
   Dados um inteiro positivo n e uma sequência com n números reais,
   determinar o número de vezes que cada número ocorre na sequência.
'''

def main():
    print("Esse programa determina a quantidade de vezes que cada número aparece em uma sequência.\n")
    n = int(input("Quantos números terá a sequência: "))

    seq = []
    ocorrencias = []

    for j in range(1, n+1):
        num = float(input(f"Digite o {j}° da sequência: "))
        k = ocorre_em(num, seq)
        if k == None:
            seq.append(num)
            ocorrencias.append(1)
        else:
            ocorrencias[k] += 1

    print("Os números e suas respectivas ocorrências são: \n")
    for p in range(len(seq)):
        print(f"{seq[p]:5}    -----{ocorrencias[p]:5} vezes.")


def ocorre_em(item, seq):
    '''
    (int, list) -> int or NoneType
    '''

    for i in range(len(seq)):
        if item == seq[i]:
            return i
    return None


main()
