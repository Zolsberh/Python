import sqlite3
import time
import math


class FDataBase:

    def __init__(self, db):
        self.__db = db
        self.__cursor = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cursor.execute(sql)
            res = self.__cursor.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из БД')
        return []

    def add_course(self, name, description, price):
        try:
            tm = math.floor(time.time())
            self.__cursor.execute('INSERT INTO courses VALUES(NULL, ?,?,?,?)', (name, description, price, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления курса в БД: ' + str(e))
            return False
        return True

    def get_course(self, id_course):
        try:
            self.__cursor.execute(f'SELECT title, description, price FROM courses WHERE id = {id_course}')
            res = self.__cursor.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения курса из БД: ' + str(e))

        return False, False, False

    def get_courses_list(self):
        try:
            self.__cursor.execute(f'SELECT * FROM courses ORDER BY date DESC')
            res = self.__cursor.fetchall()
            if res:
                return res

        except sqlite3.Error as e:
            print('Ошибка получения курса из БД: ' + str(e))

        return []

