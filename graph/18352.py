import sys
from collections import deque

def bfs(graph, dists, start): 
    visited = [0] * len(dists)
    queue = deque([start])
    visited[start-1] = 1

    while queue: 
        curr = queue.popleft()
        for v in graph[curr]: # in 보다 인덱스로 직접 접근이 훨씬 빠름
            if visited[v-1] == 0: 
                queue.append(v)
                visited[v-1] = 1
                dists[v-1] = dists[curr - 1] + 1
            



n,m,k,x = map(int, sys.stdin.readline().split())

graph = {} 
for v in range(1,n+1) : 
    graph[v] = []
for _ in range(m): 
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

dists = [0] * n

bfs(graph, dists, x)
# print(dists)
check = False
for i, dist in enumerate(dists): 
    if dist == k: 
        check = True
        print(i+1)
if not check:
    print(-1)