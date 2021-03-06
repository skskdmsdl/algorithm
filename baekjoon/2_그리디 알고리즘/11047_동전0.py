# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

n, k = map(int, input().split())

num = []
for i in range(n):
    num.append(int(input()))

cnt = 0
# for i in reversed(range(n)):
#     cnt += k//num[i]
#     k = k%num[i]

# print(cnt)

i = n-1

while k != 0:
    cnt += k//num[i] # 동전의 개수를 저장
    k %= num[i] # 동전의 가치로 나눈 나머지를 저장
    i -= 1 # 인덱스를 감소

print(cnt)