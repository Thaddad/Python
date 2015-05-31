def do_twice(f,arg):
    f(arg)
    f(arg)

def print_spam():
    print('spam')

do_twice(print_spam)
