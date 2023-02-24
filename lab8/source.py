import numpy as np

def print_massive(a:list, n:int):
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j], " ", end='')
        print()
        

def matrowchange(a:list, n:int):
    """Меняет колонны матрицы местами 1 с послденим и т.д."""
    b = np.zeros(n)
    for i in range(n//2):
        b[0:n] = a[0:n, i]
        a[0:n, i] = a[0:n, n-i-1]
        a[0:n, n-i-1] = b[0:n]
    return a

def create_array(n:int):
    return np.random.randint(0, 100, size = (n, n))
