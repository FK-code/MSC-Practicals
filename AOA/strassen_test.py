import numpy as np
import time

def split(matrix):  # split matrix into quarters
    row, col = matrix.shape
    # print ("row",row)
    # print ("col",col)
    # print ("marix",matrix)
    # print ("matrix.shape",matrix.shape)
    return matrix[:row//2, :col//2], matrix[:row//2, col//2:], matrix[row//2:, :col//2], matrix[row//2:, col//2:]


def strassen(a, b):
    q = len(a)
    if q == 1:  # base case: 1x1 matrix
        return a * b
    a11, a12, a21, a22 = split(a)
    b11, b12, b21, b22 = split(b)

 
    print(f"a11 \n{a11}")
    print(f"a12 \n{a12}")
    print(f"a21 \n{a21}")
    print(f"a22 \n{a22}")

    print(f"b11 \n{b11}")
    print(f"b12 \n{b12}")
    print(f"b21 \n{b21}")
    print(f"b22 \n{b22}")


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

matrix1 = np.random.randint(0, 10, size=(4, 4))
matrix2 = np.random.randint(0, 10, size=(4, 4))


print(f"matrix 1\n {matrix1}")

print(f"matrix 2\n {matrix2}")

start_time = time.time()
matrix3= strassen(matrix1, matrix2)
print(f"matrix 3\n {matrix3}")
print(f"Process finsihed in .. {time.time()-start_time}")

start_time = time.time()
byDot=np.dot(matrix1,matrix2)
print(f"by dot product \n {byDot}")
print(f"Process finsihed in .. {time.time()-start_time}")
