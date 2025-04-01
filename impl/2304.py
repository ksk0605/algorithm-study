"""
1. 기둥을 입력받으며 가장 높은 기둥과 그 기둥의 인덱스를 저장힙니다. 이 때, 가장 높은 기둥이 여러개라면 아무 그것들 중 아무 인덱스나 상관 없습니다. 기준점으로 삼을 기둥 하나만 있으면 됩니다.
 
2.  가장 높은 기둥의 인덱스를 기준으로 왼쪽, 오른쪽으로 나누어 진행합니다. 현재 탐색중인 그룹의 가장 높은 기둥 높이인 curr 변수를 사용합니다.

3. 왼쪽 그룹은 왼쪽에서 오름차순으로, 오른쪽 그룹은 오른쪽에서 내림차순으로 탐색합니다. 이 때, curr(탐색 중인 기둥들 중 가장 높은 기둥)를 계속 max값으로 갱신하고, 그 때의 높이를 정답에 더해줍니다. 
"""

import sys 

n = int(sys.stdin.readline())

maxh = 0
maxi = -1
G = [0] * 1001
for _ in range(n): 
    i, h = map(int, sys.stdin.readline().split())
    G[i] = h 
    if h > maxh : 
        maxi = i 
        maxh = h

result = 0 
curmax = 0

for i in range(maxi): 
    curmax = max(curmax, G[i])
    result += curmax

curmax = 0
for i in range(1000, maxi-1, -1): 
    curmax = max(curmax, G[i])
    result += curmax

print(result)