# p=2
# q=2

# matrix = [[0 for row in range(p)] for col in range(q)]
# print (matrix)

# import numpy as np
  
# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))
  
  
# print("Enter matrix 1: ")
# entries = list(map(int, input().split()))
# matrix1 = np.array(entries).reshape(R, C)

# print("Enter matrix 2: ")
# entries = list(map(int, input().split()))
# matrix2 = np.array(entries).reshape(R, C) 


# print(f"matrix 1 \n{matrix1}")
# print(f"matrix 2 \n{matrix2}")


# def strassen(x,y):
#     return x*y


# a = matrix1[0][0]
# b = matrix1[0][1]
# c = matrix1[1][0]
# d = matrix1[1][1]

# e = matrix2[0][0]
# f = matrix2[0][1]
# g = matrix2[1][0]
# h = matrix2[1][1]


# p1 = strassen(a, f - h)
# p2 = strassen(a + b, h)	
# p3 = strassen(c + d, e)	
# p4 = strassen(d, g - e)	
# p5 = strassen(a + d, e + h)	
# p6 = strassen(b - d, g + h)
# p7 = strassen(a - c, e + f)


# c11 = p5 + p4 - p2 + p6
# c12 = p1 + p2		
# c21 = p3 + p4		
# c22 = p1 + p5 - p3 - p7

# entries=[c11,c12,c21,c22]
# matrix3 = np.array(entries).reshape(R, C) 
# print("Strassen multipled Matrix")
# print(matrix3)

# stack overflow

# import numpy as np
# def straight(a, b): 
#     if len(a[0]) != len(b): return "Matrices are not m*n and n*p" 
#     p_matrix = np.zeros((len(a), len(b[0])))
#     p_matrix += [[np.sum([a[i][k] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
#     return p_matrix
# def split(matrix):  # split matrix into quarters
#     row, col = matrix.shape
#     print ("row",row)
#     print ("col",col)
#     print ("marix",matrix)
#     print ("matrix.shape",matrix.shape)
#     return matrix[:row//2, :col//2], matrix[:row//2, col//2:], matrix[row//2:, :col//2], matrix[row//2:, col//2:]
# def strassen(a, b):
#     q = len(a)
#     if q == 1 :  # base case: 1x1 matrix
#         return a * b
#     a11, a12, a21, a22 = split(a)
#     print("split a")
#     print("split b")
#     b11, b12, b21, b22 = split(b)
#     p1 = strassen(a11 + a22, b11 + b22)  # p1 = (a11 + a22) * (b11 + b22)
#     p2 = strassen(a21 + a22, b11)        # p2 = (a21 + a22) * b11
#     p3 = strassen(a11, b12 - b22)        # p3 = a11 * (b12 - b22)
#     p4 = strassen(a22, b21 - b11)        # p4 = a22 * (b21 - b11)
#     p5 = strassen(a11 + a12, b22)        # p5 = (a11 + a12) * b22
#     p6 = strassen(a21 - a11, b11 + b12)  # p6 = (a21 - a11) * (b11 + b12)
#     p7 = strassen(a12 - a22, b21 + b22)  # p7 = (a12 - a22) * (b21 + b22)
#     c11 = p1 + p4 - p5 + p7              # c11 = p1 + p4 - p5 + p7
#     c12 = p3 + p5                        # c12 = p3 + p5
#     c21 = p2 + p4                        # c21 = p2 + p4
#     c22 = p1 + p3 - p2 + p6              # c22 = p1 + p3 - p2 + p6
#     c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
#     return c
# def check():
#     a = np.random.randint(0, 10, size=(4, 4))
#     b = np.random.randint(0, 10, size=(4, 4))
#     print(a)
#     print(b)
#     assert (strassen(a, b) == straight(a, b)).all()
#     assert (np.array(strassen(a, b)) == np.dot(a, b)).all()
#     print('Hooray!')
# check()

# implementation
import numpy as np

def split(matrix):  # split matrix into quarters
    row, col = matrix.shape
    # print ("row",row)
    # print ("col",col)
    # print ("marix",matrix)
    # print ("matrix.shape",matrix.shape)
    r=row//2
    c=col//2
    return matrix[:r, :c], matrix[:r, c:], matrix[r:, :c], matrix[r:, c:]


def strassen(a, b):
    q = len(a)
    if q == 1:  # base case: 1x1 matrix
        return a * b
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)
    p1 = strassen(a11 + a22, b11 + b22)  # p1 = (a11 + a22) * (b11 + b22)
    p2 = strassen(a21 + a22, b11)        # p2 = (a21 + a22) * b11
    p3 = strassen(a11, b12 - b22)        # p3 = a11 * (b12 - b22)
    p4 = strassen(a22, b21 - b11)        # p4 = a22 * (b21 - b11)
    p5 = strassen(a11 + a12, b22)        # p5 = (a11 + a12) * b22
    p6 = strassen(a21 - a11, b11 + b12)  # p6 = (a21 - a11) * (b11 + b12)
    p7 = strassen(a12 - a22, b21 + b22)  # p7 = (a12 - a22) * (b21 + b22)
    c11 = p1 + p4 - p5 + p7              # c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5                        # c12 = p3 + p5
    c21 = p2 + p4                        # c21 = p2 + p4
    c22 = p1 + p3 - p2 + p6              # c22 = p1 + p3 - p2 + p6
    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 
    return c

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter matrix 1 row wise separated by space: ")
entries = list(map(int, input().split()))
matrix1 = np.array(entries).reshape(R, C)
print(f"matrix 1\n {matrix1}")

print("Enter matrix 2 row wise separated by space: ")
entries = list(map(int, input().split()))
matrix2 = np.array(entries).reshape(R, C)
print(f"matrix 2\n {matrix2}")

matrix3= strassen(matrix1, matrix2)
print(f"ANS by Strassen Multiplication \n {matrix3}")

byDot=np.dot(matrix1,matrix2)
print(f"ANS by dot product (numpy)\n {byDot}")

# https://martin-thoma.com/strassen-algorithm-in-python-java-cpp/
# https://stackoverflow.com/questions/12867099/strassen-matrix-multiplication-close-but-still-with-bugs
# https://www.tutorialspoint.com/design_and_analysis_of_algorithms/design_and_analysis_of_algorithms_strassens_matrix_multiplication.htm