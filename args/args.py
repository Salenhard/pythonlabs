#Даны натуральное число n, действительные числа a1,..., an. Вычислить:
#(sqrt(ai)-ai)**2 
# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136

import source
import sys
__author__ = "Влад Гурбатов"
# записываем аргументы в переменую args [1:] - с 1 до последней
args = sys.argv[1:]
# match - аналог switch c++ поддерживает разные типы данных
match args:

    # случай если ничего не было передано
    case []:
        print("программа запущена без аргументов")
        # ввод размера массива
        n = int(input("Введите размер массив: "))
        a = source.create_array(n)
        print("Данный массив:")
        source.print_array(a)
        print(f"Результат: {source.sum_array(a):.4f}")
        # случай если было введено help
    case ['help']:
        print("справка: введите массив для выполнения суммирования по формуле: (sqrt(ai)-ai)**2")
        # случай если был передан массив
    case['sum', *other]:
        numbers =[float(x) for x in other]
        source.print_array(numbers)
        print(f"Результат: {source.sum_array(numbers):.4f}")
    

