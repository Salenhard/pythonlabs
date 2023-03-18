# np vs list vs tortch tensor 

__autor__ = "Влад Гурбатов"

import random
import numpy as np 
import time 
import torch
n = 100
def multiply_matrix(A:list , B:list, n:int):
    C = []
    for i in range(n*n):
        C.append(0.)
    C = matrix_fromlist(C, n)
    for row in range(n): 
        for col in range(n):
            for elt in range(n):
                C[row][col] += A[row][elt] * B[elt][col]
    return C

def matrix_fromlist(alist:list, n:int):
    k = 0
    res = []
    for idx in range(0, n):
        sub = []
        for jdx in range(0, n):
            sub.append(alist[k])
            k += 1
        res.append(sub)
    return res

start = time.time()
rand_list = []
for i in range(n*n):
    rand_list.append(random.uniform(0,100))
rand_listmat = matrix_fromlist(rand_list, n)
rand_list2 = []
for i in range(n*n):
    rand_list2.append(random.uniform(0,100))
rand_list = matrix_fromlist(rand_list, n)
rand_list2mat = multiply_matrix(rand_list, rand_list2, n)
end = time.time()
print("list time:", end - start)

start = time.time()
anp = np.random.uniform(low = 0, high = 100, size = (n, n))
anp2 = np.random.uniform(low = 0, high = 100, size = (n, n))
anp = anp * anp2
end = time.time()
print("numpy time:", end - start)

start = time.time()
att = torch.rand(n, n)
att2 = torch.rand(n, n)
torch.mul(att, att2)
end = time.time()
print("torch time:", end - start)
# вывод матрицы
