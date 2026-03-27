from tkinter.font import names


class Hero:
    def __init__(self, name,hp,lvl) :
        self.name_hero = name
        self.hp_hero = hp
        self.lvl_hero = lvl
    def action(self):
        return f"{self.name_hero}hero base action!"

kirito = Hero("Кирито", 100, 5)

print(kirito)
print(kirito.name_hero)
print(kirito.action())