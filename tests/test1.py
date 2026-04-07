from abc import ABC, abstractmethod

class Hero:
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    def __init__(self, hero: Hero, balance: int, password: str, bank_name: str):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name
    def login(self, password: str):
        return self.__password == password
    @property
    def full_info(self):
        return f"Герой: {self.hero.name}, Уровень: {self.hero.lvl} | Баланс: {self._balance} SOM"
    def get_bank_name(self):
        return self.bank_name
    def bonus_for_level(self):
        return self.hero.lvl * 10
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"
    def __add__(self, other):
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        return "Ошибка: Нельзя сложить счета героев разных классов!"
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return (type(self.hero) is type(other.hero) and
                    self.hero.lvl == other.hero.lvl and
                    self.hero.name == other.hero.name)
        return False


class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone: str):
        pass


class KGSms(SmsService):
    def send_otp(self, phone: str):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUSms(SmsService):
    def send_otp(self, phone: str):
        return {"text": "Код: 1234", "phone": phone}


mage1 = MageHero("Merlin", 80, 500, 150)
mage2 = MageHero("Merlin", 80, 500, 200)
warrior = WarriorHero("Conan", 50, 900, 20)
acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")
print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM\n")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3, end="\n\n")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)
sms = KGSms()
print(sms.send_otp("+996706311290"))
# ru_sms = RUSms()
# print(ru_sms.send_otp("+79991234567"))
