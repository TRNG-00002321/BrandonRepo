import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# a = np.array(42)
# b = np.array([1,2,3,4,5])
# c = np.array([1,2,3], [4,5,6])
# d = np.array([[1,2,3]],[[1,2,3],[4,5,6]])
#
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# import numpy as np
#
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]]])
#
# print(a.ndim)  # 0D
# print(b.ndim)  # 1D
# print(c.ndim)  # 2D
# print(d.ndim)  # 3D


#-------------------------------------------------------

# arr = np.array([1,2,3,4], ndim=5)
# print(arr)
# print('number of dimensions :', arr.ndim)

# doesnt work?

#-------------------------------------------------------
#
# arr = np.array([1,2,3,4])
# print(arr[0])

                                                #slicing
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])

#slicing elements from index 4 to end of arr
arr2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr2[4:])

#slicing elements from beginning to index 4 (not included)
arr3 = np.array([1,2,3,4,5,6,7,8,9])
print(arr3[0:4])
#-------------------------------------------------------
                                                #negative slicing
arr = np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])

#-------------------------------------------------------
                                                #slicing 2d arr
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])

#-------------------------------------------------------
                                                #shaping and reshaping
