# from collections import deque 

# Insane_graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['G'],
#     'F': [],
#     'G': ['H'],
#     'H': ['I'],
#     'I': ['J'],
#     'J': ['K'],
#     'K': ['L'],
#     'L': ['M'],
#     'M': ['N'],
#     'N': ['O'],
#     'O': ['P'],
#     'P': ['Q'],
#     'Q': ['R'],
#     'R': ['S'],
#     'S': ['T'],
#     'T': ['U'],
#     'U': ['V'],
#     'V': ['W'],
#     'W': ['X'],
#     'X': ['Y'],
#     'Y': ['Z'],
#     'Z': []
# }

# normal_graph = {'A':['B','C'],
#                 'B':['D','E'],
#                 'C':['F'],
#                 'D':[],
#                 'E':[],
#                 }


# def dfs_shortest_distance(graph,start,end):
#     queue = deque()
#     traversed = set()
#     queue.append([start])

#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#         if node == end:
#             return path 
#         if node not in traversed:
#             traversed.add(node)
#             for roads in graph[node]:
#                 new_path = list(path)
#                 new_path.append(roads)
#                 queue.append(new_path)
#     return None

# if __name__ == '__main__':
#     print(dfs_shortest_distance(normal_graph,'A','F'))

# Quick Sort Algorithm


# def partition(array,low,high):
#     kingpin = array[high]
#     x = low - 1
#     for y in range(low,high):
#         if array[y] < kingpin:
#             x += 1
#             quickswap(array,x,y)

#     quickswap(array,x+1,high)
#     return x+1
        

# def quickswap(array,a,b):
#     array[a],array[b] = array[b],array[a]


# def quicksort(array, low , high):
#     if low < high:

#         pi = partition(array,low,high)

#         quicksort(array,low,pi-1)
#         quicksort(array,pi+1,high)

#     return array

# if __name__ == "__main__":
#     array = [43,9,82,69,28]
#     print(quicksort(array,0,len(array)-1))

# Two Sum Algorithm

# longer Version

# def two_sum(array,target):
#     unique_combos = set()
#     for i in range(len(array)):
#         j = 0
#         while j < len(array) and j != i:
#             summation = array[i] + array[j]
#             if summation == target:
#                 unique_combos.add(tuple(sorted((array[i],array[j]))))
#             j+= 1
    
#     return [item for item in list(unique_combos)]

# if __name__ == '__main__':
#     array = [10,3,2,4,1,5,2,6,3,4,2,5,2,6,3,6,456,2,352,5,3525,46,345,35,25,7]
#     print(two_sum(array,14))

# def two_sum(array,target):
#     seen = set()
#     unique_combos = set()

#     for num in array:
#         complement = target - num 
#         if complement in seen:
#             unique_combos.add(tuple(sorted((num,complement))))
#         seen.add(num)

#     return list(unique_combos)

# if __name__ == '__main__':
#     array = [2,4,1,3,5,2,6,3,5,8,4,6,2,4,3,1,2]
#     print(two_sum(array,13))

# Three Sum Algorithm

# def threesum(array,target):
#     unique_combinations = set()
#     for i in range(len(array)-2):
#         new_target = target-array[i]
#         seen = set()
#         for j in range(i+1,len(array)):
#             complement = new_target - array[j]
#             if complement in seen:
#                 unique_combinations.add(tuple(sorted((array[i],array[j],complement))))
#             seen.add(array[j])

#     return [x for x in list(unique_combinations)]

# if __name__ == "__main__":
#     array = [2,5,3,1,4,6,8,6,4,9,2,13,25,11,16]
#     print(threesum(array,9))
            

# reversed integers

# class Solution:
#     def reverse(self, x: int) -> int:
#         if x > 0:
#             reversed_string = str(x)[::-1].lstrip('0')
#             number = int(reversed_string)
#             return number

#         if x < 0:
#             string = str(x)
#             reversed_string = (string[1::])[::-1].lstrip('0')
#             number = -1 * int(reversed_string)
#             return number

#         return x   

# sol = Solution()
# print(sol.reverse(-1232490))

# Pascal's Triangle

# Dynamic Programming


# Bredth First Search Shortest Path

from collections import deque

def shortest_path(graph, start, end):
    queue = deque()
    been_there = set()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in been_there:
            been_there.add(node)
            for next in graph[node]:
                new_path = list(path)
                new_path.append(next)
                queue = new_path

    return None


if __name__ == '__main__':
    maps = {'S':['A','B'],
            'A':['P'],
            'B':['M'],
            'P':['C'],
            'M':['J'],
            'C':['J'],
            'J':[]}
    print(shortest_path(maps,'S','J'))
