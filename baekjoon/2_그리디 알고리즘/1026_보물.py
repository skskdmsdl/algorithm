# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 
# 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 S의 최솟값을 출력한다.

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(a_list) * max(b_list)
    a_list.pop(a_list.index(min(a_list)))
    b_list.pop(b_list.index(max(b_list)))

print(s)

# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# a.sort(reverse=True)
# b.sort()
# c = 0
# sum = 0
# for i in a:
#     sum += i * b[c]
#     c += 1
# print(sum)
