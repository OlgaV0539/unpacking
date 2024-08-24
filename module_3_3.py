def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


def print_params(a=25, b=False, c=(1, 3, 5), d='to be or not to be'):
    print(a, b, c, d)


print_params()


def print_params():
    print(3.14, 'Shakespeare')


print_params()


def print_params(*args):
    print(args)


values_list = [35, 'Example', True]
print_params(*values_list)
values_list_2 = [21, 'Example2']
print_params(*values_list_2)


def print_params(**kwargs):
    print(kwargs)


values_dict = {'a': 35, 'b': 'Example', 'c': True }
print_params(**values_dict)



