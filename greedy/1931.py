from sys import stdin as sin

n = int(sin.readline())

meetings = []
for _ in range(n): 
    meetings.append(list(map(int, sin.readline().split())))

# 가장 짧은, 가장 앞쪽에 있는, 끝나는 시간이 가장 앞에 있는
meetings.sort(key = lambda x:x[0])
meetings.sort(key = lambda x:x[1])

print(meetings)

end = 0
cnt = 0
for meeting in meetings: 
    if meeting[0] >= end: 
        end = meeting[1]
        cnt += 1
print(cnt)