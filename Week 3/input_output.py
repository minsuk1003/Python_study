print("Python", "Java", "Javascript", sep=' vs ', end="?")

import sys

print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {
    "수학" : 0,
    "영어" : 50,
    "코딩" : 100
}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


for num in range(1,21):
    print("대기번호 ", str(num).zfill(3))

answer = input("아무 값이나 입력하세여 : ")
print("입력하신 값은 " + answer + "입니다.")


# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))

# 양수일 때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))


# 파일 입출력

score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")

score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
print()
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
print()

import pickle
profile_file = open("profile.pickle", "wb")
profile = {
    '이름' : '박명수',
    '나이' : 30,
    '취미' : ["축구", "야구"]
}
pickle.dump(profile, profile_file)
profile_file.close()


profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("ddd")

with open("study.txt", "r", encoding="utf8") as study_file:
    study_file.read()   