# 125번 : 핸드폰 번호 -> 통신사 출력하기
tel_num = input("휴대전화 번호 입력: ")

# 좋지 않은 방식 -> 계산 시간 몇 배로 발생
if tel_num[:3] == '011':
    agency = 'SKT'
elif tel_num[:3] == '016':
    agency = 'KT'
elif tel_num[:3] == '019':
    agency = 'LGU'
else:
    agency = '알수없음'


num = tel_num[:3]
# 만약 반드시 3글자가 아니라면?

num = tel_num.split("-")[0] 
# 만약 -를 입력하지 않았다면?

if num == '011':
    agency = 'SKT'
elif num == '016':
    agency = 'KT'
elif num == '019':
    agency = 'LGU'
else:
    agency = '알수없음'

print(f"당신은 {agency} 사용자입니다.")

# 함수로 만들어보자
def tel_to_agency(tel_num):

    num = tel_num[:3]

    if num == '011':
        agency = 'SKT'
    elif num == '016':
        agency = 'KT'
    elif num == '019':
        agency = 'LGU'
    else:
        agency = '알수없음'

    print(f"당신은 {agency} 사용자입니다.")

tel_num = input("휴대전화 번호 입력: ")
tel_to_agency(tel_num)

# 126번 : 우편번호 -> 구 출력하기

# 한글 변수 권장 X
우편번호 = 0

postal_code = input("우편번호: ")
postal_code = postal_code[2]

if postal_code in ["0", "1", "2"]:
    gu = "강북구"
elif postal_code in ["4", "5", "6"]:
    gu = "도봉구"
else:
    gu = "노원구"

print(gu)