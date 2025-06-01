# Longest Palindrome
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


def run():
    test_cases = [
        [5, 3, 2, 4],
        [9, 1, 7],
        [8, 6, 2, 0, 3]
    ]

    for _ in test_cases:
        least = min(_)
        _.remove(least)
        _.insert(0,least)
        print(*_)



print("Time taken:", timeit.timeit(run, number=1))