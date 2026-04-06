from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, lvl, hp, strength):
        self.name = name
        self.level = lvl
        self.__health = hp
        self.strength = strength
    def greet(self):
        print(f"привет, я {self.name}, мой уровень {self.level}")
    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 10
    @abstractmethod
    def attack(self):
        pass
    def get_health(self):
        return self.__health


class Warrior(Hero):
    def attack(self):
        print("воин атакует мечом")


class Mage(Hero):
    def attack(self):
        print("маг использует магию")


class Assassin(Hero):
    def attack(self):
        print("ассасин атакует из-под тишка")

warrior = Warrior("Арагорн", 1, 100, 15)
mage = Mage("Гендальф", 1, 80, 10)
assassin = Assassin("Агент 47", 1, 90, 12)
print("Воин:")
warrior.greet()
# print(f"здоровье до отдыха: {warrior.get_health()}")
warrior.attack()
warrior.rest()
# print(f"здоровье после отдыха: {warrior.get_health()}")
print("Маг:")
mage.greet()
# print(f"здоровье до отдыха: {mage.get_health()}")
mage.attack()
mage.rest()
# print(f"здоровье после отдыха: {mage.get_health()}")
print("Ассасин:")
assassin.greet()
# print(f"здоровье до отдыха: {assassin.get_health()}")
assassin.attack()
assassin.rest()
# print(f"здоровье после отдыха: {assassin.get_health()}")
