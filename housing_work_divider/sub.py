# Longest Palindrome
import re
from itertools import count

# def longest_palindromic_substr(word):
#     m = len(word)
#     if m == 0:
#         return ''
#     if word == word[::-1]:
#         return word
#
#     start,max_len = 0,1
#     for i in range(m):
#         for j in range(2):
#             low,high = i,i+j
#             while low >= 0 and high < m and word[low] == word[high]:
#                 current_len = high - low + 1
#                 if current_len > max_len:
#                     start = low
#                     max_len = current_len
#                 low -= 1
#                 high += 1
#     return word[start:start+max_len]
#
# if __name__ == '__main__':
#     s = 'ggsokokokokokosgl'
#     print(longest_palindromic_substr(s))


# Depth First Search

# from collections import deque
#
# graph_1 = {
#     "Boston": ["New York"],
#     "New York": ["Boston", "Chicago", "Washington"],
#     "Chicago": ["New York", "Detroit"],
#     "Washington": ["New York", "Philadelphia"],
#     "Detroit": ["Chicago", "Toronto"],
#     "Philadelphia": ["Washington", "Toronto"],
#     "Toronto": ["Detroit", "Philadelphia", "Montreal"],
#     "Montreal": ["Toronto", "Ottawa"],
#     "Ottawa": ["Montreal"]
# }
#
# def dfs(graph,start,end):
#     queue = deque()
#     been_there = set()
#     queue.append([start])
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#         if node == end:
#             return path
#         if node not in been_there:
#             been_there.add(node)
#             for ways in graph[node]:
#                 new_path = list(path)
#                 new_path.append(ways)
#                 queue.append(new_path)
#     return None
#
# print(dfs(graph_1,'Boston','Toronto'))

# class Node:
#
#     def one(self,name):
#         return name
#
#     def two(self,name):
#         return name + ' is not that fast '
#
#     def three(self,name):
#         return name
#
# class Override(Node):
#     def one(self,phoney):
#         return phoney + ' Is not that great'
#
#     def two(self,name):
#         return 'well you see ' + name + ' I dont like it here'
#
#     def three(self,name):
#         return 'god help me out here ' + name + ' I feel alone'
#
# Buggatti = Node()
# Jesko = Override()
#
# print(Buggatti.two('Super Sport'))
#
# print('After overriding ')
#
# print(Jesko.one('Konigsegg'))



# Read the number of test cases
# test_cases = int(input())
#
# for _ in range(test_cases):
#     # Read N (number of pairs needed) and M (number of left shoes Chef already has)
#     n, m = map(int, input().split())
#
#     # Each pair needs 1 left + 1 right shoe → total 2 shoes per pair
#     total_shoes_required = n * 2
#
#     if m <= n:
#         # Case 1: Chef has fewer or equal left shoes than the pairs needed
#         # He needs (n - m) more left shoes and n right shoes → total = 2n - m
#         print(total_shoes_required - m)
#     else:
#         # Case 2: Chef has more left shoes than needed
#         # He only needs n right shoes now
#         print(n)


# for _ in range(int(input())):
#     A = list(map(int,input().split()))
#     team_a = 0
#     team_b = 0
#     for i in range(0,len(A),2):
#         team_a += A[i]
#         team_b += A[i+1]
#
#     if team_a > team_b:
#         print(1)
#     elif team_b > team_a:
#         print(2)
#     else:
#         print(0)

# t = int(input())
# for i in range(t):
#     n = int(input())
#     A = list(map(int, input().split()))
#     # Unique elements of A using Set()
#     print(*sorted(set(A)))
#
#     # Create an empty list to store frequency of elements in A
#     frequency = dict()
#     for items in A:
#         if items not in frequency:
#             frequency[items] = 1
#         else:
#             frequency[items] += 1
#
#     for key, values in frequency.items():
#         print(values, end = ' ')

import timeit


# def run():
#     test_cases = [
#         [5, 3, 2, 4],
#         [9, 1, 7],
#         [8, 6, 2, 0, 3]
#     ]
#
#     for _ in test_cases:
#         least = min(_)
#         _.remove(least)
#         _.insert(0,least)
#         print(*_)
#
#
#
# print("Time taken:", timeit.timeit(run, number=1))

# def three_sum(array, target):
#     n = len(array)
#     unique_triplets = set()
#
#     for i in range(n):
#         seen = set()
#         curr_target = target - array[i]
#         for j in range(i + 1, n):
#             complement = curr_target - array[j]
#             if complement in seen:
#                 triplet = tuple(sorted((array[i], array[j], complement)))
#                 unique_triplets.add(triplet)
#             seen.add(array[j])
#
#     return list(unique_triplets)
#
# if __name__ == '__main__':
#     arr = [2, 4, 1, 3, 6, 4, 7, 23, 8, 5, 3, 13, 17]
#     print(three_sum(arr, 12))


# Hash Map based threesum

# def threesum_indices(array, target):
#     n = len(array)
#     unique_combinations = set()
#
#     for i in range(n):
#         seen = {}
#         for j in range(i + 1, n):
#             complement = target - array[i] - array[j]
#             if complement in seen:
#                 k = seen[complement]
#                 triplet_indices = tuple(sorted((i, j, k)))
#                 unique_combinations.add(triplet_indices)
#             seen[array[j]] = j  # map value to index
#
#     return [tuple(array[i] for i in triplet) for triplet in unique_combinations]
#
# if __name__ == "__main__":
#     array = [2, 5, 3, 1, 4, 6, 8, 6, 4, 9, 2, 13, 25, 11, 16]
#     print(threesum_indices(array, 9))

# Longest substring without repeating characters

# def lon_sub(word):
#     result = ''
#     for k in range(1,len(word)):
#         repeater = []
#         i = k-1
#         while i < len(word) and word[i] not in repeater:
#             repeater.append(word[i])
#             i += 1
#
#         latest_word = ''.join(repeater)
#         repeater.clear()
#         if len(latest_word) > len(result):
#             result = latest_word
#
#
#     return result
#
# if __name__ == '__main__':
#     print(lon_sub("abcabcbb"))

# class Solution:
#     def LengthOfLongestSubstring(self,s: str):
#         ml = 0
#         i = 0
#         for j in range(len(s)):
#             if len(set(s[i:j+1])) == len(s[i:j+1]):
#                 ml = max(ml,len(s[i:j+1]))
#             while len(set(s[i:j+1])) < len(s[i:j+1]):
#                 i+= 1
#         return ml
#
# loli = Solution()
# print(loli.LengthOfLongestSubstring('abasdbeuaseubn'))

# class Solution:
#     def lengthOfLongestSubstring(self,s):
#         seen = set()
#         i = 0
#         ml = 0
#
#         for j in range(len(s)):
#             while s[j] in seen:
#                 seen.remove(s[i])
#                 i += 1
#             seen.add(s[j])
#             ml = max(ml,j-i+ 1)
#
#         return ml


# def slow_version(s):
#     ml = 0
#     i = 0
#     for j in range(len(s)):
#         if len(set(s[i:j+1])) == len(s[i:j+1]):
#             ml = max(ml, len(s[i:j+1]))
#         while len(set(s[i:j+1])) < len(s[i:j+1]):
#             i += 1
#     return ml
#
# def fast_version(s):
#     seen = set()
#     i = 0
#     ml = 0
#     for j in range(len(s)):
#         while s[j] in seen:
#             seen.remove(s[i])
#             i += 1
#         seen.add(s[j])
#         ml = max(ml, j - i + 1)
#     return ml
#
# setup_code = '''
# from __main__ import slow_version, fast_version
# s = "abcabcbb" * 1000  # Increase size to test speed
# '''
#
# # Time the slower one (your version with set rebuilding)
# slow_time = timeit.timeit('slow_version(s)', setup=setup_code, number=100)
#
# # Time the faster one (with sliding window + set)
# fast_time = timeit.timeit('fast_version(s)', setup=setup_code, number=100)
#
# print(f"Slow version time: {slow_time:.5f} seconds")
# print(f"Fast version time: {fast_time:.5f} seconds")

# row = [1] * 2
# new_row = []
# for i in range(2):
#     new_row = [1] * (i+1)
#
# print(row)
# print(new_row)

# for j in range(1,0):
#     print(j)

# Pascals Triangle DP

# def generate(numRows):
#     triangle = []
#
#     for i in range(numRows):
#         row = [1] * (i + 1)  # Start each row with 1s
#
#         for j in range(1, i):
#             # Fill middle values using DP: triangle[i-1][j-1] + triangle[i-1][j]
#             row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#
#         triangle.append(row)
#
#     return triangle
import numpy as np
import pandas as pd
from debugpy.server.cli import switches
from websocket import continuous_frame


# array = [1,2,3,4,5]
# print(array*5)
#
# sp_array = np.array([1,2,3,4,5])
# print(sp_array*5)

# class Account:
#
#     def __init__(self, name, starting_balance, deposit_amount = None, withdrawal_amount = None):
#         self.name = name
#         self.starting_balance = starting_balance
#         self.deposit_amount = deposit_amount
#         self.withdrawal_amount = withdrawal_amount
#
#     def withdrawal(self,amount):
#         if amount <= 0:
#             print('Invalid withdrawal amount. Must be positive.')
#             return
#         if amount > self.starting_balance:
#             print(f'Sorry {self.name}, insufficient balance. Your current balance is {self.starting_balance}','\n')
#         else:
#             self.starting_balance -= amount
#             print(f'{self.name}, you withdrew {amount}. New balance: {self.starting_balance}','\n')
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print('Invalid deposit amount. Must be positive.')
#             return
#         self.starting_balance += amount
#         print(f'{self.name}, you deposited {amount}. New balance: {self.starting_balance}','\n')
#     def cur_bal(self):
#         return self.starting_balance
#
#
# # Banking = Account('Swapnanil',1000000)
#
# def money_here_n_there():
#     print('####  Welcome to HBC banking  ####')
#     print('Let us initialize your account')
#     name = input('Name: ')
#     initial_amount = int(input('Initial Amount: '))
#     balance = initial_amount
#     if initial_amount <= 0:
#         money_here_n_there()
#     else:
#         bank = Account(name, balance)
#         condition = True
#         while condition:
#             print('\n')
#             print('### HBC Banking made easy ###')
#             print('These are the valid options from where you must choose: ')
#             print('1. Deposit money to existing account ---> ')
#             print('2. Withdraw money from existing account ---> ')
#             print('3 Show current balance ---> ')
#             print('4. Stop the service Immediately ---> ','\n')
#
#             try:
#                 response = int(input('What would you like to do? please choose 1 or 2 or 3: '))
#                 if response == 1:
#                     deposited = int(input('Enter the amount you want to deposit: '))
#                     bank.deposit(deposited)
#                 elif response == 2:
#                     withdraw_amount = int(input('Mention the amount you wish to withdraw: '))
#                     bank.withdrawal(withdraw_amount)
#                 elif response == 3:
#                     print(f"Thank you {name} for using our service")
#                     break
#                 else:
#                     print("Invalid option. Please enter 1, 2, 3 or 4.")
#             except ValueError:
#                 print("Invalid input. Please enter a number.")
#
#
# if __name__ == '__main__':
#     money_here_n_there()

# class Mortgage:
#     def __init__(self, name, data):
#         self.name = name
#         self.data = data  # this can be any iterable
#
#     def __getitem__(self, index):
#         if isinstance(index, slice):
#             print(f"Slicing from {index.start} to {index.stop}")
#             return self.data[index]
#         else:
#             return self.data[index]
#
#
# mor = Mortgage('Swapnanil', 'Armageddon')
# print(mor[1:4])   # prints 'rma'
# print(mor[0])     # prints 'A'

# Longest Palindromic Substring

# def longest_palindromic_substr(a_string):
#     n = len(a_string)
#     if n == 0:
#         return ""
#     start,maxlen = 0,1
#
#     for i in range(n):
#         for j in range(2):
#             low,high = i,i+j
#             while low >= 0 and high < n and a_string[low] == a_string[high]:
#                 curlen = high - low + 1
#                 if curlen > maxlen:
#                     start = low
#                     maxlen = curlen
#                 low -= 1
#                 high += 1
#     return a_string[start:start+maxlen]
#
# if __name__ == '__main__':
#     s = 'malayalam'
#     print(longest_palindromic_substr(s))

# class Person:
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def print_name(self):
#         return (self.fname,self.lname)
#
#
# class Childe(Person):
#     pass
#
# y = Childe('Swapnanil', 'Retas')
# print(y.print_name())

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         # import re
#         # cleaned = re.sub(r'[@#!$%]')
#         allowed = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         convertible = ''
#         s = s.replace(" ", '')
#         for index, values in enumerate(s):
#             if values in allowed:
#                 convertible += values
#             else:
#                 break
#
#         if len(convertible) >= 1 and convertible[0] == '-':
#             result = int(convertible[1:]) * (-1)
#             if result < -2 ** 31:
#                 return -2147483648
#             else:
#                 return result
#
#         elif len(convertible) >= 1 and convertible[0] != '-':
#             new_convertible = ''
#             for chars in convertible:
#                 if chars in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#                     new_convertible += chars
#                 else:
#                     break
#
#             new_convertible = re.sub(r"[^\w\s+-]", '', new_convertible)
#             int_version = int(new_convertible)
#             if int_version > 2 ** 31 - 1:
#                 return 2147483647
#             else:
#                 int_version
#
#         else:
#             return 0


# Remove Duplicates from Sorted Array

# def removeDuplicates(nums: list[int]):
#     def removeDuplicates(self, nums: list[int]) -> list[int]:
#         uniques = set(nums)
#         list_form = list(uniques)
#         return [items for items in list_form]
#
# print(removeDuplicates([1,1,2]))

# def searchInsert(nums:list,target: int):
#     median_value = nums[len(nums)//2]
#     if median_value < target:
#         for index, value in enumerate()

# def addDigits(x: int) -> int:
#     s = str(x)
#     if len(s) == 1:
#         return x
#     else:
#         while len(s) >= 2:
#             summation = sum(int(i) for i in list(s))
#             if summation < 10:
#                 return summation
#             else:
#                 return addDigits(summation)
#
#
#     return 0
#
#
# if __name__ == "__main__":
#     print(addDigits(6535))


# Wrong Doesn't work

# def countPrimes(n: int) -> int:
#     primes = [False] * n
#     if n < 2:
#         return 0
#     if n == 2:
#         return 1
#     for _ in range(3,int(n ** 0.5) +1):
#         if n%_ != 0:
#             primes[_] = True
#
#     return sum(primes)
#
# if __name__ == "__main__":
#     print(countPrimes(10))

# Extremely Unusual

# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

str = 'Hello'
value = int(sum(ord(char) for char in str))
print(value)

