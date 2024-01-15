# 0과 1이 출력되는 횟수를 저장해야함 
# fib 3 의 1 개수 = fib 2 의 1 개수 + fib 1의 1개수
# base case 
# 0 | 1 0 1 
# 1 | 0 1 1

n = int(input())

zero_counts = [0] * 41
one_counts = [0] * 41
zero_counts[0] = 1
zero_counts[1] = 0
zero_counts[2] = 1
one_counts[0] = 0
one_counts[1] = 1
one_counts[2] = 1

test_case = []

for i in range(n): 
    test_case.append(int(input()))

for i in range(3,41): 
    zero_counts[i] = zero_counts[i-1] + zero_counts[i-2]
    one_counts[i] = one_counts[i-1] + one_counts[i-2]

for case in test_case: 
    print(zero_counts[case], one_counts[case])