import math

from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models


def paging(page):
    paging = []
    pcontrol = {}
    db = conn()
    cursor = db.cursor(DictCursor)

    sql = 'select count(no) as count from board'
    cursor.execute(sql)
    result = cursor.fetchone()

    cursor.close()
    db.close()

    count = result['count']
    max_page = math.ceil(count / 5)

    # 출력될 페이지 수
    if max_page <= 5:
        for p in range(1, max_page + 1):
            paging.append(p)
    elif page <= 3 and max_page > 5:
        paging = [1, 2, 3, 4, 5]
    elif max_page - page >= 2:
        for p in range(page - 2, page + 3):
            paging.append(p)
    else:
        for p in range(max_page - 4, max_page + 1):
            paging.append(p)

    # > 표시의 조건식
    if max_page >= 6 and max_page - page >= 3:
        if max_page - page >= 6:
            pcontrol['next_p'] = page + 5
        else:
            pcontrol['next_p'] = max_page
        pcontrol['next_view'] = 'on'
    else:
        pcontrol['next_view'] = 'off'

    # < 표시의 조건식
    if page >= 4:
        if page - 5 <= 0:
            pcontrol['prev_p'] = 1
        else:
            pcontrol['prev_p'] = page - 5
        pcontrol['prev_view'] = 'on'
    else:
        pcontrol['prev_view'] = 'off'

    results = {'paging': paging, 'pcontrol': pcontrol}

    return results


def fetchall(page):
    db = conn()
    cursor = db.cursor(DictCursor)
    start = (int(page)-1)*5

    sql = '''
        select b.no, b.title, b.content, b.hit, b.reg_date, b.g_no, b.o_no, b.depth, u.name
        from board as b, user as u
        where b.user_no = u.no
        order by g_no desc, o_no asc
        limit %s, 5
    '''
    cursor.execute(sql, (start,))
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
    cursor.execute(sql, (no,))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    return result


def hit(no):
    db = conn()
    cursor = db.cursor()

    sql = 'update board set hit=hit+1 where no=%s'
    cursor.execute(sql, (no,))
    db.commit()

    cursor.close()
    db.close()


def insert(title, content):
    db = conn()
    cursor = db.cursor()

    sql = '''insert into board values(null, %s, %s, 1, 
                                    ifnull((select max(g_no) from board as b), 0) + 1, 
                                    1, 1, now(), 1)
    '''
    cursor.execute(sql, (title, content))
    db.commit()

    cursor.close()
    db.close()


def modify(title, content, no):
    db = conn()
    cursor = db.cursor()

    sql = 'update board set title=%s, content=%s where no=%s'
    cursor.execute(sql, (title, content, no))
    db.commit()

    cursor.close()
    db.close()


def delete(no):
    db = conn()
    cursor = db.cursor()

    sql = 'delete from board where no=%s'
    cursor.execute(sql, (no,))
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