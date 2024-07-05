import sys 
n,m  = map(int, sys.stdin.readline().split())
l  = list(map(int, sys.stdin.readline().split()))
cnt = 0 
time = 1

while True: 
    for i in l:
        if (time % i) == 0:
            cnt += 1
    if cnt == m:
        break
    time += 1

print(time)
