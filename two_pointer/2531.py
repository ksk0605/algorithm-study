""" 
다음은? start + 1 % jubsi

10 개 접시 일때 
0 1 2 3 4 5 6 7 8 9 0 순서니까 
이전거 + 1 % 전체 숫자 나머지
"""


"""
몇번 반복? 
모든 조합을 한번씩 확인할 수 있도록
end < jubsi 일때만
"""

import sys
jubsi, gagit, yeon, coupon = map(int, sys.stdin.readline().split())

chobabs = [0] * jubsi
for i in range(jubsi): 
    chobabs[i] = int(sys.stdin.readline())

start = 0
maxgagit = 0
while start < jubsi: 

    ## 리스트 슬라이싱(성공)
    if (start + yeon) <= jubsi:
        cntcho = set(chobabs[start:start+yeon])
    else:
        cntcho = set(chobabs[start:])
        cntcho.update(chobabs[:(start+yeon)%jubsi])
    cntcho.add(coupon)

    ## 반복문 방식 (시간초과)
    # print(cntcho)
    # for i in range(yeon):
    #     cntcho.add(chobabs[(start+i)%jubsi])
    # print(cntcho)
    maxgagit = max(maxgagit, len(cntcho))
    start  = start + 1

print(maxgagit)