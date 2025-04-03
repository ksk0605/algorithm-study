"""
while S의 길이가 T와 같아질때까지 
    S에 A추가 하기 
    S에 B추가하고 뒤집기

BFS로 완탐

dict {
    글자수 : 종류
    1 : A 
    2 : AA BA 
    3 : AAA BAA BAA BAB
}

다 끝나면 종류에 T가 있는지 확인
"""

"""
# 메모리 초과
import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

d = {}
d[len(s)] = [s]

for i in range(len(s) + 1, len(t)+1): 
    d[i] = []
    for v in d[i-1]: 
        d[i].append(v + 'A')
        d[i].append((v + 'B')[::-1])

# print(d)
if t in d[len(t)]: 
    print(1)
else : 
    print(0)
"""

import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

d = {}
d[len(t)] = [t]

for i in range(len(t) - 1, len(s) - 1, -1): 
    if len(d[i+1]) == 0: 
        break
    
    d[i] = []
    for v in d[i+1]: 
        if v[-1] == 'A': 
            d[i].append(v[0:-1])
        if v[0] == 'B': 
            d[i].append(v[::-1][0:-1])


if len(s) not in d.keys(): 
    print(0)
elif s in d[len(s)]: 
    print(1)
else : 
    print(0)