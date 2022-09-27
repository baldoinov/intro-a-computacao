'''
   Arquivo: seq_sem_repeticoes_func.py
   
   Dados um inteiro positivo n e uma sequência de n números inteiros,
   construir uma sequência sem repetições (dos números dados). 
   
'''

def main():
    print("Esse programa cria uma sequência sem repetições.\n")
    n = int(input("Quantos números serão dados? "))
    seq = []

    for i in range(n):
        num = int(input("Insira um número para a sequência: "))
        if not (num in seq):
            seq.append(num)
    
    print(f"A sequência sem repetições é {seq}")


def versão_professora():
    print("Esse programa cria uma sequência sem repetições.\n")
    n = int(input("Quantos números serão dados? "))
    seq = []

    for i in range(n):
        num = int(input("Insira um número para a sequência: "))
        if not pertence_a_seq(num, seq):
            seq.append(num)

    print(f"A sequência sem repetições é {seq}")


def pertence_a_seq(m, seq):
    '''
    (int, list) -> (bool)
    '''
    n = len(seq)
    for i in range(n):
        if seq[i] == m:
            return True
    return False


main()
