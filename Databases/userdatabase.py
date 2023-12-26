import sqlite3
from Properties import db_paths
global udb


def init_udb():
    global udb
    udb = sqlite3.connect(db_paths.udb_path)


def close_udb():
    global udb
    udb.close()


# Создание базы данных, хранящей айди, имя и максимальный счет пользователя
def udb_start():
    global udb
    cur = udb.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Users(
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name TEXT NOT NULL, 
                cur_score INTEGER,
                max_score INTEGER,
                counter INTEGER,
                film_list TEXT
                )""")
    udb.commit()


# Заполнение базы данных для определенного пользователя
def insert_user(uid, name):
    global udb
    cur = udb.cursor()
    cur.execute("""
                INSERT OR IGNORE INTO Users (
                user_id,
                user_name,
                cur_score,
                max_score,
                counter) 
                VALUES (?, ?, ?, ?, ?)
                """,
                (uid, name, 0, 0, 0))
    udb.commit()


# Обновление максимального счета пользователя
def update_max_score(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                UPDATE Users 
                SET max_score = cur_score 
                WHERE user_id = ? 
                AND cur_score > max_score
                """,
                (uid,))
    udb.commit()


# Обновления списка фильмов для пользователя
def update_film_list(film_list, uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                UPDATE Users 
                SET film_list = ? 
                WHERE user_id = ?
                """,
                (film_list, uid))
    udb.commit()


# Обновление временного счета и счетчика фильма пользователя
def update_current_score_and_counter(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                UPDATE Users 
                SET cur_score = cur_score + ?,
                counter = counter + ? 
                WHERE user_id = ?""",
                (1, 1, uid))
    udb.commit()


# Аннулирование временного счета и счетчика фильмов для пользователя
def nullification_of_temp_data(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                UPDATE Users 
                SET cur_score = ?,
                counter = ? 
                WHERE user_id = ?
                """,
                (0, 0, uid))
    udb.commit()


# Получение текущего счета пользователя
def get_current_score(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                SELECT cur_score 
                FROM Users 
                WHERE user_id = ?
                """,
                (uid,))
    result = cur.fetchone()[0]
    return result


# Получение текущего значения счетчика пользователя
def get_current_counter(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                SELECT counter 
                FROM Users 
                WHERE user_id = ?
                """,
                (uid,))
    result = cur.fetchone()[0]
    return result


# Получения списка фильмов пользователя
def get_film_list(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                SELECT film_list 
                FROM Users 
                WHERE user_id = ?
                """,
                (uid,))
    res = cur.fetchone()[0]
    result = [int(x) for x in res.split(',')]
    return result


def get_in_game_status(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                SELECT in_game_status 
                FROM Users 
                WHERE user_id = ?
                """,
                (uid,))
    result = cur.fetchone()[0]
    return result


def get_user_max_score(uid):
    global udb
    cur = udb.cursor()
    cur.execute("""
                SELECT max_score 
                FROM Users 
                WHERE user_id = ?
                """,
                (uid,))
    result = cur.fetchone()[0]
    return result


def get_top5_users():
    global udb
    cur = udb.cursor()
    cur.execute("""
                SELECT user_name
                FROM Users
                ORDER BY max_score
                DESC LIMIT 5
                """)
    result = cur.fetchall()
    top = '\n'.join(f'{row[0]}' for row in result)
    return top
