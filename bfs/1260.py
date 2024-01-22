from collections import deque
import sys

def bfs(start, graph):
    if start not in graph: 
        return [start]
    visited = []
    dq = deque([start])

    while dq: 
        value = dq.popleft()
        if value not in visited: 
            visited.append(value)
            for u in graph[value]: 
                dq.append(u)
    
    return visited

def dfs(start, graph): 
    if start not in graph: 
        return [start]
    visited = []
    dq = deque([start])

    while dq: 
        v = dq.pop()
        if v not in visited: 
            visited.append(v)
            for u in reversed(graph[v]): 
                dq.append(u)
    
    return visited

n,m,start_v = map(int ,sys.stdin.readline().split())

graph = {}
for _ in range(m): 
    v,u = map(int, sys.stdin.readline().split())
    if v not in graph:
        graph[v] = [u]
    else: 
        graph[v].append(u)
    if u not in graph: 
        graph[u] = [v]
    else: 
        graph[u].append(v)

for key in graph.keys():
    graph[key].sort()

for i in dfs(start_v, graph): 
    print(i, end=' ')
print()
for i in bfs(start_v, graph): 
    print(i, end=' ')