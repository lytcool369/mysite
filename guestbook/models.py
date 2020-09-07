# from django.db import models
from MySQLdb import connect
from MySQLdb.cursors import DictCursor


def list():
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = '''
        select no, 
               name, 
               message, 
               date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date
        from guestbook
        order by reg_date desc;
    '''

    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


def insert(name, password, message):
    db = conn()
    cursor = db.cursor()

    sql = 'insert into guestbook values(null, %s, %s, %s, now())'
    cursor.execute(sql, (name, password, message))
    db.commit()

    cursor.close()
    db.close()


def delete(no, password):
    db = conn()
    cursor1 = db.cursor(DictCursor)

    sql1 = '''
        select no, 
               password
        from guestbook
        where no=%s
    '''

    cursor1.execute(sql1, no)
    results = cursor1.fetchall()

    cursor1.close()

    if password == results[0]['password']:
        cursor2 = db.cursor()
        sql2 = 'delete from guestbook where no=%s and password=%s'

        cursor2.execute(sql2, (no, password))
        db.commit()
        cursor2.close()

        db.close()

        return 0
    else:
        db.close()

        return -1


def conn():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.137',
        port=3307,
        db='mysite',
        charset='utf8'
    )