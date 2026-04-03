import random

class Hero:
    def __init__(self, name, lvl, hp, strength): # Поменял местами для логики: имя, уровень, хп, сила
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strength = strength

    def attack(self):
        print(f"{self.name} наносит удар!")


class Warrior(Hero):
    def __init__(self, name, lvl, hp, strength, stamina):
        super().__init__(name, lvl, hp, strength) # Теперь порядок совпадает с Hero
        self.stamina = stamina
    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, lvl, hp, strength, mp):
        super().__init__(name, lvl, hp, strength)
        self.mp = mp
    def attack(self):
        print("Маг кастует заклинание!")


class Assasin(Hero):
    def __init__(self, name, lvl, hp, strength, stealth):
        super().__init__(name, lvl, hp, strength)
        self.stealth = stealth
    def attack(self):
        print("Ассасин атакует исподтишка!")

user_choice = input("Выберите героя (Классы: Warrior, Mage, Assasin): ").capitalize()
if user_choice == "Warrior":
    player = Warrior("Арагорн", 1, 100, 15, 50)
elif user_choice == "Mage":
    player = Mage("Гендальф", 1, 80, 10, 100)
elif user_choice == "Assasin":
    player = Assasin("Агент 47", 1, 90, 12, 40)
else:
    player = None

if player:
    enemy_choice = random.randint(1, 3)
    if enemy_choice == 1:
        enemy = Warrior("Вражеский-Воин", 1, 100, 15, 50)
        enemy_type = "Warrior"
    elif enemy_choice== 2:
        enemy = Mage("Вражеский-Маг", 1, 80, 10, 100)
        enemy_type = "Mage"
    else:
        enemy = Assasin("Вражеский-Ассасин", 1, 90, 12, 40)
        enemy_type = "Assasin"

    print(f"\nвы: {user_choice} vs соперник: {enemy_type}")

    if user_choice == enemy_type:
        print("Ничья!")
    elif (user_choice == "Warrior" and enemy_type == "Assasin") or \
         (user_choice == "Assasin" and enemy_type == "Mage") or \
         (user_choice == "Mage" and enemy_type == "Warrior"):
        player.attack()
        print(f"Результат: {user_choice} победил!")
    else:
        enemy.attack()
        print(f"Результат: {enemy_type} победил!")
else:
    print("Ошибка: введите имя героя точно как в списке!")