def do_twice(f, s):
    f(s)
    f(s)


def print_twice(s):
    print(s)
    print(s)


def do_four(f, p):
    do_twice(f, p)
    do_twice(f, p)


do_four(print, 'test')
