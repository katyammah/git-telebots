import sqlite3


def create_table(month, cur, con):
    cur.execute('CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, workout_ex TEXT, date NOT NULL)'.format(month))
    con.commit()


def db_data_add(month, id: int, workout_ex, date):
    cur.execute('INSERT into {} (id, workout_ex, date) VALUES (?, ?, ?)'.format(month), (id, workout_ex, date))
    con.commit()


def get_num_id(month):
    cur.execute('SELECT MAX(id) FROM {}'.format(month))
    num = cur.fetchone()[0]
    if num is None:
        num_id = 1
    else:
        num_id = num + 1
    return num_id
