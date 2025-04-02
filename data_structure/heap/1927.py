import heapq
import sys

n = int(sys.stdin.readline())

hq = []
for i in range(n): 
    num = int(sys.stdin.readline())

    if num == 0: 
        if len(hq) == 0: 
            print(0)
            continue

        print(heapq.heappop(hq))
        continue

    heapq.heappush(hq, num)
