# 리스트
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


# 딕셔너리
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