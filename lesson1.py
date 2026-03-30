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
print(f"сила до атаки: {kirito.strength}")
kirito.attack()
print(f"сила после атаки: {kirito.strength}")
asuna.greet()
print(f"HP до: {asuna.hp}")
asuna.rest()
print(f"HP после: {asuna.hp}")