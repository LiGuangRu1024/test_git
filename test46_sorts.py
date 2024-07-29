# @time     ：2024/7/15 14:57
# @author   : 莉光哈哈哈
# @file     : test46_sorts.py
# @software : PyCharm
'''
冒泡排序
'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def test_bubble_sort():
    arr = [35, 22, 45, 199, 34, 24]
    print(bubble_sort(arr))


'''
快速排序
'''


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def test_quick_sort():
    arr = [35, 22, 45, 199, 34, 24]
    print(quick_sort(arr))


'''
二分查找----在已排序的数组中查找目标值，时间复杂度为O(log n)
'''


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


def test_binary_search():
    arr = [35, 22, 45, 199, 34, 24]
    target = 45
    print(binary_search(arr, target))


'''
深度优先搜索DFS----遍历或搜索树或土的数据结构算法
'''


def dfs(graph, start, visited=None):

    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)


# def test_dfs():
#     GRAPH = {
#         'A': ['B', 'C'],
#         'B': ['D', 'E'],
#         'C': ['F'],
#         'D': [],
#         'E': ['F'],
#         'F': ['G'],
#         'G': []
#     }
#     print(dfs(graph=GRAPH, start='A', visited=set('G')))


'''
广度优先搜索BFS----遍历或搜索树或图的数据结构，但是按照层次进行搜索
'''
from collections import deque


def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


'''
KMP字符串匹配算法-----用于在一个大字符串里查找子字符串
'''


def compute_prefix_function(pattern):
    m = len(pattern)
    prefix = [0] * m
    border = 0
    for i in range(1, m):
        while border > 0 and pattern[i] != pattern[border]:
            border = prefix[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        prefix[i] = border
    return prefix


def kmp_match(text, pattern):
    n = len(text)
    m = len(pattern)
    prefix = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and text[i] != pattern[q]:
            q = prefix[q - 1]
        if text[i] == pattern[q]:
            q += 1
        if q == m:
            print("Pattern found at index", i - m + 1)
            q = prefix[q - 1]


'''
欧几里得算法（辗转相除法）
'''


# 计算两个整数的最大公约数
def gcd(a, b):
    while b != 0:
        a, b, = b, a % b
    return a


def test_gcd():
    a = 43
    b = 56
    print(gcd(a, b))


'''
Dijkstra最短路径算法
'''
import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distances = current_distance + weight
            if distances < distances[neighbor]:
                distances[neighbor] = distances
                heapq.heappush(pq, (distances, neighbor))
    return distances


'''
Prim最小生成树算法----找出加权无向图的最小生成树
'''


def prim(graph):
    mst = {}
    visited = set(['A'])  # 假设从节点A开始
    edges = [(cost, start, end) for start, end, cost in graph if start == 'A']
    heapq.heapify(edges)

    while edges:
        cost, start, end = heapq.heappop(edges)
        if end not in visited:
            visited.add(end)
            mst[end] = (start, cost)
            for edge in graph:
                if edge[0] == end or edge[1] == end:
                    heapq.heappush(edges, (edge[2], edge[0], edge[1]))
    return mst
