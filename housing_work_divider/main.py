import random
from operator import index

from fontTools.ttLib.ttVisitor import visit


# def actual_cal():
#     tasks = ['Cooking','Cooking Helper', 'Dish Wash']
#     return random.choice(tasks)
#
#
# class Divider:
#
#     def __init__(self,number_of_people,one,two,three,four):
#         self.number_of_people = number_of_people
#         self.one = one
#         self.two = two
#         self.three = three
#         self.four = four
#
#     def affiliation(self):

# This is how you create a random Dataset

# import pandas as pd
#
#
# Food_names = ["Pizza", "Sushi", "Tacos", "Biryani", "Ramen", "Paella", "Kimchi",
#     "Croissant", "Shawarma", "Pad Thai", "Goulash", "Moussaka", "Pho",
#     "Pierogi", "Falafel", "Kebabs", "Churros", "Tandoori Chicken",
#     "Dim Sum", "Fajitas", "Baklava"]
#
# Country_names = ['Italy', 'USA', 'Mexico', 'Japan', 'India', 'China', 'France', 'Thailand','Canada','Greece','GreenLand','Indonesia','Vietnam','Ghana','Africa','Bangladesh']
#
# Rating = ['Excellent','Good','Fine','Bad','Terrible','Okay']
#
# def generate_randomness():
#     food = random.choice(Food_names)
#     country = random.choice(Country_names)
#     price = round(random.uniform(4,312),2)
#     rating = random.choice(Rating)
#
#     return [food,price,country,rating]
#
# rows_of_data = 100
#
# data = [generate_randomness() for _ in range(rows_of_data)]
#
# columns = ['Food','Price','Country_of_Origin','Rating']
# df = pd.DataFrame(data, columns = columns)

# print(df.head(5))

# print(df.sort_values(by= ['Price']))

# N = 5
#
# while N > 0:
#     N -= 1
#     print("damn DudE")

# we shall now try to find the longest palindrome

# def longest_palindrome(word):
#     word = word.lower()
#     longest_substring = ''
#     l = len(word)
#     mid = l//2
#     if word == word[::-1]:
#         return word
#     else:
#         if l % 2 == 0:
#             right = mid
#             left = (mid - 2)
#             while left > 0:
#                 sub = word[left:right]
#                 if sub == sub[::-1] and len(sub) > len(longest_substring):
#                     longest_substring = sub
#                 left -= 1
#                 right += 1
#         else:
#             right = mid+1
#             left = mid
#             while left > 0:
#                 sub = word[left:right]
#                 if sub == sub[::-1] and len(sub) > len(longest_substring):
#                     longest_substring = sub
#                 left -= 1
#                 right += 1
#
#         return longest_substring
#
#
# if __name__ == "__main__":
#     print(longest_palindrome('asbuifufiucasds'))

# def longest_palindromic_substr(word):
#     l = len(word)
#     longest_sub = ""
#     left_scanner = l//2
#     right_scanner = l//2 + 1
#     if word == word[::-1]:
#         return word
#
#     while left_scanner > 0:
#         left = left_scanner - 1
#         right = left_scanner + 1
#         scanned = word[left:right+1]
#         while scanned == scanned[::-1] and len(scanned) > len(longest_sub):
#             scanned = word[left:right + 1]
#             longest_sub = scanned
#             left = left_scanner - 1
#             right = left_scanner + 1
#         left_scanner -= 1
#
#     while right_scanner < l-1:
#         right = right_scanner + 1
#         left = right_scanner - 1
#         scanned = word[left:right+1]
#         while scanned == scanned[::-1] and len(scanned) > len(longest_sub):
#             scanned = word[left:right + 1]
#             longest_sub = scanned
#             left = left_scanner - 1
#             right = left_scanner + 1
#         right_scanner += 1
#
#     return longest_sub
#
# if __name__ == "__main__":
#     print(longest_palindromic_substr("rascefecfjfjckret"))

# This code above is wrong, now we will do the Right one

# def longest_palindromic_substr(word):
#     longest = ""
#
#     for i in range(len(word)):
#         for j in range(i, len(word)):
#             substr = word[i:j+1]
#             if substr == substr[::-1] and len(substr) > len(longest):
#                 longest = substr
#
#     return longest
#
# if __name__ == "__main__":
#     print(longest_palindromic_substr("rascefecfjfjckret"))

# for _ in range(int(input())):
#     goodies = ['010', '101']
#     number = input()
#     for i in range(1,len(number)-1):
#         test = number[i-1]+number[i]+number[i+1]
#         if test in goodies:
#             print('Good')
#             break
#     else:
#         print("Bad")



# Extremely Interesting for-else combo

# for i in range(5):
#     if i == 3:
#         print("Found 3!")
#         break
# else:
#     print("Didn't find 3!")  # This won't run because we broke the loop


# iNteresting Way of doing this one .lstrip() function is quite useful

# def string_to_number():
#     for _ in range(int(input())):
#         convertible = input().lstrip('0')  # Remove leading zeroes
#         if convertible == '':
#             print(0)
#         else:
#             print(int(convertible))
#
# string_to_number()


# def string_to_number():
#     for _ in range(int(input("number of repetitions: "))):
#         convertible = input("The String: ")
#         new_li = []
#         counts = 0
#         for char in convertible:
#             if char == '0':
#                 counts += 1
#                 continue
#             else:
#                 break
#
#         new_li = list(convertible[counts:])
#         new_num = "".join(new_li)
#         if len(new_num) == 0:
#             print(0)
#         else:
#             print(new_num)
#
# string_to_number()


# number = '03457359'
# print(number[2:])
# for char in number[2:]:
#     print(char, end = " ")


# class Dog:
#     def speak(self):
#         return 'Woof'
#
# class Cat:
#     def speak(self):
#         return 'Meow'
#
# class Bird:
#     def speak(self):
#         return 'Chrip'
#
# animals = [Dog(),Cat(),Bird()]
#
# for animals in animals:
#     print(animals.speak())



# class Me:
#     def say(self):
#         return 'I '
#
# class My:
#     def say(self):
#         return 'am the'
#
# class Oho:
#     def say(self):
#         return ' Best'
#
# quotes = [Me(),My(),Oho()]
#
# for things in quotes:
#     print(things.say(), end = "")


# class Introduction:
#     def say(self):
#         return 'I am Swapnanil'
#
# class Work:
#     def say(self):
#         return 'Presently I am a Student at the Northeastern University'
#
# class Future:
#     def say(self):
#         return 'I wish to build my own company in the future'
#
# compact = [Introduction(),Work(),Future()]
#
# for items in compact:
#     print(items.say(), end =  "\n")

# an_arbitrary_list = [1, 2, None, 4, None,6,None]
#
# for _ in an_arbitrary_list:
#     if _ is None:
#         continue
#
#     print(_, end= " ")

# list_a = [(5,'banana'),(4,'apple')]
# print(min(list_a))

# def swap(pairs,lower,higher):
#     pairs[lower],pairs[higher] = pairs[higher],pairs[lower]
#
# class Solution:
#
#     def bubbleSort(self,pairs):
#         n = len(pairs)
#         while n >= 0:
#             n -= 1
#             for i in range(n):
#                 if pairs[i] > pairs[i+1]:
#                     swap(pairs,i,i+1)
#
#         return pairs
#
# sol = Solution()
#
# print(sol.bubbleSort([(5, "apple"), (2, "banana"), (9, "cherry"),(3,'carrot'),(4,'ginger'),(6,'haritaki'),(1,'mango')]))

# Building an Insertion Sort Algorithm

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr
#
# print(insertion_sort([5, 3, 4, 1, 2]))

# arr = [3,2,5,4,1,6]
#
# arr[2] = arr[5]
#
# print(arr)


# something seriously Wrong with this one.

# arr = [3,5,2,4,1,6,3,7,8,4]
#
# n = len(arr)
# for i in range(1,n):
#     insert_index = i
#     current_value = arr.pop(i)
#     for j in range(i-1,-1,-1):
#         if arr[j] > current_value:
#             insert_index = j
#         arr.insert(insert_index,current_value)
#
# print(arr)

# Depth-First_Search

# def dfs(graph,nodes, visited ):
#     if nodes not in visited:
#         print(nodes, end = ' ')
#         visited.add(nodes)
#         for items in graph[nodes]:
#             dfs(graph,items,visited)
#
#
#
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E', 'F'],
#     'D': [],
#     'E': ['G'],
#     'F': [],
#     'G': []
# }
#
# visited = set()
# dfs(graph, 'A', visited)


# Breadth-First_Search

# from collections import deque
#
# def bfs(graph,start):
#     visited = set()
#     queue = deque([start])
#
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     queue.append(neighbor)
#
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': [],
#     'E': []
# }
#
#
# bfs(graph,'A')

# dictio = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': [],
#     'E': []}
#
# node = 'A'
# # for stuff in dictio[node]:
# #     print(stuff)
#
# from collections import deque
#
# queue = deque()
#
# queue.append([stuff for stuff in dictio[node]])
# # Extremely Important
#
# print(type(queue[0]))
# print(type(queue))

# from collections import deque
#
#
# def bfs_shortest_path(graph, start, goal):
#     queue = deque()
#     queue.append([start])  # Start with path containing only start
#     visited = set()
#
#     while queue:
#         path = queue.popleft()  # Get the first path from the queue
#         node = path[-1]  # Get the last node from the path
#
#         if node == goal:
#             return path  # Found the goal!
#
#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph[node]:
#                 new_path = list(path)  # Copy the current path
#                 new_path.append(neighbor)  # Add the neighbor
#                 queue.append(new_path)
#
#     return None  # If there's no path


# Design Your Special Graph, in Dictionary Form.
# Then Initiate the function.


# from collections import deque
#
# def bfs_shortest_path(graph, start, goal):
#     queue = deque()
#     visited = set()
#     queue.append([start])
#
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#
#         if node == goal:
#             return path
#
#         if node not in visited:
#             visited.add(node)
#             for mates in graph[node]:
#                 new_path = list(path)
#                 new_path.append(mates)
#                 queue.append(new_path)
#
#     return None

# def add(x, y):
#   return (x**2) + (y**2)
#
# # Equivalent of this function is --
#
# add_lambda = lambda x,y: x**2 + y**2
#
# print(add(3,4))
# print("")
# print(add_lambda(3,4))

# list_a = [2,3,4,5,6]
# squared_numbers = list(map(lambda x:x**2,list_a))
# print(squared_numbers)

new_list = [1,3,2,4,5,7,6,8]
# even_numbers = list(map(lambda y:y%2 == 0,new_list))
# print(even_numbers) # This will return a boolean
# print("")
# odd_numbers = list(filter(lambda x:x%2 != 0,new_list))
# print(odd_numbers)

# def squares(n):
#     print(f'Generating squares from 1 to {n**2}')
#     for i in range(1,n+1):
#         yield i ** 2
#
# for x in squares(5):
#     print(x, end=" ")

# Some Classic Data Cleaning methods:

# import re
#
# def clean_string(strings):
#     fresh = []
#     for value in strings:
#         value = value.strip()
#         value = re.sub("[!#$%?@.:_]","",value)
#         value = value.title()
#         fresh.append(value)
#     return fresh
#
# uncleaned_strings = [
#     "  Hello World!  ",
#     "Python\n",
#     "\tData Science ",
#     "123Machine Learning!@#",
#     "OpenAI\t\tGPT",
#     "  clean   me    please  ",
#     "Email: user@example.com ",
#     " $$$ Make money fast $$$ ",
#     "\n\nNew\nLine\n",
#     "no_special_characters_needed"
# ]
#
# splitted = (items for items in clean_string(uncleaned_strings))
#
# for items in splitted:
#     print(items)

# import re
#
# def clean_single_string(s):
#     s = s.strip()
#     s = re.sub(r"[!#$%?@.:_]", "", s)
#     s = re.sub(r"\s+", " ", s)
#     return s.title()
#
# uncleaned_strings = [
#     "  Hello World!  ",
#     "Python\n",
#     "\tData Science ",
#     "123Machine Learning!@#",
#     "OpenAI\t\tGPT",
#     "  clean   me    please  ",
#     "Email: user@example.com ",
#     " $$$ Make money fast $$$ ",
#     "\n\nNew\nLine\n",
#     "no_special_characters_needed"
# ]
#
# # Clean all using map (functional programming magic 🪄)
# cleaned = map(clean_single_string, uncleaned_strings)
#
# # Still using generator here, just to keep it light
# for item in cleaned:
#     print(item)

# import numpy as np
# import timeit
#
# my_arr = np.arange(1_00_00)  # small typo in your original size too!
# # my_list = list(range(1_000_000))  # (not used here right now)
#
# # Measure time
# execution_time = timeit.timeit(lambda: my_arr * 2, number=1000)
# print(f"Execution time: {execution_time} seconds")

# Time battle between numpy and a normal list

import numpy as np
import timeit

# # Python list
# my_list = list(range(1_00_00))
#
# # NumPy array
# my_arr = np.arange(1_00_00)
#
# # Timing normal Python list * 2
# list_time = timeit.timeit(lambda: [x * 2 for x in my_list], number=1000)
#
# # Timing NumPy array * 2
# numpy_time = timeit.timeit(lambda: my_arr * 2, number=1000)
#
# print(f"Python List Time: {list_time:.4f} seconds")
# print(f"NumPy Array Time: {numpy_time:.4f} seconds")

# a_list = list(range(30000))
# an_array = np.arange(30000)
#
# list_time = timeit.timeit(lambda: [x*3 for x in a_list], number = 1200)
# array_time = timeit.timeit(lambda : an_array*3, number = 1200)
#
# print(f'Array time is: {array_time:.5f} \nand the List time is: {list_time:.5f}')
#
# print(a_list[:15])
# print(an_array[:15])

# Very Interesting

import numpy as np

# arr2d = np.array([[1,2,3],[3,4,5],[5,6,7]])
# # print(arr2d)
#
# # lower_dim_slice = arr2d[:2,1:]
# # print(lower_dim_slice)
# # print(lower_dim_slice.shape)
#
# # another_lower_slice = arr2d[1,:2]
# # print(another_lower_slice)
# # print(another_lower_slice.shape)
#
# # new_arr = arr2d[0:,2]
# # print(new_arr)
# # print(new_arr.shape)
#
# # new_arr = arr2d[1:2,:2]
# # print(new_arr)
# # print(new_arr.shape)
#
# names = np.array(['bob','candy','plushy','loli','loli','bob'])
# # print(names)
# # print(names == 'loli') # Returns an array with booleans
#
# data = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# # print(data[names == 'loli'])
# # this returns the values from the data array, remember for this to work both the array should have the same structure
#
# # mask = (names == 'bob') | (names == 'loli')
# # print(mask) # returns a boolean array
#
#
#
# empty_list = [1, 2, 3, 4, 5, 6]
#
# # Create the new list
# new_list = [[x, -x] for x in empty_list]
#
# # If you want it as a numpy array:
# new_data = np.array(new_list)
#
# print(new_data)
#
# new_data[new_data < 0] = 1 # will replace all the values of the vectors that were less than -1
#
# print(new_data)
#
# data[names == 'loli'] = 2
# print(data)

# Fancy Indexing

# arr = np.zeros((8,4),dtype= np.int64)
#
# for i in range(8):
#     arr[i] = i
#
# print(arr)

# the ~ operator can be useful when you want to invert a Boolean array referenced by a variable.

# an_array = np.arange(40, dtype = np.int32).reshape((10,4))
#
# print(an_array)

#
# an_array = np.arange(40, dtype = np.int32)
#
# new_array = an_array.reshape(5, -1) # This will automatically calculate the remaining column that this will need
# print(new_array) # remember 5 is the number of rows %

# Each item inside an array is just called an element (or scalar).
# A row or column (a collection of elements) can be called a vector.

# arr = np.arange(8).reshape(2,2,2)
# print(arr)
# new_arr = arr * 0
# print(new_arr)
# alternative for creating an array with zeroes as the values inside them
# sp_array = np.zeros((3,3,3),dtype = np.int32)
# print(sp_array)

# x = np.array([1,2,3,4,5,6])
# y = np.array([2,3,4,5,6,7])
#
# condi = np.array([True ,False ,False ,True ,False ,True])
#
# result = np.where(condi,x, y)
# print(result)

# import timeit
#
# any_array = np.arange(1_000_000)
#
# x = timeit.timeit(lambda: any_array.sum(), number= 1)
# print(f'Time Taken for the summation of the elements within the array is: {x:.8f} seconds')
# print((any_array.sum()))
import matplotlib.pyplot as plt

# nsteps = 1000
# # This sets the number of steps in the random walk
# # Here its 1000
#
# rng = np.random.default_rng(seed=12345)
# # This creates a random number generator with a fixed seed(12345)
# # For reproducibility. Using a seed means you'll get the same random values
# # Each time you run the code
#
# draws = rng.integers(0,2,size = nsteps)
# # This generates nsteps(1000) random integers either 0 or 1
# # 0 and 1 represent a coin flip outcome.
# # size = nsteps gives you a 1D array of 1000 random values,
# # Either 0 or 1
# steps = np.where(draws == 0, 1, -1)
# # This converts the 0s and 1s to steps in the random walks
# # if the draw is 0 then step += 1, and if its 1 then step -= 1
#
# walk = steps.cumsum()
# # This computes cumulative sum of steps
# # You can think of this as a person starting at 0 and taking +1 or -1 steps in each move.
# # walk[i] tells you where the person is after step i
# print(walk.min()," ", walk.max())
#
#
# plt.figure(figsize=(10, 4))
# plt.plot(walk[:300], label='Random Walk (First 300 Steps)')
# plt.xlabel('Step')
# plt.ylabel('Position')
# plt.title('1D Random Walk Visualization')
# plt.axhline(15, color='gray', linestyle='--')  # Optional baseline
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
#
# Generate random walk
# nsteps = 1000
# rng = np.random.default_rng(seed=12345)
# draws = rng.integers(0, 2, size=nsteps)
# steps = np.where(draws == 0, 1, -1)
# walk = steps.cumsum()
#
# # Find min and max
# min_pos = walk.min()
# max_pos = walk.max()
# min_idx = walk.argmin()
# max_idx = walk.argmax()
#
# # Plot
# plt.figure(figsize=(12, 5))
# plt.plot(walk, label='Random Walk', color='blue')
# plt.scatter(min_idx, min_pos, color='red', label=f'Min ({min_pos})', zorder=5)
# plt.scatter(max_idx, max_pos, color='green', label=f'Max ({max_pos})', zorder=5)
#
# # Annotate min and max
# plt.text(min_idx, min_pos - 5, f'Min: {min_pos}', color='red', ha='center')
# plt.text(max_idx, max_pos + 5, f'Max: {max_pos}', color='green', ha='center')
#
# # Additional formatting
# plt.xlabel('Step')
# plt.ylabel('Position')
# plt.title('1D Random Walk with Min/Max Points')
# plt.axhline(0, color='gray', linestyle='--')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
from functools import reduce

# a_list = [1,3,2,4,3,5,4,6,5,7]
# result = sum(filter(lambda x: x % 2 == 0, a_list))
# print(result)

# Dynamic Programming Fibonacci with memoization

# def fib(n, memo=None):
#     if memo is None:
#         memo = {}
#     if n<= 1:
#         return n
#     if n not in memo:
#         memo[n] = fib(n-1,memo) + fib(n-2,memo)
#     return memo[n]
#
# print(fib(3))

# def fib_tab(n):
#     dp = [0] * (n+1)
#     dp[1] = 1
#     for i in range(2,n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#
#     return dp[n]
#
# print(fib_tab(10))

# def min_coin(total ,list_of_coins):
#     counts = 0
#     list_of_coins = sorted(list_of_coins, reverse=True)
#     for coin in list_of_coins:
#         if total >= coin:
#             count = total//coin
#             counts += count
#             total -= coin * counts
#         if total == 0:
#             return counts
#         else:
#             return 'Not Possible'
#
# print(min_coin(47, [1, 2, 5]))

# Dynamic Programming min coins

# def min_coin_dp(total, coins):
#     # Create a dp array with total+1 entries, initialized to "infinity" (we'll use total+1 as a stand-in)
#     dp = [total + 1] * (total + 1)
#
#     # Base case: 0 coins needed to make amount 0
#     dp[0] = 0
#
#     # Fill the dp array
#     for amt in range(1, total + 1):
#         for coin in coins:
#             if amt - coin >= 0:
#                 dp[amt] = min(dp[amt], 1 + dp[amt - coin])
#
#     # If dp[total] is still "infinity", return -1 (not possible)
#     return dp[total] if dp[total] != total + 1 else -1

# Two-Pointers Problem

# def two_sum(nums,target):
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     pairs = []
#     uniques = set()
#     while left < right:
#         current_sum = nums[left] + nums[right]
#
#         if current_sum == target:
#             pairs.append([nums[left],nums[right]])
#             right -= 1
#             left += 1
#         elif current_sum > target:
#             right -= 1
#         else:
#             left += 1
#
#     return pairs
#
# if __name__ == "__main__":
#     print(two_sum([1,3,2,4,5,6,2,7,4,8,5,2,5,1,7,4],10))

# Alternative Approach to the two-pointers problem

# def two_sum(nums,target):
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     pairs = set()
#
#     while left < right:
#         sum_of_pairs = nums[left] + nums[right]
#
#         if sum_of_pairs == target:
#             pairs.add((nums[left],nums[right]))
#             left += 1
#             right -= 1
#
#         elif sum_of_pairs > target:
#             right -= 1
#
#         else:
#             left += 1
#
#     return [list(pair) for pair in pairs]
#
# if __name__ == "__main__":
#     print(two_sum([1,3,2,4,5,6,2,7,4,8,5,2,5,1,7,4],10))

# Hash Style Baby

# def two_sum(nums,target):
#     seen = set()
#     pairs = set()
#
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             pairs.add(tuple(sorted((num,complement))))
#         seen.add(num)
#
#     return [list(pair) for pair in pairs]
#
# if __name__ == "__main__":
#     print(two_sum([1, 3, 2, 4, 5, 6, 2, 7, 4, 8, 5, 2, 5, 1, 7, 4], 10))

# classic threesum

# def t3sum(nums, target):
#     triplets = set()
#     nums.sort()
#
#     for i in range(len(nums)):
#         left = i + 1
#         right = len(nums) - 1
#
#         while left < right:
#             summation = nums[i] + nums[left] + nums[right]
#             if summation == target:
#                 triplets.add((nums[i], nums[left], nums[right]))
#                 left += 1
#                 right -= 1
#             elif summation < target:
#                 left += 1
#             else:
#                 right -= 1
#
#     return [list(t) for t in triplets]


# Longest list of Consecutive Integers

# def longest_consecutive(array):
#     array = sorted(set(array))  # Sort and remove duplicates
#     longest = []
#     current = [array[0]]
#
#     for i in range(1, len(array)):
#         if array[i] == array[i - 1] + 1:
#             current.append(array[i])
#         else:
#             if len(current) > len(longest):
#                 longest = current
#             current = [array[i]]
#
#     if len(current) > len(longest):
#         longest = current
#
#     return longest
#
#
# if __name__ == '__main__':
#     sp_list = [21, 1, 4, 5, 17, 6, 8, 12, 11, 13, 7, 20]
#     print(longest_consecutive(sp_list))  # Output: [4, 5, 6, 7, 8]

# def binary_search(array,target):
#     low = 0
#     high = len(array) - 1
#
#     while low<=high:
#         mid = (low+high)//2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return 'Number Not Present'
#
# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 7
# print(binary_search(arr, target))

# Binary Search For First and Last Occurrences

# def bInArY_sEaRcH(array,num,low,high):
#     while low <= high:
#         mid = (low+high)//2
#         if array[mid] == num:
#             return mid
#         elif array[mid] > num:
#             return bInArY_sEaRcH(array,num,low,mid-1)
#         else:
#             return bInArY_sEaRcH(array,num,mid+1,high)
#
# def masker(array,num,low,high):
#     first_occurrence = bInArY_sEaRcH(array,num,low,high)
#     last_occurrence = 0
#     for index,values in enumerate(array[first_occurrence:-1]):
#         if values == num:
#             continue
#         else:
#             last_occurrence = (index-1)
#
#     print(f'The First occurrences: {first_occurrence}, and the second occurrence: {last_occurrence}')
#
# if __name__ == "__main__":
#     arr = [1,2,3,4,5,5,5,6,7,7,7,8,9,10]
#     masker(arr,7,0,len(arr)-1)

# The Code Above is Wrong -- > -- > ^

# def longest_palindrome(word):
#     l = len(word)
#     if l == 0:
#         return ""
#     start, maxlen = 0,1
#
#     # This will run len(word) times
#     for i in range(l):
#         # THIS RUNS TWO TIMES
#         # for both odd and even length
#         # palindromes. j = 0 means odd
#         # and j = 1 means even length
#         for j in range(2):
#             low,high = i, i+j
#             # Expand substring while it is a palindrome
#             # and in bounds
#             while low >= 0 and high < l and word[low] == word[high]:
#                 currlen = high - low + 1
#                 if currlen > maxlen:
#                     start = low
#                     maxlen = currlen
#                 low -= 1
#                 high += 1
#     return word[start:start + maxlen]
#
# if __name__ == "__main__":
#     s = "forgeeksskeegfor"
#     print(longest_palindrome(s))

# word = 'gogol'
# print(word[::-1])

# INsertioN Sort Algorithm O(n) time complexity

# def searchInsert(nums:list,target:int):
#     for index,value in enumerate(nums):
#         if value < target:
#             continue
#         if value >= target:
#              return index
#
#     return len(nums)
#
# print(searchInsert([1,3,5,6],2))
#
# # Insertion Sort Algorithm O(logN)
#
# def mid_finder(list_a):
#     return index(list_a[(len(list)//2)])
#
# def searchins(nums,target):

# Search Insert Algorithm

# def searchInsert(nums: list[int], target: int) -> int:
#     left, right = 0, len(nums) - 1
#     if target > nums[right]:
#         return right+1
#
#     if target == nums[right]:
#         return right
#
#     while left < right and nums[left] < target:
#         if nums[left] == target:
#             return left
#
#         left += 1
#
#
#     return left
#
#
# if __name__ == "__main__":
#     print(searchInsert([1,3,5,6],7))

# word = "  I am Confused  "
# new_word = word.lstrip(' ')
# print(new_word)

# def lengthOfLastWord(s: str) -> int:
#     v = s.strip()  # Removes both leading and trailing spaces
#     l = []
#     right = len(v) - 1
#
#     for x in range(right, -1, -1):  # Include index 0
#         if v[x] == " ":
#             return len(l)
#         else:
#             l.append(v[x])  # Append the character, not the index
#
#     return len(l)
#
# if __name__ == "__main__":
#     print(lengthOfLastWord("  fly me    to the moon   "))  # Output: 4

def addDigits( num: int) -> int:
    num_str = str(num)
   length = len(str(num))
   while length >= 2:
       total = sum(int(items) for items in num_str ))







