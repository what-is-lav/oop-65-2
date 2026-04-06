#
# class BankAccount:
#     def __init__(self, login, password, balance):
#         self.login = login
#         self.__password = password
#         self._balance = balance
#
#     def get_balance(self,password):
#         if password == self.password:
#             return self._balance
#         else:
#             return "Не верный пароль"
#     def get_password(self, password):
#         if password == self.__password:
#             return self.__password
#         else:
#             return "..."
#
# vlad = BankAccount("vlad","233232" ,12000)
# print(vlad.get_balance(12000))
# print(vlad.get_password("233232"))

#Абстрактный класс
from abc import ABC, abstractclassmethod
class Animal(ABC):
    @abstractclassmethod
    def move(self):
        pass
    @abstractclassmethod
    def voice(self):
        pass

class Dog(Animal):
    def move(self):
        return "Step step"
    def voice(self):
        return "Gav gav"

guff = Dog()
print(guff.move())
print((guff.voice()))

class SmsOtp(ABC):
    @abstractclassmethod
    def send_sms_to_phone(self):
        pass


class SmsKr(SmsOtp):
    def send_sms_to_phone(self):
        data = '''
        <Phone>996702896119</Phone>
        <Text>Ваш код : 1234 </Text>'''
        return "Ok sms sended"


class SmsRu(SmsOtp):
    def send_sms_to_phone(self):
        data = {
            "phone": "+79898980040",
            "text": "Ваш код: 2341"
        }

