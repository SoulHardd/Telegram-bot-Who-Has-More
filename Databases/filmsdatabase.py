import sqlite3
from Properties import db_paths
global fdb


def init_fdb():
    global fdb
    fdb = sqlite3.connect(db_paths.fdb_path)


def close_fdb():
    global fdb
    fdb.close()


def get_film_rating(rate_position):
    global fdb
    cur = fdb.cursor()
    cur.execute("""
                SELECT rating
                FROM Films
                ORDER BY rating DESC
                """)
    result = cur.fetchall()
    result = ' '.join(f'{row[0]}' for row in result)
    result = [float(x) for x in result.split()]
    return result[rate_position-1]


def get_num_of_films():
    global fdb
    cur = fdb.cursor()
    cur.execute("""SELECT COUNT(*) FROM Films""")
    n = cur.fetchone()[0]
    return n


def get_film_name(rate_position):
    global fdb
    rate = get_film_rating(rate_position)
    cur = fdb.cursor()
    cur.execute("""
                SELECT name 
                FROM Films 
                WHERE rating = ?
                """,
                (rate,))
    result = cur.fetchone()[0]
    return result


def get_film_poster_url(rate_position):
    global fdb
    rate = get_film_rating(rate_position)
    cur = fdb.cursor()
    cur.execute("""
                SELECT poster 
                FROM Films 
                WHERE rating = ?
                """,
                (rate,))
    result = cur.fetchone()[0]
    return result
