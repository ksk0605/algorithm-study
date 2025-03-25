"""
아래 숫자는 항상 위보다 크다. 
5

12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49


"""

# 메모리 초과
# import sys
# n = int(sys.stdin.readline())

# l = []
# for i in range(n): 
#     l.extend(list(map(int, sys.stdin.readline().split())))

# l.sort()
# print(l[-n])

"""
우선순위 큐를 사용해서 
"""

import heapq
import sys

hq = []
n = int(sys.stdin.readline())

for _ in range(n): 
    nums = list(map(int, sys.stdin.readline().split()))

    for num in nums: 
        if len(hq) < n: 
            heapq.heappush(hq, num)
        else: 
            if hq[0] < num: 
                heapq.heappop(hq)
                heapq.heappush(hq, num)
    
print(hq[0])