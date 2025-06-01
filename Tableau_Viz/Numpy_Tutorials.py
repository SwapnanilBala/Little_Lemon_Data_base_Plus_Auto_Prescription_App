# import numpy as np

# list_a = [1,1,2,2,3,4,3,4,3,5,6,2,4,2,5,1,2,3,4,5]


# arr = np.array(list_a)

# print("The Output:\n")


# print(arr)
# print(np.__version__)
# print(type(arr))

# arr = np.array(253) # this is a 1-D array
# print(arr)
# print("")
# arr = np.array([1,2,3,4,5,6,7]) # this is also an 1-D array
# print(arr)
# print("")
# arr = np.array([[1,2,3,],[4,5,6,],[7,8,9]]) # this is a 2-D array
# print(arr)
# print(" ")
# arr = np.array([[[1,2,3,4,],[5,6,7,8]],[[4,3,2,1,],[8,7,6,5]]]) # this is a 3D-array
# print(arr)
# print("")

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# # the .ndim at the end checks the dimension of the array
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# new_arr = np.array([1,2,3],ndmin = 2)
# print(new_arr)
# print(f'the number of dimensions are: ', new_arr.ndim)


# print("\nThe End")

import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr[1])

# print(arr[0] + arr[3])

# arr = np.array([[1,2,3,4,6,5,8],[5,6,7,8,8,0,6]])
# print(arr)

# print('3rd element of the 2nd row is: ',arr[1,2])

# print('5th element of the 2nd row is: ',arr[1,4])

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print('the third element of the second array of the first array is: ',arr[0,1,2])

# new_arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])

# print("last element of the 2nd row of the array is: ",new_arr[1,-1])

# arr = np.array([1,2,3,4,5])

# print(arr[0:5:1])
# print(arr[0::3])
# print(arr[:4])
# print(arr[-3:-1])

# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# # print(arr[1,2::1])
# print(arr[0:2,2])

# print(arr[0:2,1:4])

# arr = np.array([1,2,3,4])
# print(arr.dtype)

# arr_1 = np.array(["Honey","Lemon","Spouse"])
# print(arr_1.dtype)

# arr_2 = np.array([1,2,3,4],dtype = 'S')
# print(arr_2)
# print(arr_2.dtype)

# arr_3 = np.array([1,2,3,4,5], dtype= 'i4')
# print("")
# print(arr_3)
# print(arr_3.dtype)

# arr = np.array([1.8,2.3,3.9,4.6])
# new_arr = arr.astype('i')

# print(new_arr)
# print(new_arr.dtype)

# arr = np.array([1,2,0,4,0,3,0])

# new_arr = arr.astype(bool)

# print(new_arr)
# print(new_arr.dtype)

 # numpy datatypes

# i - integer
#
# b -boolean
#
# u - unsigned integer
#
# f - float
#
# c - complex float
#
# m - timedelta
#
# M - datetime
#
# O - object
#
# S - String
#
# U -unicode
#
# V -fixed chunk of memory for other type (void)

# exp_arr = np.array([1,2,3,4,5,6,5,4,3,2,1,2,3,4,5,2,3,4,1])
#
# unique, counts = np.unique(exp_arr,return_counts = True)
#
# dictionary_sp = dict(zip(unique,counts))
#
#
# print(dictionary_sp.items())

# print(f'Keys: {(i for i in X)} and Values: {(j for j in Y)}')

# arr = np.array([1,2,3,4,5,6,7,6,5,4,3,2,1,2,3,4,5,6,7,8])
#
# unique, counts = np.unique(arr, return_counts = True)
#
#  print(unique, "is related to: ", counts)
#
# dictionary = dict(zip(unique, counts))
#
# for key, pair in dictionary.items():
#     print(f'the number: {key} counts: {pair}')

# arr = np.array([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
#
# x= arr.view()
# print(f'this is the non- modified view: ',x)
#
# arr[0] = 42
# print(x)
# print("")
# print(f'normal array: ', arr)

# arr = np.array([1,2,3,4,5])
# # x = arr.view()
# # x[0] = 42
# #
# # print(arr)
# # print(x)
#
# x = arr.copy()
# y = arr.view()
#
# print(x.base) # unaffected by any changes to the original x, stores the data in a completely separate memory
# print(arr)
# arr[2] = 4 # changing the value of the 3rd item in the array to see if it affects the one below
# print(y.base) # this accepted the changed value

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape) # 2 rows and 4 columns
#
# arr_1 = np.array([1,2,3,4,5,6,7], ndmin= 4)
# print(arr_1.shape) # the last 7 will remain constant but the ones ahead of it will change accordingly


# interesting thing here -

# arr = np.array([1,2,3,4,5,6,7,8,9,0,2,1,3,5,1,1,4,5,2,3,6,7,3,3])
# counts = len(arr)
# print(counts)
# new_arr = arr.reshape(3,8)
# omagwd_arr = arr.reshape(8,3)
# print(new_arr)
# print(omagwd_arr)


# arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#
# newarr = arr.reshape(2,3,2)
# print(newarr)
#
# new_arr = np.array([1,2,3,4,5,6,7,8,76,6,4,6,2,6,3,6,46,4])
# print(len(new_arr))
# modified = new_arr.reshape(3,2,3)
# print(modified)

# arr = np.array([1,2,3,4,5,6,7,8,9])
#
# # print(arr.reshape(2,4))
# # print(arr.reshape(2,4).base)
#
# new_arr = arr.reshape(3,3)
# print(new_arr)

# arr2 = np.array([1,2,3,4,5,6,7,8])
#
# newarr = arr2.reshape(2,2,-1)
# print(newarr)
#
# arr3 = np.array([1,2,3,4,5,6,7,8,9,0,9,8,7,6,7])
# print(len(arr3))
# print("")
#
# print(arr3.reshape(1,3,-1))
#
# print("")
#
# print(arr3.reshape(3,1,-1))
#
# print("")
#
# print(arr3.reshape(5,1,-1))


# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print("")
# new_arr = arr.reshape(-1)
# print(new_arr)

# arr = np.array([1,2,3])
# for x in arr:
#     print(x)
#
# arr_2 = np.array([[1,2,3,4],[5,6,7,8]])
# for i in arr_2:
#     print(i)
#
# for x in arr_2:
#     for i in x:
#         print(i)

# Iterate through the following 3-D array:

# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
#
# for x in np.nditer(arr): # this is to flush out each integers out of their respective box
#   print(x)

# Iterate through the array as a string:

# arr_2 = np.array([1,2,3,4,5])
# for x in np.nditer(arr, flags = ['buffered'], op_dtypes=['S']):
#     print(x)

# arr_3 = np.array([[1,2,3,4],[5,6,7,8]])
# for x in np.nditer(arr_3[::1,::2]):  # ::1 because of there are 2 rows
#     print(x)

# arr = np.array([1,2,3])
#
# for idx,x in np.ndenumerate(arr):
#     print(idx, x)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
#
# for index,values in np.ndenumerate(arr):
#     print(index,values)

# arr = np.array([1,2,3,4,5,6,7])

# for x in np.nditer(arr, flags = ['buffered'], op_dtypes=['S']):
#     print(x)  # this wil return the results in the form of a string

# arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])

# for i in np.nditer(arr[::1,::2],flags=['buffered'], op_dtypes=['S']):
#     print(i)

# Numpy Joining Array

# arr_1 = np.array([1,2,3,4,5])

# arr_2 = np.array([6,7,8,9,0])

# arr = np.concatenate((arr_1,arr_2))
# print(arr)

# arr_1 = np.array([[1,2,3],[4,5,6]])
# arr_2 = np.array([[7,8,9],[0,9,8]])

# arr = np.concatenate((arr_1,arr_2), axis = 1)
# print(arr)
# print("\n-- HELLO MOTO --\n")
# arr = np.concatenate((arr_1,arr_2),axis = 0)
# print(arr)

# arr_1 = np.array([1,2,3])
# arr_2 = np.array([4,5,6])

# arr = np.hstack((arr_1,arr_2))
# print(arr)

# print('\n -- Damn Bruv -- \n')

# arr = np.concatenate((arr_1,arr_2))
# print(arr) Stack along the rows

# arr = np.vstack((arr_1,arr_2))
# print(arr) Column wise

# arr = np.dstack((arr_1,arr_2))  
# print(arr) Depth Stack

# arr = np.array([1,2,3,4,5,6])

# new_arr = np.array_split(arr, 3)
# print(new_arr)

# print(new_arr[0])

# arr = np.array([1,2,3,4,5,6])

# new_arr = np.array_split(arr,4)
# print("\n -- Hello Moto -- \n")
# print(new_arr)


# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# newarr = np.array_split(arr, 3)

# print(newarr[0])
# print("\n")
# print(newarr[1])
# print("\n")
# print(newarr[2])

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr = np.array_split(arr, 3)

# print(newarr)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

# newarr = np.array_split(arr, 3, axis=1)

# print(newarr)
# print('\n')
# print(newarr[0])
# print('\n')
# print(newarr[2])
# print('\n')

# new_arr = np.hsplit(arr,3)
# print(new_arr)

# arr = np.array([1,2,3,4,5,6,7,8,9,0])

# x = np.where(arr == 8)
# print(x)

# y = np.where(arr%3 == 0) 
# print(y)

# z = np.where(arr%2 != 0)
# for items in z:
#     print(items)

# arr = np.array([6,7,8,9])

# x = np.searchsorted(arr,7) 
# y = np.searchsorted(arr,7, side = 'right')
# print(y)
# print(x)

# arr = np.array([1, 3, 5, 7])

# x = np.searchsorted(arr, [2, 4, 6])

# print(x)

# arr = np.array([3,5,2,1,6,7,3,5,2,8,9,2])
# print(np.sort(arr))

# arr = np.array(['banana', 'cherry', 'apple','lesanga','orange'])
# print(np.sort(arr))

# arr = np.array([True, False, True])

# print(np.sort(arr)) this would be arranged alphabatically

# arr = np.array([41,42,43,44])
# x = [True,False,True,False]

# new_arr = arr[x]

# print(new_arr) # this will return [41 43]

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

# filtered_array = []

# for element in arr:
#     if element > 6:
#         filtered_array.append(True)
#     else:
#         filtered_array.append(False)

# new_arr = arr[filtered_array]

# print(new_arr)
# print("")
# print(filtered_array)

# prior one was quite important\


# arr = np.array([1,2,3,4,5,6,7,8,9,10])

# filtered_arr = arr > 4

# print(filtered_arr)

# new_array = arr[filtered_arr]

# print(new_array)

# arr = np.array([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,3,5,12,5,35,6,1,6,1,63,363,6,36,13623,2,46])


# key, counts = np.unique(arr, return_counts= True)

# dictionary = dict(zip(key,counts))

# for key,items in dictionary.items():
#     print(f'the value {key} has appeared {items} many times')

import time
import numpy as np
from matplotlib.pyplot import figure
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

# Normal Distribution

# x = random.normal(size=(3,3))
# print(x)

# x = random.normal(loc = 5, scale= 0.1, size = (2,2))
# print(x)

# fig = sns.histplot(random.normal(loc = 10, scale = 2, size = 10000), kde = True)
# plt.show()

# Binomial Distribution
# n is the number of trials, p is the probability of success,
# and size is the shape of the returned array

# x = random.binomial(n =10 , p = 0.4, size = 15)
# print(x)

# fig = sns.histplot(random.binomial (5, p = 0.7, size = 10000), kde =False)
# plt.show()

# plt.figure(figsize=(7,5))
# sns.histplot(random.normal(loc = 10000, scale = 500, size = 15000 ),kde=True)
# plt.title("Normal Distribution")
# plt.ylabel("Number of Occurrences")
#
#
# plt.figure(figsize=(7,5))
# sns.histplot(random.binomial(n = 10, p = 0.3, size = 15000), kde = True)
# plt.title("Binomial Distribution")
# plt.ylabel("Number of Occurrences")
#
# plt.show()

# sns.histplot(random.normal(loc = 50, scale = 5, size = 1000),label ='Normal')
# sns.histplot(random.binomial(n = 100, p= 0.5, size = 1000), label ='Binomial')
#
# plt.show()

# Poisson Distribution, lam - rate or known number of occurrences,
# and size is the shape of the returned array

# x = random.poisson(lam = 2, size = 10)
# print(x)

# the expected number of occurrences per interval is 2,
# size = 10 generates and array of 1- random samples from a [poisson distribution]

# sns.histplot(random.poisson(lam= 2, size = 10000), kde = False )
# plt.show()

# Binomial distribution only has two possible outcomes,
# whereas poisson distribution can have unlimited possible outcomes.

# But for very large n and near-zero p binomial distribution,
# is near identical to poisson distribution such that n * p is nearly equal to lam.

# Uniform distribution

# the uniform distribution has three parameters ,
# low - lower bound default si 0.0
# high - upper bound default si 1.0
# size - the shape of the array

# x = random.uniform(low = 15, high  = 125,size = (2,3))
# print(x)
#
# fig = figure(figsize=(8,5))
# sns.histplot(random.uniform(low = 0, high = 10, size = 2000), kde = False)
# plt.show()

# fig  = figure(figsize=(7,4))
#
# sns.distplot(np.random.uniform(low = 10, high = 110, size = 500), kde = False)
# plt.title("Distplot of some random values between 10 and 50000")
# plt.xlabel("Occurrences")
# plt.show()

# Logistic Distribution, loc - mean, where the peak is . Default 0,
# scale - S.D, size is the size of the returned array

# x = random.logistic(loc = 10, scale=3, size=(3,3))
# print(x)

# sns.histplot(np.random.logistic(loc= 100, scale= 3, size = 1000), kde = True)
# plt.show()

# Multinomial Distribution

# Multinomial distribution is a generalization of binomial distribution,
# it describes outcomes of multi-nomial scenarios unlike binomial scenarios
# must be only one of the two, Blood type of population, dice roll outcome

# it has three parameters:

# n - number of possible outcomes(e.g 6 for dice roll),
# pvals - list of probabilities of outcomes(e.g [1/6,1/6,1/6,1/6,1/6,1/6] for dice roll)
# size is basically the shape of the returned array

# x= random.multinomial(n = 6, pvals= [1/6,1/6,1/6,1/6,1/6,1/6] )
# print(x)

# y = random.multinomial(n = 3, pvals=[1/4,1/4,1/2])
# print(y) # 3 are the number of possible outcomes, pvals is the probability of that related outcome

# Exponential Distribution
# here the scale means the inverse of rate(lam in poisson distribution) defaults to 1.0
# size is as usual

# x = np.random.exponential(scale = 2, size=(3,3))
# print(x)

# fig = figure(figsize= (6,5))
# sns.histplot(np.random.exponential(scale = 5, size = 2000), kde= True)
# plt.title("Exponential Graph ")
# plt.ylabel("Counts Here")
# plt.show()
# scale -  this is the mean(lambda = 1/rate). this average time before an event happens is 5 units.