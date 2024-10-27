import numpy as np
def generate_valid_matrix(k):
    valid_matrix = []
    for i in range(2**k):
        binary_str = format(i, f'0{k}b')
        if binary_str.count('0') != k and binary_str.count('1') != k and binary_str.count('1') != 1:
            valid_matrix.append([int(bit) for bit in binary_str])
    return np.array(valid_matrix)
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for row {i+1}, column {j+1}: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose
n = int(input("Enter the code word:"))
k = int(input("Enter the data word:"))
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
D = input_matrix(rows, cols)
print("Entered matrix:")
print(D)
r = n - k

a = np.identity(k, int)
matrix = generate_valid_matrix(k)

g = []
for i in range(0, 3):
    concatenated_array = np.concatenate((a[i], matrix[i]), axis=0)
    g.append(concatenated_array)


for array in g:
    print(array)
G=np.array(g)
C = np.dot(D, G)
C=C%2
print(C)
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
R = input_matrix(row, col)
p = transpose_matrix(matrix)
h=[]
for i in range(0, 3):
    concatenated_array = np.concatenate(( p[i],a[i]), axis=0)
    h.append(concatenated_array)
h1=transpose_matrix(h)
print(h1)
s=np.dot(R, h1)
s=s%2
print(s)
for i, arr in enumerate(h1):
    if (s == arr).all():
        print("There is error in R,"+str(i)+" positions counting from left")
        break
else:
    print("correct Message")

