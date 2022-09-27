# -*- coding: utf-8 -*-

'''
   Arquivo: num_ocorrencias.py

   Dados um inteiro positivo n e uma sequência com n números reais,
   determinar o número de vezes que cada número ocorre na sequência.

'''

def main():
    n = int(input("Digite o número de elementos da sequência: "))
    print()
    seq = []
    num_ocor = []
    
    #  Ler cada número num da sequência;
    # se num estiver na lista seq, atualizar seu número de ocorrências;
    # se não estiver, inserir num na lista seq e inserir 1 na lista num_ocor.
    i = 1
    while i <= n:
        num = float(input("Digite um número real da sequência: "))
        print("num dado=", f'{num:.2f}') 
        k = indice_pertence_lista(num, seq)
        if k == None:
            # num não está na lista seq
            seq.append(num)
            num_ocor.append(1)
        else:
            num_ocor[k] += 1
        i += 1
                                    
    print()
    print("Lista de números sem repetiçoes: ", seq)
    print()
    print("      Número       No. ocorrências")
    comp_seq = len(seq)
    i = 0
    while i < comp_seq:
        print("%12f%16d" %(seq[i], num_ocor[i]))
        i += 1
    i = 0
    while i < comp_seq:
        print(f'{seq[i]:{8}.{3}}', "   ", num_ocor[i])
        i += 1


        
#---------------------------------------------------------------

def indice_pertence_lista(item, lista):
    ''' (objeto, list) -> int ou NoneType

    Recebe um objeto item e uma lista lista.
    Retorna o índice da posição em que item ocorre na lista.
    Caso item não ocorra na lista, retorna None.
    '''
    
    comp = len(lista)
    indice = None
    i = 0
    while i < comp and indice == None:
        if item == lista[i]:
            indice = i
        else:
            i += 1
      
    return indice

#-------------------------------------------------------------------

main()

'''
   f'{value:.2f}'    # 2 after the decimal
   f'{value:{width}.{precision}}'
   f'{value}'   -- 

# notice that it adds spaces to reach the number of characters specified by width
In [1]: f'{1 + 3 * 1.5:10.3f}'
Out[1]: '     5.500'

# notice that it uses more characters than the ones specified in width
In [2]: f'{3000 + 3 ** (1 / 2):2.1f}' 
Out[2]: '3001.7'

In [3]: f'{1.2345 + 4 ** (1 / 2):9.6f}'
Out[3]: ' 3.234500'

# omitting width but providing precision will use the required characters to display the number with the the specified decimal places
In [4]: f'{1.2345 + 3 * 2:.3f}' 
Out[4]: '7.234'

# not specifying the format will display the number with as many digits as Python calculates
In [5]: f'{1.2345 + 3 * 0.5}'
Out[5]: '2.7344999999999997'

'''
