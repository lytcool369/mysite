from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models


def fetchall():
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = '''
        select b.title, b.content, b.hit, b.reg_date, b.g_no, b.o_no, b.depth, u.name
        from board as b, user as u
        where b.user_no = u.no
    '''
    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


def conn():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.137',
        port=3307,
        db='mysite',
        charset='utf8'
    )