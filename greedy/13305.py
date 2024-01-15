# 다음 도시의 기름이 나보다 더 적은 금액일 순간까지는 앞의 기름 가격으로 이동하기 
# 주어진 도시를 반복하면서 
# 해당 도시의 기름 값을 현재 기름값과 비교하여 
# 더 적은 기름 값으로 다음 도시로 이동

n = int(input()) 
dist_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))

cur_cost = city_list[0]
sum_of_cost = cur_cost * dist_list[0]

for i in range(1,n-1):
    city_cost = city_list[i]
    dist = dist_list[i]
    if city_cost >= cur_cost: 
        sum_of_cost += cur_cost * dist
    else: 
        sum_of_cost += city_cost * dist
        cur_cost = city_cost
    
print(sum_of_cost)