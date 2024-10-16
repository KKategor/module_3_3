# Task "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a = 1, b = 'строка')
print_params(c = True)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['Слово', 3.2, [True, False]]
values_dict = {'a' : 'сказка', 'b' : False, 'c' : '88'}
print_params(* values_list)
print_params(** values_dict)
values_list_2 = ("Текст", 4.4)
print_params(*values_list_2, 42)