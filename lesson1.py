class Hero:
    def __init__(self, name, hp, lvl, strength):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.lvl}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.hp += 1

kirito = Hero("Кирито", 100, 5, 100)
asuna = Hero("Асуна", 100, 4, 95)
kirito.greet()
print(f"Сила до атаки: {kirito.strength}")
kirito.attack()
print(f"Сила после атаки: {kirito.strength}")
print(f"HP до отдыха: {kirito.hp}")
kirito.rest()
print(f"HP после отдыха: {kirito.hp}")
asuna.greet()
print(f"Сила до атаки: {asuna.strength}")
asuna.attack()
print(f"Сила после атаки: {asuna.strength}")
print(f"HP до отдыха: {asuna.hp}")
asuna.rest()
print(f"HP после отдыха: {asuna.hp}")