#1
def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)
print_params()
print_params(a = False, c = 10)
print_params(b = 25)            #работает
print_params(c = [1, 2, 3])     #работает
print('')

#2
values_list = ['String', False, 4]
values_dict = {'a': True, 'b': 1.43, 'c': 'Text'}
print_params(*values_list)
print_params(**values_dict)
print('')

#3
values_list_2 = [1.25, 'WoW']
print_params(*values_list_2, 42)    #работает