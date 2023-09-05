# 자료형
print(5), print(-10), print(3.14), print(1000)
print(3*(3+1))
print(max([3,4,5,6]))
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")

print(5,2,4+3, sep='\t', end=' ')
print("나는","할 수 있다.", sep='\n')


# 변수
animal = "강아지" # 문자열 자료형
name = "연탄"
age = 4 # 숫자 자료형
hobby = "산책" 
is_adult = age >= 3 # Boolean 자료형

print("우리집 " + animal + "의 이름은 " + name + "입니다.")
print("우리집 ", animal, "의 이름은 ", name, "입니다.", sep='')
print(f"우리집 {animal}의 이름은 {name}입니다.")

number = 5

number = number ** 2
number //= 2
print(number)

from math import *
number = -16

print(sqrt(max(abs(number),14)))

from random import *
number1 = randint(1,45) # 1이상, 45이하 랜덤 정수
number2 = random() # 0 ~ 1의 임의의 값
number3 = randrange(1,46) # 1 ~ 46의 임의의 값
print(number1, number2, number3)

name = "강민석"
born_date = "19971003"

print(f"성 : {name[0]}")
print(f"이름 : {name[1:]}")
print(f"년 : {born_date[:4]}")
print(f"일 : {born_date[-2:]}")

sentence = "Python is amazing"
print(sentence.count("i")) # 출력 결과 : ?
sentence.replace("amazing", "good")
print(sentence.find('good')) # 출력 결과 : ?
print(len(sentence)) # 출력 결과 : ?
print("스터디\t화이팅")