class Unit:
    # __init__ : constructor
    def __init__(self, name, hp, damage):
        # member variables
        self.name = name
        self.hp = hp
        self.damage = damage

        print(f"{self.name} unit created.")
        print(f"hp {self.hp}, damage {self.damage}")

class StandardUnit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print(f"{self.name} moves to {location} at speed {self.speed}.")

# inheritance
# StandardUnit is parent class
# AttackUnit is child class
class AttackUnit(StandardUnit):
    def __init__(self, name, hp, damage, speed):
        StandardUnit.__init__(self, name, hp, speed)
        # self.name = name
        # self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} attacks towards {location} with damage {self.damage}.")

    def damaged(self, damage):
        print(f"{self.name} received {damage} damage.")
        self.hp -= damage
        print(f"{self.name}'s current hp is {self.hp}.")
        if self.hp <= 0:
            print(f"{self.name} has been destroyed.")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} flies towards {location} at speed {self.flying_speed}.")

# multiple inheritance
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    # method overriding: 메소드 재정의. 메소드명은 같고 안에 내용 변경
    # move method in StandardUnit is overridden
    def move(self, location):
        print("[Air Unit Movement]")
        self.fly(self.name, location)

class BuildingUnit(StandardUnit):
    def __init__(self, name, hp, location):
        # pass keyword: when you don't want to implement anything yet
        pass

supply_depot = BuildingUnit("Supply Depot", 500, "7 o'clock")

def game_start():
    print("[Alert] A new game has started.")
game_start()

def game_over():
    pass
game_over()

vulture = AttackUnit("Vulture", 80, 10, 20)
battlecruiser = FlyableAttackUnit("Battlecruiser", 500, 25, 3)


vulture.move("11 o'clock")
battlecruiser.fly(battlecruiser.name, "9 o'clock")
battlecruiser.move("9 o'clock")

valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3 o'clock")

# creating an instance of AttackUnit
# when call constructor and methods, doesn't need to pass self
firebat = AttackUnit("Firebat", 50, 16, 16)
firebat.attack("5 o'clock")
firebat.damaged(25)
firebat.damaged(25)



# objects
# instances are created from class
# need to pass 3 parameters
marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)
        
wraith1 = Unit("Wraith", 80, 5)
print(f"Wraith's hp is {wraith1.hp}, damage is {wraith1.damage}")

wraith2 = Unit("Wraith2", 80, 5)
# adding member variable 
wraith2.clocking = True  

if wraith2.clocking == True:
    print(f"{wraith2.name} is in cloaking mode.")