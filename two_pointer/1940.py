import sys 

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

unique = list(map(int, sys.stdin.readline().split()))

unique.sort()
start, end = 0,(n-1)

cnt = 0

while start < end: 
    if unique[start] + unique[end] > m: 
        end -= 1
    elif unique[start] + unique[end] < m: 
        start += 1
    else: 
        cnt += 1
        start += 1
        end -= 1

print(cnt)