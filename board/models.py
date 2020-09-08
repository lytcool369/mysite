from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models


def fetchall():
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = '''
        select b.no, b.title, b.content, b.hit, b.reg_date, b.g_no, b.o_no, b.depth, u.name
        from board as b, user as u
        where b.user_no = u.no
        order by g_no desc, o_no asc
    '''
    cursor.execute(sql)
    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results


def fetchone(no):
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = '''
        select b.no as board_no, b.title, b.content, u.no as user_no
        from board as b, user as u
        where b.user_no = u.no
        and b.no=%s
    '''
    cursor.execute(sql, str(no))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result


def modify(title, content, no):
    db = conn()
    cursor = db.cursor()

    sql = 'update board set title=%s, content=%s where no=%s'
    cursor.execute(sql, (title, content, str(no)))
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