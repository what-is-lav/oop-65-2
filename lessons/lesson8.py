import sqlite3

connect = sqlite3.connect("grade.db")
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            grade INTEGER NOT NULL,
            age INTEGER NOT NULL,
            subject VARCHAR (30) NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
''')
def create_user(name, age):
    cursor.execute(
        'INSERT INTO users(name, age) VALUES (?,?)',
        (name, age)
)
connect.commit()
def create_grade(grade,subject,user_id):
    cursor.execute(
        'INSERT INTO users(grade, subject, user_id) VALUES (?,?,?)',
        (grade, subject,user_id)
    )
create_user("Vlad",20)
create_user("vasya",19)
create_user("oleg",20)
create_grade(5, "Информатика",1)
create_grade(5,'fizra',2)
create_grade(5,"matesha",3)
