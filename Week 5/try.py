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




