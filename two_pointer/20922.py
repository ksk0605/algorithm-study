# import sys

# n,k = map(int, sys.stdin.readline().split())

# numlist = list(map(int, sys.stdin.readline().split()))

# left = 0; 
# right = 0;

# lengths = []

# def check(l): 
#     checklist = [0] * 100001
#     for i in l: 
#         checklist[i] += 1

#     # for i in checklist: 
#     #     if i > k: 
#     #         return True
        
#     if max(checklist) > k:
#         return False
#     return True

# while right != n: 
#     # 현재 리스트가 조건에 부합하는가? (k 이하로 같은 원소가 들어있는가?)
#     newlist = numlist[left:right+1]
#     # print(newlist)
#     result = check(newlist)

#     # if left == right:
#     #     right += 1

#     # 같은 원소의 개수가 k 이하라면 right++ 
#     if result: 
#         right += 1
#     # 같은 원소의 개수가 k 초과라면 right - left 를 저장, left++
#     else: 
#         lengths.append(right-left)
#         left += 1
#     if right == n: 
#         lengths.append(right -left)

# print(max(lengths))

import sys

n, k = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
max_length = 0

count_dict = {}  # 현재 슬라이딩 윈도우 내 숫자 개수 저장

while right < n:
    num = numlist[right]
    count_dict[num] = count_dict.get(num, 0) + 1

    # 만약 k를 초과하는 숫자가 있으면 left를 이동
    while count_dict[num] > k:
        count_dict[numlist[left]] -= 1
        left += 1

    # 윈도우 크기 갱신
    max_length = max(max_length, right - left + 1)
    
    # right 이동
    right += 1

print(max_length)
