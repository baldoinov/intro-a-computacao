def right_justify(s):
    """
    (str) -> str
    """

    len_s = len(s)
    y = 70 - len_s    # number of spaces left up to the 70th column
    print((" " * y) + s)


right_justify('Vitor')
