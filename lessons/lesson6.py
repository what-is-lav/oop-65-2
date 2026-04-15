def simple_decorator(func):
    def wrapper():
        print("До выполнения")
        func()
        print("После выполнения")
    return wrapper

@simple_decorator
def say_hello():
    print('Hello world')
say_hello()

def greaying_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"hi")
        return func(*args, **kwargs)
    return wrapper

@greaying_decorator
def test(name):
    print(f"how are you {name}")
test('vlad')

def repeat_decorator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat_decorator(10)
def hi():
    print('hi')
hi()

def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print("new action")
    return NewClass

@class_decorator
class OldClass:
    def action(self):
        print("old action")

test_obj = OldClass()
test_obj.action()

def is_admin(func):
    def wrapper(user):
        if user.role == "админ":
            func()
        else:
            print("Вы не админ!!")
    return wrapper

def binary_seacrh(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right // 2)
        if array(mid) == target:
            print("ok")
        elif mid < target:
            left = mid + 1
        else:
            right = mid - 1
print( "не нашли")

my_list = [1,2,3,4,5,6,7,8,9,10]
binary_seacrh(my_list,10)