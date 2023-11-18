import datetime as dt
import sqlite3
from faker import Faker
import random


available_expanses_names_show = ['Такси', 'Развлечения', 'Продукты', 'Собака', 'Все расходы']


def register(user_id, username):
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    try:
        cursor.execute(
        'INSERT INTO Users (id, username) VALUES (?,?)', (user_id, username))
    except sqlite3.IntegrityError as ex:
        return 'Вы уже зарегистрированы'
    connection.commit()
    connection.close()
    return f'Вы добавлены как: {username}'


def approve_user(user_id):
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[0] == user_id:
            connection.commit()
            connection.close()
            return True
    connection.commit()
    connection.close()
    return False


def new_expanse(name, cost, user_id):
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Expanse (name, cost, user_id, created_at) VALUES (?, ?, ?, ?)',
                   (name,
                    cost,
                    user_id,
                    dt.datetime.now().replace(second=0, microsecond=0)))
    connection.commit()
    connection.close()


def show_my_id(user_id):
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id FROM Users WHERE id = ?', (user_id,))
    my_id = cursor.fetchall()
    connection.commit()
    connection.close()
    return my_id[0][0]


def show_expanses(user_id, type_ex, date):
    now = dt.datetime.now().replace(second=0, microsecond=0)
    now_two = now - dt.timedelta(date)
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    if type_ex == 'Все расходы':
        cursor.execute(f'SELECT SUM(cost) FROM Expanse WHERE user_id = ? AND created_at >= "{now_two}" AND created_at <= "{now}"', (user_id,))
    else:
        cursor.execute(f'SELECT SUM(cost) FROM Expanse WHERE user_id = ? AND name = ? AND created_at >= "{now_two}" AND created_at <= "{now}"', (user_id, type_ex))
    all_expanses = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_expanses[0][0]
