import sqlite3

# Создать/подключиться к БД
conn = sqlite3.connect("not_telegram.db")
cursor = conn.cursor()

# Создать таблицу Users
cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)""")

# Заполнить таблицу 10 записями
users = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000),
]
cursor.executemany("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", users)

# Обновить balance для каждой 2ой записи
cursor.execute("UPDATE Users SET balance=balance+500 WHERE id%2=1")

# Удалить каждую 3ью запись
cursor.execute("DELETE FROM Users WHERE id%3=0")

# Выбрать все записи, где возраст не равен 60
cursor.execute("SELECT * FROM Users WHERE age!=60")
results = cursor.fetchall()

# Вывести результаты в консоль
for row in results:
    print(f"Имя: {row[1]} | Почта: {row[2]} | Возраст: {row[3]} | Баланс: {row[4]}")

# Закрыть соединение с БД
cursor.close()
conn.commit()
conn.close()

