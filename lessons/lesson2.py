
class Hero:
    def __init__(self,name,lvl,hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} base action"

kirito = Hero( "afef" , 100, 120)

class MageHero(Hero):
    def __init__(self, name, lvl, hp,mp ):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f' Hi i {self.name} this my action')

asuna = MageHero("asuna",97,80 , 999)

# print(kirito.action())
# print(asuna.action())

class Fly:
    def action(self):
        print("FLY")

class Swim:
    def action(self):
        print("Swim")

class Animal(Swim,Fly):
    pass

duck = Animal()
# duck.action()

class A:
    def action(self):
        print(A)

class B(A):
    def action(self):
        super().action()
        print(B)

class C(B):
    def action(self):
        super().action()
        print(C)

class D(B,C):
    def action(self):
        super().action()
        print(D)
test_obg = D()
test_obg.action()




