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


if __name__ == '__main__':
    print(get_uploadpicurl(1,"201140124"))
