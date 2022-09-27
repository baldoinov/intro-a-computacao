def draw_grid_1():
    plus = "+"
    minus = "-" * 4
    bars = "|" + " " * 4 + "|" + " " * 4 + "|"
    print(plus, minus, plus, minus, plus, sep="")
    print(bars, bars, bars, bars, sep="\n")
    print(plus, minus, plus, minus, plus, sep="")
    print(bars, bars, bars, bars, sep="\n")
    print(plus, minus, plus, minus, plus, sep="")


def draw_grid_2():
    first = "+----+----+----+"
    bars = "|    |    |    |"
    print(first)
    print(bars, bars, bars, bars, sep="\n")
    print(first)
    print(bars, bars, bars, bars, sep="\n")
    print(first)
    print(bars, bars, bars, bars, sep="\n")
    print(first)

draw_grid_2()
