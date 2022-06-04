import pymysql


def get_studentdoomroom(inputcode: str) -> tuple:
    """
    获取学生的楼栋信息和房间信息
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "CALL proc_getstudentroom(%s)"
    try:
        cursor.execute(sql, inputcode)
        result = cursor.fetchone()
        # 返回楼栋ID，楼栋名称，寝室ID，寝室名称
        return result
    except:
        print("Error")
    finally:
        conn.close()


def count_totalpicnum(studentcode: str) -> int:
    """
    获取学生总上传图片数
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT count(*) FROM view_uploaddetail WHERE StudentCode=%s"
    try:
        cursor.execute(sql, studentcode)
        result = cursor.fetchone()
        return result[0]
    except:
        print("Error")
    finally:
        conn.close()


def get_name_isAdmin(inputcode: str) -> tuple:
    """
    获取学生是否是楼长
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT StudentName,IsAdmin FROM Students WHERE StudentCode=%s"
    try:
        cursor.execute(sql, inputcode)
        result = cursor.fetchone()
        return result
    except:
        print("Error")
    finally:
        conn.close()


def count_openingtask(dormid: str) -> int:
    """
    查询楼栋正在进行的任务数目
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT count(TaskID) FROM Task WHERE TaskDormID=%s and TaskStatus=1"
    try:
        cursor.execute(sql, dormid)
        result = cursor.fetchone()
        return result[0]
    except:
        print("Error")
    finally:
        conn.close()


def get_tasklistdetail(dormid: str):
    """
    查询任务详情
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "SELECT TaskID,TaskContent,TaskStatus,PublisherCode,StudentName " \
          "FROM Task,Students " \
          "WHERE Task.PublisherCode=Students.StudentCode " \
          "and TaskDormID=%s and TaskStatus=1"
    try:
        cursor.execute(sql, dormid)
        result = cursor.fetchall()
        return result
    except:
        print("Error")
    finally:
        conn.close()


def count_uploadstatus(taskid: int, studentcode: str) -> int:
    """
    查询提交图片个数
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_countroomtaskstatus(%s,%s)"
    try:
        cursor.execute(sql, (studentcode, taskid))
        result = cursor.fetchone()
        return result[0]
    except:
        print("Error")
    finally:
        conn.close()


def get_uploadpicurl(taskid: int, studentcode: str) -> tuple:
    """
    获取当前任务上传图片链接
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_getroomtaskpic(%s,%s)"
    try:
        cursor.execute(sql, (studentcode, taskid))
        result = cursor.fetchall()
        return result
    except:
        print("Error")
    finally:
        conn.close()


def insert_picurl_to_database(taskid: int, studentcode: str, internetpath: str):
    """
    将成功插入的图片地址存入数据库
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_insertroomtaskpic(%s,%s,%s)"
    try:
        cursor.execute(sql, (studentcode, taskid, internetpath))
        conn.commit()
        return True
    except:
        print("Error")
        conn.rollback()
        return False
    finally:
        conn.close()


def get_uploadedtaskoneinf(studentcode: str) -> tuple:
    """
    获取page2已提交任务概览
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_geteachtaskone(%s)"
    try:
        cursor.execute(sql, studentcode)
        result = cursor.fetchall()
        return result
    except:
        print("Error")
    finally:
        conn.close()


def get_checkcompleterate(studentcode: str) -> float:
    """
    获取完成率数据
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_checkcompleterate(%s)"
    try:
        cursor.execute(sql, studentcode)
        result = cursor.fetchone()
        return result[0]
    except:
        print("Error")
    finally:
        conn.close()


def check_timerate_myrate(studentcode: str) -> list:
    """
    获取时间段和个人完成率统计情况
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_check_timerate_myrate(%s)"
    try:
        cursor.execute(sql, studentcode)
        result = cursor.fetchone()
        newlist = []
        for i in range(len(result)):
            if result[i] is None:
                newlist.append(0)
            else:
                newlist.append(result[i])
        return newlist
    except:
        print("Error")
    finally:
        conn.close()


def get_getfloor_room(doomid: str) -> tuple:
    """
    查询当前楼栋每层楼的已注册寝室数量
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "call proc_getfloor_room(%s)"
    try:
        cursor.execute(sql, doomid)
        result = cursor.fetchone()
        return result
    except:
        print("Error")
    finally:
        conn.close()


def get_totalroom(dormid: int) -> int:
    """
    获取房间总数
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "select distinct count(distinct Students.RoomID) from view_dormandroom,Students where Students.RoomID = " \
          "view_dormandroom.RoomID and view_dormandroom.DormID =%s "
    try:
        cursor.execute(sql, dormid)
        result = cursor.fetchone()
        return result[0]
    except:
        print("Error")
    finally:
        conn.close()


def get_histask_situation(dormid: str) -> tuple:
    """
    获取任务历史概览
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "select TaskContent, ifnull(completenum,0), Task.TaskStatus,Task.TaskID from Task left join (select " \
          "Task.TaskID, " \
          "count(distinct R.RoomID) as completenum, isConfirmed from Task join view_uploaddetail vu on Task.TaskID = " \
          "vu.TaskID join Room R on vu.RoomID = R.RoomID where DormID = %s group by Task.TaskID, isConfirmed) s on " \
          "s.TaskID = Task.TaskID where TaskDormID = %s order by Task.TaskID desc; "
    try:
        cursor.execute(sql, (dormid, dormid))
        result = cursor.fetchall()
        return result
    except Exception as e:
        print("Error:" + str(e))
    finally:
        conn.close()


def check_task_status(taskid: str) -> int:
    """
    检查任务状态
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "select TaskStatus from Task where TaskID = %s"
    try:
        cursor.execute(sql, taskid)
        result = cursor.fetchone()
        return result[0]
    except Exception as e:
        print("Error:" + str(e))
    finally:
        conn.close()


def open_task(taskid: str) -> bool:
    """
    开启任务
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "update Task set TaskStatus = 1 where TaskID = %s"
    try:
        cursor.execute(sql, taskid)
        conn.commit()
        return True
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


def close_task(taskid: str) -> bool:
    """
    关闭任务
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "update Task set TaskStatus = 0 where TaskID = %s"
    try:
        cursor.execute(sql, taskid)
        conn.commit()
        return True
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


def delete_task(taskid: str) -> bool:
    """
    删除任务
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "delete from Task where TaskID = %s"
    try:
        cursor.execute(sql, taskid)
        conn.commit()
        return True
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()


if __name__ == '__main__':
    print(check_task_status("10"))
