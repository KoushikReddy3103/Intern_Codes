import numpy as np

def levenstein_dist(str_1,str_2):
    size_a = len(str_1) + 1
    size_b = len(str_2) + 1
    matrix = np.zeros((size_a,size_b))
    for i in range(size_a):
        matrix[i,0] = i
    for j in range(size_b):
        matrix[0,j] = j
    
    for i in range(1,size_a):
        for j in range(1,size_b):
            if str_1[i-1] == str_2[i-1]:
                matrix[i,j] = min(matrix[i-1, j-1], matrix[i-1,j] + 1, matrix[i,j-1]+1)
            else:
                matrix[i,j] = min(matrix[i-1, j]+1, matrix[i-1,j-1]+1, matrix[i,j-1]+1)
    return matrix[size_a-1,size_b-1]