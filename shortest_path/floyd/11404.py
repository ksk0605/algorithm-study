import sys 

# 도시개수 n 버스개수 m 
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 10000003
# graph 저장 
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(m): 
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start][end] = min(weight,graph[start][end]) # 가장 짧은 간선 하나만 택하기 위해 min 연산사용 
for i in range(1,n+1):
    graph[i][i] = 0


def floyd(): 
    for node in range(1, n+1): 
        for start in range(1,n+1): 
            for end in range(1,n+1): 
                if graph[start][end] > graph[start][node] + graph[node][end]:
                    graph[start][end] = graph[start][node] + graph[node][end]

floyd()

for i in range(1,n+1): 
    for j in range(1,n+1): 
        if graph[i][j] == INF: 
            print(0, end=' ')
        else: 
            print(graph[i][j], end=' ')
    print()