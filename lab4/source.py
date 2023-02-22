def find_sum(n:int):
    s = 0
    for i in range(1, n):
        i2 = i**2
        s += i2/(i2 + 2*i + 3)
    return s