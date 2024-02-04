# 벨만포드와 다익스트라의 차이는 매회 간선의 확인 횟수라고 할 수 있음
# 시간이 더 느린 대신 음수간선이 있는 그래프에서 사용가능하다는 장점있음 
import sys
city, bus = map(int, sys.stdin.readline().split())

edges = []
# for i in range(1,bus+1): 
#     graph[i] = []

# 테이블 초기화
for _ in range(bus): 
    start, end, weight = map(int, sys.stdin.readline().split())
    edges.append([start,end,weight])

INF = 1111111111
dists = [INF] * (city + 1)
l = [INF] * (city + 1)

def bellman(): 
    # 출발 노드 설정
    start_node = 1
    dists[start_node] = 0 

    # N - 1 번 반복
    for _ in range(2,city+1): 
        # 전체 간선에 대해서
        for edge in edges:
            start = edge[0]
            end = edge[1]
            weight = edge[2]
            if dists[start] != INF and dists[end] > dists[start] + weight:
                dists[end] = dists[start] + weight

bellman()
pre_dists = dists.copy()
bellman()

if pre_dists == dists: 
    for dist in dists[2:]:
        if dist == INF:
            print(-1)
        else:
            print(dist)
else:
    print(-1)
