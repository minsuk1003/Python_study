# 169번 : 1~10의 모든 홀수 합 출력
sum = 0
for i in range(1,11):
    if i % 2 != 0:
        sum += i
print(sum)

# 170번 : 1~10의 모든 숫자 곱 출력
result = 1
for i in range(1,11):
    result *= i
print(result)