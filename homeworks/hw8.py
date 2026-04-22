import sqlite3
connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating INTEGER CHECK(rating >= 1 AND rating <= 10),
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (movie_id) REFERENCES movies (id)
    )
''')
connect.commit()
cursor.execute('DELETE FROM reviews')
cursor.execute('DELETE FROM users')
cursor.execute('DELETE FROM movies')
cursor.execute('DELETE FROM sqlite_sequence WHERE name IN ("users", "movies", "reviews")')
connect.commit()

users_data = [
    ("Vlad",), ("Tynystan",), ("Artem",), ("Artur",), ("Dimoon",)
]
cursor.executemany('INSERT INTO users (name) VALUES (?)', users_data)

movies_data = [
    ("Бойцовский клуб", "Триллер"),
    ("Оппенгеймер", "Драма"),
    ("Волк с Уолл-стрит", "драма"),
    ("Интерстеллар", "Фантастика"),
    ("Один дома", "Комедия")
]
cursor.executemany('INSERT INTO movies (title, genre) VALUES (?, ?)', movies_data)

reviews_data = [
    (1, 1, 9), (2, 1, 10), (3, 1, 8),
    (4, 2, 10), (5, 2, 9),
    (1, 3, 7), (2, 3, 8), (3, 3, 9),
    (4, 4, 10), (5, 4, 10)
]
cursor.executemany('INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)', reviews_data)
connect.commit()

print(" База данных создана и заполнена!\n")

print(" Имя пользователя + Фильм + Оценка ")
cursor.execute('''
    SELECT users.name, movies.title, reviews.rating 
    FROM reviews
    JOIN users ON reviews.user_id = users.id
    JOIN movies ON reviews.movie_id = movies.id
''')
for row in cursor.fetchall():
    print(f"Пользователь: {row[0]} | Фильм: {row[1]} | Оценка: {row[2]}")

print("\n ВСЕ фильмы, даже без отзывов")
cursor.execute('''
    SELECT movies.title, reviews.rating 
    FROM movies
    LEFT JOIN reviews ON movies.id = reviews.movie_id
''')
for row in cursor.fetchall():
    rating = row[1] if row[1] is not None else "Нет оценок"
    print(f"Фильм: {row[0]} | Оценка: {rating}")

print("\n Агрегации")
cursor.execute('''
    SELECT 
        ROUND(AVG(rating), 2) AS avg_rating, 
        MAX(rating) AS max_rating, 
        MIN(rating) AS min_rating 
    FROM reviews
''')
stats = cursor.fetchone()
print(f"cредняя оценка: {stats[0]}")
print(f"максимальная оценка: {stats[1]}")
print(f"минимальная оценка: {stats[2]}")

print("\n Бонуска: Средняя оценка каждого фильма")
cursor.execute('''
    SELECT movies.title, ROUND(AVG(reviews.rating), 1)
    FROM movies
    JOIN reviews ON movies.id = reviews.movie_id
    GROUP BY movies.id
''')
for row in cursor.fetchall():
    print(f"Фильм: {row[0]} | Средний балл: {row[1]}")
connect.close()