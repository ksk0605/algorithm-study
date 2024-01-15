# import sys 

# # 메모리 초과가 

# n = int(sys.stdin.readline())

# p1 = p2 = 1
# cnt = 0
# sum = 0
# while p1 < n//2+1 :
#     print(p1,p2)
#     sum += p2
#     p2 += 1

#     if sum == n: 
#         cnt += 1

#     if sum+p2 > n: 
#         p1 = p2 = p1+1
#         sum = 0

# print(cnt+1)

# 제공된 코드는 양의 정수 n을 연속된 양의 정수의 합으로 표현하는 방법의 수를 찾기 위한 것으로 보입니다. 그러나 코드에는 논리 오류가 있어 무한 루프에 빠지는 문제가 있을 수 있습니다.

# 문제는 while p1 < n//2+1: 조건에 있습니다. 루프 내에서 p1이 p2 = p1+1로 증가되면서 p1이 여전히 n//2+1 이상이거나 같을 수 있어 무한 루프에 빠질 수 있습니다.

# 이 문제를 해결하기 위해 루프 조건을 while p1 < n//2 + 1 and p2 <= n:로 수정하고 루프 본문을 조정하면 됩니다. 아래는 수정된 코드입니다.


import sys 

n = int(sys.stdin.readline())

p1 = p2 = 1
cnt = 0
sum_val = 0

while p1 < n//2 + 1 and p2 <= n:
    sum_val += p2
    p2 += 1

    while sum_val > n:
        sum_val -= p1
        p1 += 1

    if sum_val == n: 
        cnt += 1

print(cnt + 1)
