from functions import *

# 게임 진행
def game_start():
    minerals = mineral_init()
    
    for i in range(10):
        left_scale = list(map(int, input("왼쪽 저울에 놓을 광물의 수를 차례대로 입력하세요.").split()))      
        right_scale = list(map(int, input("오른쪽 저울에 놓을 광물의 수를 차례대로 입력하세요.").split()))    

        left_weight = weight(left_scale, minerals)
        right_weight = weight(right_scale, minerals)

        compare(left_weight, right_weight)

        submit = challenge(minerals)
        if submit == True:
            print("저울 게임에 성공하셨습니다.")
            break

        if i == 9:
            print("저울 게임에 실패하셨습니다.")
            break

game_start()