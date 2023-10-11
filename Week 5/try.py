num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
try:
    print(num1 / num2)
except Exception as e:
    print(e)


# 예외 처리
try:
    4/0
except ZeroDivisionError as e:
    print(e)
finally:
    print("감사합니다.")


# 예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("민석")


# 297번
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        new_per.append(float(per))
    except:
        new_per.append(0)

print(new_per)



# 300번
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print("float type으로 변환할 수 없습니다.")
    else:
        print("float type으로 변환되었습니다.")
    finally:
        print("감사합니다.")
