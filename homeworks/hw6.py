import time
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            func(user)
        else:
            print("вы не являетесь администратором!!")
    return wrapper

@is_admin
def delete_video(user):
    print("видео удалено")
admin = User("Vlad", "admin")
user = User("Bek", "user")
delete_video(user)
delete_video(admin)

#Задание 2
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time:.1f} секунд")
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")
download_video()