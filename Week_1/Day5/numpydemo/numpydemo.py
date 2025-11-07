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
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5])

#slicing elements from index 4 to end of arr
# arr2 = np.array([1,2,3,4,5,6,7,8,9])
# print(arr2[4:])

#slicing elements from beginning to index 4 (not included)
# arr3 = np.array([1,2,3,4,5,6,7,8,9])
# print(arr3[0:4])
#-------------------------------------------------------
                                                #negative slicing
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[-3:-1])

#-------------------------------------------------------
                                                #slicing 2d arr
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[1,1:4])

#-------------------------------------------------------
                                                #iterating

# arr = np.array([1,2,3])
# for x in arr:
#     print(x)


#iterating a 3-d arr
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# for x in arr:
#     for y in x:
#         for z in y:
#             print(z)

#iterating using nditer()
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr):
#     print(x)

#iterating through every scalar element of the 2d arr skipping 1 element
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#     print(x)

#numpy joining arr
# arr_1 = np.array([1,2,3])
# arr_2 = np.array([4,5,6])
# arr = np.concatenate((arr_1,arr_2))
# print(arr)

#join two 2-d arrays along rows (axis =1)
# arr_1 = np.array([[1, 2], [3, 4]])
# arr_2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr_1, arr_2), axis=1)
# print(arr)

#stacking
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

#hstack - stacking along rows
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.hstack((arr1, arr2))
# print(arr)

#vstack - stacking along columns
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.vstack((arr1, arr2))
# print(arr)

#splitting
# arr = np.array([1,2,3,4,5,6])
# new_arr = np.split(arr, 3)
# print(new_arr)

#numpy search arr
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)