import sys 

"""
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
"""


n = int(sys.stdin.readline())

for _ in range(n):
    s = int(sys.stdin.readline())
    cases = list(map(int, sys.stdin.readline().split()))
    max = 0
    result = 0
    for i in range(len(cases) - 1, -1, -1): 
        # print(cases[i], max)
        if max < cases[i]: 
            max = cases[i]
        else: 
            result += max - cases[i]
    print(result)