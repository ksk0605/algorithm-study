"""
단축키 목록 set 

문자열 왼쪽부터 검사 
단축키 목록에 없으면 replace(단어, [단어]) (' ' 공백 제외)

스트링은 iterable index 접근 가능 but immutable (replace 사용)
replace 는 복사본 생성 (스트링 특징 기억해)
upper()
lower()

"""

import sys 

n = int(sys.stdin.readline())

shorts = set([])

def find(tokens): 
    print(tokens)

for i in range(n):
    option = sys.stdin.readline()
    tokens = option.split()
    changed = False
    for i in range(len(tokens)): 
        token = tokens[i]
        s = token[0]

        if s not in shorts: 
            shorts.add(s.lower())
            shorts.add(s.upper())
            tokens[i] = token.replace(s, '['+ s+']', 1)
            changed = True
            break
    if changed: 
        print(' '.join(tokens))
    else: 
        for i in range(len(tokens)):
            token = tokens[i]

            for s in token: 
                if s not in shorts: 
                    shorts.add(s.upper())
                    shorts.add(s.lower())
                    tokens[i] = token.replace(s, '[' + s+ ']', 1)
                    changed = True
                    break
            if changed: 
                break
        print(' '.join(tokens))
