import random
lotto = []

while len(lotto) < 6:
    num = random.randint(1,45)
    if num not in lotto: # 중복 안되게
        lotto.append(num)

print(lotto)














my_lotto = [13,23,33,43,44,45]

while True:
    lotto = []

    while len(lotto) < 6:
        num = random.randint(1,45)
        if num not in lotto: # 중복 안되게
            lotto.append(num)

    if len(set(lotto).intersection(my_lotto)) >= 3:
        print(f"{len(set(lotto).intersection(my_lotto))}개 : 당첨")
        break
    else:
        print(f"{len(set(lotto).intersection(my_lotto))}개 : 낙첨")