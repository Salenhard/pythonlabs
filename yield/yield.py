# yield test
__author__ = "Vladislav Gurbatov"

def fact(n:int):
    N = 1
    sum = 0
    for a in range(1, n+1):
        for b in range(1, a+1):
            N = N * b
        sum += N
    return sum
# хз как работает... (генератор при вызове функции делает шаг в цикле)
def cycle(n:int):
    for i in range(1, n):
        yield 2 * i / fact(i)


n = int(input("Введите кол-во итераций: "))

for i in cycle(n + 1):    
    print("Результат: ", i)