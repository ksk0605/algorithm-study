# 300 60 10 
# 최소 숫자이니까 가장 큰 것 부터 빼줘 
# 무한 반복 
# 한 횟수당 뺄 수 있는 가장 큰 버튼으로 빼줌 
# 안되면 -1 반환 ( 10 단위가 아니면 )

def calculater(sec): 
    if sec % 10 != 0:
        return -1
    
    a = 0
    b = 0
    c = 0

    while(True):
        if sec >= 300: 
            sec -= 300
            a += 1
        elif sec >= 60: 
            sec -= 60
            b += 1
        else: 
            sec -= 10
            c += 1

        if sec == 0: 
            break
    
    return a,b,c

sec = int(input())
result = calculater(sec)

if result == -1: 
    print(-1)
else: 
    print(result[0], result[1], result[2])