"""
항상 순서대로 자기보다 큰 숫자가 주어짐 
따라서 greedy로 왼쪽부터 처리하면 됌. 
왜냐? 뒷 숫자는 나보다 항상 클것이고 앞숫자는 나보다 항상 작을 것이니 
내 앞에 몇개가 있는지만 세면 된다. 
"""

import sys

input = sys.stdin.readline()

n = int(input)

# 리스트 초기화 쉬운 반복을 위해 0 번째 추가
inputs = list(map(int, sys.stdin.readline().split()))
leftcounts = [0] * (n+1)
for i in range(n):
    leftcounts[i+1] = inputs[i]

results = [0] * (n+1)
for num in range(1, n+1): 
    count = leftcounts[num]

    zerocnt = 0
    for i in range(1, n+1): 
        if zerocnt == count:
            if results[i] != 0: 
                continue  
            results[i] = num
            break

        if results[i] == 0: 
            zerocnt += 1


print(' '.join(map(str,results[1:])))
