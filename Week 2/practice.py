# 리스트 : 여러 값 저장
ssg = ["김광현", "최정", "김강민"]
print(ssg)

ssg.append("추신수")
print(ssg)

ssg.insert(1, "서진용")
print(ssg)

ssg.pop()


ssg.sort()
print(ssg)

ssg.clear()
print(len(ssg))


# 딕셔너리 - key : value 페어
ssg_num = {
    "김광현" : 29,
    "최정" : 14,
    "김강민" : 0
}

print(ssg_num["김광현"])
print(ssg_num.get("추신수")) # key가 없다면 오류 대신 None을 출력
print(ssg_num.get("최정")) 

print("추신수" in ssg_num) # 없으면 False
print("김강민" in ssg_num) # 있으면 True

ssg_num["추신수"] = 17

print(ssg_num.keys())
print(ssg_num.values())
print(ssg_num.items())


ssg_num.clear()

# 튜플 - 값 수정 불가
ssg_legend = ("박경완", "김광현", "최정")

# 집합 - 중복 불가, 순서 없음
python = {"강민석", "김진수", "심건우"}
sql = {"강민석", "유지수", "강세영", "조윤주"}

print(sql.intersection(python)) # 교집합
print(sql.union(python)) # 합집합
print(sql - python) # 차집합
print(python - sql)

python.add("강세영")
print(python)

sql.remove("조윤주")
print(sql)

# 자료형 변경
menu = {"김밥", "떡볶이", "라면", "잔치국수"}
menu = list(menu)
menu = tuple(menu)

