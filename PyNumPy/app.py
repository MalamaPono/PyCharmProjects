import numpy as np

def func():
    # dot product
    a = np.array([1, 3])
    b = np.array([5, 4])
    print(np.dot(a, b))

    # dot product speed test
    from timeit import default_timer as timer
    a = np.random.randn(1000)
    b = np.random.randn(1000)

    A = list(a)
    B = list(b)

    trials = 1000

    def dot1():
        dot = 0
        for i in range(len(A)):
            dot += A[i] * B[i]
        return dot

    def dot2():
        return np.dot(a, b)

    start = timer()
    for t in range(trials):
        dot1()
    end = timer()
    t1 = end - start

    start = timer()
    for t in range(trials):
        dot2()
    end = timer()
    t2 = end - start

    print('list calculation', t1)
    print('np.dot', t2)
    print('ratio', t1 / t2)

    # multidimensional arrays
    a = np.array([[1, 2, 3], [3, 4, 9], [1, 2, 4]])

    # inverse
    print(np.linalg.inv(a))

    # det
    print(np.linalg.det(a))

    # diagonal elements
    print(np.diag(a))

    # new axis
    a = np.ones((3, 4), dtype=int)
    b = a[:, np.newaxis]
    print(b)

a = np.ones((3, 4), dtype=int)
b = np.ones((3, 4), dtype=int)
c = np.hstack((a,b))
print(c)





# other useful methods

# array = np.zeros((3,4),dtype=int)
# array = np.ones((3,4),dtype=int)
# array = np.full((3,4),5,dtype=int)
# array = np.random.random((3,4))
# print(array)
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# print(a.itemsize)
#
# dimensions_inch = np.array([1,2,3])
# dimensions_cm = dimensions_inch * 2.54
# print(dimensions_cm)

# print(array[0,0])
# print(array > 0.2)
# print(array[array>0.5])
# print(np.sum(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.round(array))

# first = np.array([1,2,3])
# second = np.array([1,2,3])
# sum_array = first + second + 2
# sum_array = first+second
# mult_array = first*second
# difference_array = first - second
# quotient_array = first/second