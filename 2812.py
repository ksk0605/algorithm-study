import sys
n,m = map(int, sys.stdin.readline().split())

number = sys.stdin.readline()

cnt = m
remove_num = 0
while cnt > 0:
    remove = str(remove_num)
    for chr in number: 
        if chr == remove_num:
            number = number.replace(chr, '', 1)
            cnt -= 1
            print(cnt)

    remove_num += 1
    
print(number)
    
    