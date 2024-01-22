import sys
from collections import deque


def bfs(start, mp, visited): 
    dq = deque([start])

    while dq: 
        target = dq.popleft()
        if target not in visited:
            visited.append(target)
            for v in mp[target]: 
                dq.append(v)

n,m = map(int, sys.stdin.readline().split())

mp = {}
for _ in range(m): 
    u,v = map(int, sys.stdin.readline().split()) 
    if u not in mp: 
        mp[u] = [v]
    else: 
        mp[u].append(v)
    if v not in mp: 
        mp[v] = [u]
    else: 
        mp[v].append(u)

visited = []

count = 0
for value in range(1,n+1): 
    if value not in visited and value in mp: 
        bfs(value, mp, visited)
        count += 1
    elif value not in visited and value not in mp:
        count +=1 
print(count)
