import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def attack(self):
        print(f"{self.name} наносит удар!")
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")
    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает... Здоровье восстановлено до {self.health}!")


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        print("воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print("маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print("ассасин атакует исподтишка!")

warrior = Warrior("Арагорн", 1, 100, 15, 50)
mage = Mage("Гендальф", 1, 80, 10, 100)
assassin = Assassin("Агент 47", 1, 90, 12, 40)
# warrior.greet()
# warrior.rest()
# warrior.attack()
# mage.greet()
# mage.rest()
# mage.attack()
# assassin.greet()
# assassin.rest()
# assassin.attack()

while True:
    user_choice = input("Выберите героя (Warrior / Mage / Assassin) или 'Выход' если устали играть: ").capitalize()
    if user_choice == "Выход":
        print("спасибо за игру!")
        break
    if user_choice == "Warrior" or "Воин":
        player = warrior
    elif user_choice == "Mage" or "Маг":
        player = mage
    elif user_choice == "Assassin" or "Убийца":
        player = assassin
    else:
        player = None
    if player:
        enemy_choice = random.randint(1, 3)
        if enemy_choice == 1:
            enemy = warrior
            enemy_type = "Warrior"
        elif enemy_choice == 2:
            enemy = mage
            enemy_type = "Mage"
        else:
            enemy = assassin
            enemy_type = "Assassin"

        print(f"\nВы: {user_choice} vs Машина: {enemy_type}")

        if user_choice == enemy_type:
            print("нничья!")
        elif (user_choice == "Warrior" and enemy_type == "Assassin") or (user_choice == "Assassin" and enemy_type == "Mage") or (user_choice == "Mage" and enemy_type == "Warrior"):
            player.attack()
            print(f"результат: {user_choice} победил!")
        else:
            enemy.attack()
            print(f"результат: {enemy_type} победил!")
    else:
        print("введите имеющегося героя")