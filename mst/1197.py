import sys 
v,e = map(int, sys.stdin.readline().split())

union = [i for i in range(v+1)]

edges = []
for i in range(e): 
    v1,v2,w = map(int ,sys.stdin.readline().split())
    edges.append((w,v1,v2))

edges.sort()

def find(x):
    if union[x] != x:
        return find(union[x])
    return x

# 두 원소가 속한 집합을 합치기
def is_same_group(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    if a < b:
        union[b] = a
    else:
        union[a] = b
    return False
     

cnt = 0
dist = 0
for edge in edges: 
    w,v1,v2 = edge
    if is_same_group(v1,v2):
        continue
    dist += w
    cnt += 1
    if cnt == v-1:
        break

print(dist)