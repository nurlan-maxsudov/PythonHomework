import numpy as np

def task1():
    vector = np.arange(10, 49)
    return vector
    
def task2():
    array = np.arange(0, 9).reshape(3, 3)
    return array

def task3():
    matrix = np.identity(3)
    return matrix

def task4():
    arr = np.random.randint(0, 9, size=(3, 3, 3))
    return arr

def task5():
    arr = np.random.randint(3, 15, size=(10, 10))
    mxm = arr.max()
    mnm = arr.min()
    
    return mxm, mnm

def task6():
    arr = np.random.randint(10, 50, size=(30))
    mean_value = arr.mean()
    return mean_value

def task7():
    matrix = np.random.randint(1, 6, size=(5, 5))
    magnitude = np.linalg.norm(matrix)
    
    normalized_matrix = matrix / magnitude
    
    return normalized_matrix

def task8():
    matrix1 = np.full((5, 3), 2)
    matrix2 = np.full((3, 2), 3)
    
    result = np.matmul(matrix1, matrix2)
    
    return result

def task9():
    matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[2, 3, 4], [1, 9, 8], [10, 6, 7]])
    
    result = np.dot(matrix1, matrix2)
    
    return result

def task10():
    matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    transposed_matrix = matrix.transpose()
    return transposed_matrix

def task11():
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    determinant = np.linalg.det(matrix)
    return determinant

def task12():
    matrix1 = np.full((3, 4), 2)
    matrix2 = np.full((4, 3), 3)
    result = np.matmul(matrix1, matrix2)
    return result

def task13():
    matrix = np.random.randint(1, 10, size=(3,3))
    x = np.array([[1],
                 [2],
                 [3]])
    
    result = np.matmul(matrix, x)
    return result


def task14():
    matrix = np.array([[2, 3, 1],
                        [4, 7, 2],
                        [3, 5, 1]])
    b = np.array([[2],
                  [2],
                  [2]])
    
    result = np.linalg.solve(matrix, b)
    return result



def task15():
    matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])
    print("Column-wise: ")
    for i in range(5):
        print(sum((matrix[:, i])), end=" ")
    
    print("\nRow-wise sum: ")
    for i in range(5):
        print(sum(matrix[i, :]))


    
    