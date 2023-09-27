class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛 생성")
        print(f"체력 : {self.hp}, 공격력 : {self.damage}")
        
marine1 = Unit("마린", 100, 10)
tank1 = Unit("탱크", 200, 30)
wraith1 = Unit("레이스", 80, 5)

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp, damage)
    
    def attack(self, location):
        print(f"{self.name} : {self.location} 방향으로 적군을 공격합니다. [{self.damage}]")

    def damaged(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("파괴")

firebat1 = AttackUnit("파이어뱃", 20, 20)
firebat1.damaged(15)
firebat1.damaged(15)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f"{self.na}")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


