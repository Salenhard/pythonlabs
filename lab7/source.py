def sum_cicle(n:int, m:int):
    s = 0
    for i in range(1, n):
        for j in range(1, m):
            s += (j-i+1)/(i+j)
    return s