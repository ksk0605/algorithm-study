from collections import deque
def bfs(y, x, visited, grim, JN, rgb): 
    jn = ["R", "G"]
    dir = [(1,0), (0,1), (-1,0), (0,-1)]
    
    dq = deque([(x,y)])
    visited[y][x] = True
    
    while dq:
        cur = dq.popleft() 
        x = cur[0]
        y = cur[1]
        for d in dir: 
            nextx = x+d[0] 
            nexty = y+d[1]
            if nextx == len(grim) or nexty == len(grim) or nextx < 0 or nexty <0:
                continue
            if not JN: 
                if not visited[nexty][nextx] and grim[nexty][nextx] == rgb:
                    dq.append((nextx, nexty))
                    visited[nexty][nextx] = True
            else: 
                if rgb == "R" or rgb == "G" :
                    if not visited[nexty][nextx] and grim[nexty][nextx] in jn:
                        dq.append((nextx, nexty))
                        visited[nexty][nextx] = True
                else : 
                    if not visited[nexty][nextx] and grim[nexty][nextx] == rgb:
                        dq.append((nextx, nexty))
                        visited[nexty][nextx] = True

# 입력 - n*n의 이차원 배열 만들기
from sys import stdin as s 
n = int(s.readline())
grim = []
for i in range(n):
    line = s.readline()
    l = []
    for item in line[:-1]: 
        l.append(item)
    grim.append(l)

# 솔루션 - 원소를 하나씩 방문하면서 bfs 돌림 bfs가 돌아간 횟수를 카운트해서 반환
def solution(grim, n): 
    cnt = 0
    jncnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    jnvisited = [[False for _ in range(n)] for _ in range(n)]
    for y in range(len(grim)): 
        for x in range(len(grim[y])): 
            if not jnvisited[y][x]: 
                bfs(y, x, jnvisited, grim,True, grim[y][x])
                jncnt+=1
            if not visited[y][x] : 
                bfs(y, x, visited, grim,False, grim[y][x])
                cnt+=1
    return (cnt,jncnt)

# 출력 - 카운트 출력
result = solution(grim=grim, n=n)
print(result[0], result[1])
