import pymysql


def get_roomcompletesitui_fromtask(taskid: str):
    """
    获取任务中的完成情况
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call get_roomcompletesitui_fromtask(%s)"
    try:
        cursor.execute(sql, taskid)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


def get_taskname(taskid: str):
    """
    获取任务名
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "select TaskContent from Task where taskid=%s"
    try:
        cursor.execute(sql, taskid)
        result = cursor.fetchone()
        return result
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


def check_complete(taskid, roomid, stcode) -> bool:
    """
    已读任务
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "update PicURL set isConfirmed=1,CheckStudentCode=%s where TaskID = %s and StudentCode in (select " \
          "StudentCode from Students " \
          "where RoomID = %s) "
    try:
        cursor.execute(sql, (stcode, taskid, roomid))
        conn.commit()
        return True
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


def delete_complete(taskid, roomid) -> bool:
    """
    打回任务
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "delete from PicURL where TaskID = %s and StudentCode in (select StudentCode from Students " \
          "where RoomID = %s) "
    try:
        cursor.execute(sql, (taskid, roomid))
        conn.commit()
        return True
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


if __name__ == "__main__":
    print(get_roomcompletesitui_fromtask('2'))
    print("ok")
