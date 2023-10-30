import sqlite3

with sqlite3.connect('students.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            hobby TEXT,
            first_name TEXT,
            last_name TEXT,
            birth_year INTEGER,
            homework_score INTEGER
        )
    ''')

    students_data = [
        ('Football', 'John', 'Smithson', 1998, 12),
        ('Gaming', 'Alice', 'Wonderland', 1999, 5),
        ('Reading', 'Bob', 'Roberts', 1997, 15),
        ('Chess', 'Eva', 'Johnson', 1996, 8),
        ('Painting', 'Michael', 'Michaelson', 1999, 20),
        ('Dancing', 'Sophia', 'Sullivan', 1998, 3),
        ('Coding', 'Olivia', 'Oliverson', 1997, 14),
        ('Swimming', 'William', 'Williamson', 1999, 9),
        ('Singing', 'Emma', 'Emmerson', 1998, 18),
        ('Cooking', 'James', 'Jameson', 1996, 6)
    ]
    cursor.executemany('''
        INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score)
        VALUES (?, ?, ?, ?, ?)
    ''', students_data)

    cursor.execute("SELECT * FROM students WHERE LENGTH(last_name) >= 10")
    long_last_names = cursor.fetchall()
    print("Студенты с фамилией более 10 символов:")
    for student in long_last_names:
        print(student)

    cursor.execute("UPDATE students SET first_name = 'Genius' WHERE homework_score > 10")

    cursor.execute("SELECT * FROM students WHERE first_name = 'Genius'")
    genius_students = cursor.fetchall()
    print("\nСтуденты с именем 'Genius':")
    for student in genius_students:
        print(student)

    cursor.execute("DELETE FROM students WHERE id % 2 = 0")


