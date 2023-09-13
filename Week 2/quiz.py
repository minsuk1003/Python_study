import random
lotto = []

for i in range(6):
    num = random.randint(1,45)
    lotto.append(num)

print(lotto)

my_lotto = [13,23,33,43,44,45]

while True:
    lotto = []

    for i in range(6):
        num = random.randint(1,45)
        lotto.append(num)
        
    if len(set(lotto).intersection(my_lotto)) >= 3:
        print("당첨")
        break
    else:
        print("낙첨")