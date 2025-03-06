"""

"""

import sys 

n, d = map(int, sys.stdin.readline().split())

zirms= []
for i in range(n): 
    zirms.append(list(map(int, sys.stdin.readline().split())))

zirms.sort()
# print(zirms)
# def find(cntd): 
#     minds = []
#     for zirm in zirms: 
#         if zirm[1] == cntd: 
#             minds.append(zirm)
    
#     if len(minds) == 0: 
#         return (False, -1)
# # min(minds, key=lambda x:x[2])
#     return (True, minds[0])
def find(cntd): 
    minds = [zirm for zirm in zirms if zirm[1] == cntd]

    if not minds:
        return (False, -1)

    return (True, min(minds, key=lambda x: x[2]))  # ✅ 가장 짧은 지름길을 선택

dists = [0 for _ in range(d+1)]
for cntd in range(1,d+1):
    haszirm, zirm = find(cntd)

    # if haszirm: 
    #     start = zirm[0]
    #     zlen = zirm[2]
    #     dists[cntd] = min(dists[start] + zlen, dists[cntd-1] + 1)
    # else: 
    #     dists[cntd] = dists[cntd-1] + 1

    if haszirm and start < cntd:  # ✅ start가 현재 위치보다 작거나 같을 때만 사용 가능
        dists[cntd] = min(dists[start] + zlen, dists[cntd-1] + 1)
    else:   
        dists[cntd] = dists[cntd-1] + 1

print(dists[-1])