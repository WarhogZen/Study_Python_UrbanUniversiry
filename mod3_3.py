def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
# task1
print_params()
print_params(3)
print_params(3,False)
print_params(4,[1],{'d':2})
print_params(b = 25)
print_params(c = [1,2,3])

# task2
values_list = [5, False, ([],[],[])]
values_dict = {'a':True, 'b':4.3, 'c':[6,6,6]}
print_params(*values_list)
print_params(**values_dict)

#task3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)