import random

# 190번

apart = [ [101, 102], [201, 202], [301, 302] ]

for floor in apart:
    for ho in floor:
        print(f"{ho} 호")

print("-----")

# 210번

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range(3) :
        message2()
        print("C")
    message1()

message3()


# Class
# 팀 생성 클래스
class KBOteam:
    def __init__(self, team, stadium):
        self.team = team
        self.stadium = stadium

# 팀 생성
team1 = KBOteam("SSG Landers", "인천 SSG 랜더스필드") 
team2 = KBOteam("LG Twins", "잠실야구장")

# 게임 생성 및 실행 클래스
class KBOgame(KBOteam):
    def __init__(self, team, stadium, away):
        KBOteam.__init__(self, team, stadium)
        self.away = away

    def game(self):
        home_score = random.randint(0,10)
        away_score = random.randint(0,10)
        if home_score > away_score:
            print(f"[패] {self.away} {away_score} vs {home_score} {self.team} [승] ({self.stadium})")
        else:
            print(f"[승] {self.away} {away_score} vs {home_score} {self.team} [패] ({self.stadium})")


# 게임 만들기
game1 = KBOgame(team1.team, team1.stadium, team2.team)

# 게임 5번 실행
for _ in range(5):
    game1.game()