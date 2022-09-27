'''
   Dados um inteiro positivo n e uma sequência com n números reais,
   determinar o número de vezes que cada número ocorre na sequência.
'''
#--------------------------------------------------------------------------

def main():
    n = int(input("Digite o número de elementos da sequência: "))
    
    #  A lista seq terá os números lidos sem repetições. 
    #  Para cada i, num_ocorrencias[i] representa o número de 
    #  ocorrências de seq[i] na sequência de entrada.
    
    seq = []
    num_ocorrencias = []
    
    # Ler cada número num da sequência;
    # se num estiver na lista seq, atualizar seu número de ocorrências;
    # se não estiver, inserir num na lista seq e inserir 1 na lista
    # num_ocorrencias.

    for i in range(n):
        num = float(input("Digite um número real da sequência: "))
        k = indice_pertence_lista(num, seq)
        if k == None:    # num não está na lista seq
            seq.append(num)             # guarda num em seq 
            num_ocorrencias.append(1)   # e marca que num ocorreu 1 vez (por enquanto)
        else:
            num_ocorrencias[k] += 1     # como k já ocorreu, acrescento 1 na contagem de num_ocorrencias[k]
                                        
    print("\nLista de números sem repetições: ", seq)
    print("\nLista de números de ocorrências: ", num_ocorrencias)

    print("\nOs números sem repetições e seus números de ocorrências são:")
    print("\n         Número      No. ocorrências")
    for i in range(len(seq)):
        print("%15f%15d" %(seq[i], num_ocorrencias[i]))
   
#--------------------------------------------------------------------------

def indice_pertence_lista(item, lista):
    ''' (objeto, list) -> int ou NoneType

    Recebe um objeto item e uma lista lista.
    Retorna o índice da posição em que item ocorre na lista.
    Caso item não ocorra na lista, retorna None.
    '''
    
    comp = len(lista)
    i = 0
    while i < comp:
        if item == lista[i]:
            return i
        else:
            i += 1
      
    return None


#--------------------------------------------------------------------------
main()

