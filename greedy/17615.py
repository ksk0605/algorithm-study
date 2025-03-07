"""
색은 하나 선택하면 못바꿈 
옆에 몇개가 있던 뛰넘 가능 


중요한 것은 위치가 아니고 
내 옆에 반대 색이 몇개 있는가? 

어쨌든 특정 색이 양쪽으로 몰려있어야 하는건 맞고

아니지 그럼 한번에 넘을 수 있도록하려면 중간에 치우는작업도 해야하잖아 

R R R R B B B B
RBRBRBRB -> 3번 
R BBB R B RRR -> 2번
RBBRRBBRBRRRBB -> 5
RRRRRRRBBBBBBB B5
RRRRBBBBBRRRBB R6

RBBBRBRRR -> 4번 

맨 가에 있는 색을 알아내고 한번 쭉 돌면서 그 색이 몇개있는지 세면?
"""

import sys 
n = int(sys.stdin.readline())
string = sys.stdin.readline()
ll = [] 
for s in string: 
    ll.append(s)
ll.pop()
answers = []

if len(set(ll)) == 1: 
    print(0)
else: 
    lr = False
    lrc = 0
    for s in ll: 
        if s != "R": 
            lr = True
            continue
        if s == "R" and lr: 
            lrc += 1
            
    answers.append(lrc)

    lb = False
    lbc = 0
    for s in ll: 
        if s != "B": 
            lb = True
            continue
        if s == "B" and lb: 
            lbc += 1
            
    answers.append(lbc)
    
    rr = False
    rrc = 0
    for s in reversed(ll): 
        if s != "R": 
            rr = True
            continue
        if s == "R" and rr: 
            rrc += 1
                
    answers.append(rrc)
    
    rb = False
    rbc = 0
    for s in reversed(ll): 
        if s != "B": 
            rb = True
            continue
        if s == "B" and rb: 
            rbc += 1
                
    answers.append(rbc)
    # print(answers)
    print(min(answers))