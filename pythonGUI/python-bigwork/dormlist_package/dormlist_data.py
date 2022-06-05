import pymysql


def getfloorforminf(dormid: str, floor: str) -> tuple:
    """
    获取1-7楼具体楼层的具体信息
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_getfloordorminf(%s,%s)"
    try:
        cursor.execute(sql, (dormid, floor))
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(e)
    finally:
        conn.close()


def getotherfloordorminf(dormid: str) -> tuple:
    """
    获取除1-7层其他楼层具体信息
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_getotherfloordorminf(%s)"
    try:
        cursor.execute(sql, dormid)
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == "__main__":
    print(getfloorforminf('6', '6'))
    print(getotherfloordorminf('6'))
