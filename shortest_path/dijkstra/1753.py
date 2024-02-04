import sys
import heapq as hq

INF = 111111111 # 가중치들의 앞이 INF를 넘어갈 수 있다 설정에 주의

v,e = map(int, sys.stdin.readline().split())
dists = [INF for _ in range(v+1)]
start = int(sys.stdin.readline())
q = []

graph = {} 
for i in range(1,v+1): 
    graph[i] = []
for i in range(e):
    s,e,w = map(int, sys.stdin.readline().split())
    graph[s].append((w,e))

def dijkstra(start): 
    dists[start] = 0 # 자기 자신의 거리는 0
    
    # 우선순위 큐에 (0,시작점을 추가)
    q.append((0,start))

    # 큐가 빌때까지 2,3번 과정을 반복
    while q: 
        item = hq.heappop(q) # 거리 가장 작은 원소 택
        w = item[0]
        v = item[1]

        # 해당거리가 최단 거리 테이블에 있는 값과 다를 경우 다음 과정을 수행하지 않고 넘어감
        if w != dists[v]: 
            continue

        # 원소가 가르키는 정점이 v 라 할때   
        for tp in graph[v]: # v와 이웃한 정점들(tpv)에 대해
            tpw = tp[0]
            tpv = tp[1]
            if dists[tpv] > dists[v] + tpw: # 최단 거리 테이블 값보다 v를 거쳐가는 것이 더 작은 값을 가질 경우
                dists[tpv] = dists[v] + tpw # 최단 거리 테이블의 값을 갱신하고 
                hq.heappush(q, (dists[tpv],tpv)) # 우선순위 큐에 (거리, 이웃한 정점의 번호)를 추가

dijkstra(start)

for i in range(1,v+1): 
    if dists[i] == INF:
        print('INF')
    else:
        print(dists[i])