# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
	print(a, b, c)
print_params()
print_params(b = 25)
# print_params(c = 1, 2, 3) - ошибка в последовательности аргументов

# 2.Распаковка параметров:
values_list = [13, 'молоко', True]
values_dict = {'a' : 32, 'b' : 'хлеб', 'c' : False}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [12, 'вода']
# print_params(*values_list_2;) - несовпадение количества параметров
