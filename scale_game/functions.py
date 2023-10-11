import random

# 세 광물의 무게 랜덤 추출 후 리스트로 저장하기
def mineral_init():
    mineral_weights = []
    for _ in range(3):
        mineral_weights.append(random.randint(1,10))
    mineral_weights.sort()
    return mineral_weights

# 양쪽 저울의 무게 구하기
def weight(scale, mineral):
    weight = 0
    for i in range(3):
        weight += (scale[i] * mineral[i])
    return weight

# 양쪽 저울 비교하기
def compare(left, right):
    if left < right:
        print(f"오른쪽 저울이 {right-left} 더 무겁습니다.")
    elif left > right:
        print(f"왼쪽 저울이 {left-right} 더 무겁습니다.")
    else:
        print("양쪽 저울의 무게가 동일합니다.")


# 정답 맞추기
def challenge(mineral):
    challenge_answer = list(map(int, input("첫 번째 광물부터 광물의 무게를 차례대로 입력하세요.").split())) 
    if challenge_answer == mineral:
        return True
    else:
        print("틀렸습니다.")
        return False 