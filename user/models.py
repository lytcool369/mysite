from MySQLdb import connect
from MySQLdb.cursors import DictCursor
# from django.db import models


def insert(name, email, password, gender):
    db = conn()
    cursor = db.cursor()

    sql = 'insert into user values(null, %s, %s, password(%s), %s, now())'
    cursor.execute(sql, (name, email, password, gender))
    db.commit()

    cursor.close()
    db.close()


def fetchone(email, password):
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = '''
              select no, name 
              from user 
              where email=%s and password=password(%s)
        '''
    cursor.execute(sql, (email, password))
    result = cursor.fetchone()

    # 자원 정리
    cursor.close()
    db.close()

    return result


def fetchone_no(no):
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = '''
              select name, email, gender
              from user
              where no=%s
        '''
    cursor.execute(sql, no)
    result = cursor.fetchone()

    # 자원 정리
    cursor.close()
    db.close()

    return result


def update(name, password, gender, no):
    db = conn()
    cursor = db.cursor()

    if password == '':
        sql = 'update user set name=%s, gender=%s where no=%s'
        cursor.execute(sql, (name, gender, no))
    else:
        sql = 'update user set name=%s, password=password(%s), gender=%s where no=%s'
        cursor.execute(sql, (name, password, gender, no))
    db.commit()

    cursor.close()
    db.close()


def conn():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.137',
        port=3307,
        db='mysite',
        charset='utf8'
    )