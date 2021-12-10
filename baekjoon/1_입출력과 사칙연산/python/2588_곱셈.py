# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (생략)

a = int(input()) # 첫번째 입력받은 문자 : 숫자로 변환
b = input() # 두번째 입력받은 문자 : 문자열 그대로 둠

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))