n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N-1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])
    
print(sum)

# n = int(input())
# path = list(map(int,input().split()))
# price = list(map(int,input().split()))
 
# answer = 0
# liter = price[0]
# for i in range(len(path)):
#     answer = answer + path[i]*liter
#     if liter > price[i+1]:
#         liter = price[i+1]
# print(answer)
