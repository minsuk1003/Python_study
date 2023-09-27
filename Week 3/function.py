def open_account():
    print("새로운 계좌 생성")

def deposit(balance, money): # 입금
    print(f"입금 완료. 잔액은 {balance+money}원")
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print(f"출금 완료. 잔액은 {balance - money}")
        return balance - money
    else:
        print(f"출금 실패. 잔액은 {balance}")
        return balance

balance = 0
balance = deposit(balance, 2000)
balance = withdraw(balance, 2000)

def profile(name, age, main_lang):
    print(f"이름 : {name}, 나이 : {age}, 사용 언어 : {main_lang}")

profile("유재석", 20, "파이썬")

def profile(name, age=27, main_lang="파이썬"):
    print(f"이름 : {name}, 나이 : {age}, 사용 언어 : {main_lang}")

profile("강민석")

profile(age = 30, name="강민석")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}, 나이 : {age}", end=" ")

profile("유재석", 20, "파이썬")

def profile(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}, 사용 언어 : {lang}")

profile("유재석", 25, "파이썬", "JAVA")

gun = 10

def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
checkpoint(2)
print(f"남은 총 : {gun}")

