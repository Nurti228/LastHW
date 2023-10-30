import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error:
        print('Ошибка в функции create_connection')
    return conn


def create_students_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                имя TEXT,
                фамилия TEXT,
                год_рождения INTEGER,
                баллы_за_дз INTEGER,
                хобби TEXT
            )'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print('Ошибка в функции create_students_table')


def insert_students_data(conn, data):
    sql = '''INSERT INTO students (id, имя, фамилия, год_рождения, баллы_за_дз, хобби)
             VALUES (?, ?, ?, ?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()
    except Error:
        print('Ошибка в функции insert_students_data')


def get_students_with_long_surnames(conn):
    sql = "SELECT * FROM students WHERE LENGTH(фамилия) >= 10"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Error:
        print('Ошибка в функции get_students_with_long_surnames')
        return []


def update_students_with_high_scores(conn):
    sql = "UPDATE students SET имя = 'genius' WHERE баллы_за_дз >= 10"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error:
        print('Ошибка в функции update_students_with_high_scores')


def get_genius_students(conn):
    sql = "SELECT * FROM students WHERE имя = 'genius'"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Error:
        print('Ошибка в функции get_genius_students')
        return []


def delete_even_id_students(conn):
    sql = "DELETE FROM students WHERE id % 2 = 0"
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error:
        print('Ошибка в функции delete_even_id_students')


if __name__ == '__main__':
    database = 'students2.db'
    connection = create_connection(database)

    if connection is not None:
        create_students_table(connection)

        students_data = [
            (1, 'Иван', 'Петров', 1995, 15, 'Чтение'),
            (2, 'Мария', 'Сидорова', 1998, 8, 'Плавание'),
            (3, 'Алексей', 'Смирнов', 1997, 12, 'Футбол'),
            (4, 'Елена', 'Козлова', 1996, 5, 'Рисование'),
            (5, 'Дмитрий', 'Ивановичевский', 1994, 7, 'Музыка'),
            (6, 'Анна', 'Соловьева', 1999, 10, 'Танцы'),
            (7, 'Павел', 'Морозов', 2000, 9, 'Плавание'),
            (8, 'Татьяна', 'Васильевна', 1998, 11, 'Лыжи'),
            (9, 'Игорь', 'Козловский', 2001, 13, 'Компьютеры'),
            (10, 'Маргарита', 'Сидоровичев', 2002, 6, 'Чтение')
        ]

        insert_students_data(connection, students_data)

        long_surname_students = get_students_with_long_surnames(connection)
        print("Студенты с длинными фамилиями:")
        for student in long_surname_students:
            print(student)

        update_students_with_high_scores(connection)

        genius_students = get_genius_students(connection)
        print("Студенты с именем 'genius':")
        for student in genius_students:
            print(student)

        delete_even_id_students(connection)
