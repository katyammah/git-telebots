import sqlite3

con = sqlite3.connect('database2.db', check_same_thread=False)
cur = con.cursor()


def create_table(month):
    cur.execute('CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, workout_ex TEXT, date NOT NULL)'.format(month))
    con.commit()


def db_data_add(month, id: int, workout_ex, date):
    cur.execute('INSERT into {} (id, workout_ex, date) VALUES (?, ?, ?)'.format(month), (id, workout_ex, date))
    con.commit()


def get_num_id(month):
    list_of_w = cur.execute('SELECT MAX(id) FROM {}'.format(month))
    if list_of_w.fetchall() == [(None,)]:
        num_id = 1
    else:
        num_id = list_of_w.fetchone()[0] + 1
    return num_id
