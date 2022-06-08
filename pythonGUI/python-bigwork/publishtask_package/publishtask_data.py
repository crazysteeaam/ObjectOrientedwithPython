import pymysql


def publish_task(taskdormid: int, content: str, stcode: str) -> bool:
    """
    发布任务
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "insert into Task(TaskContent,TaskDormID,PublisherCode,PublishTime) values(%s,%s,%s,now())"
    try:
        cursor.execute(sql, (content, taskdormid, stcode))
        conn.commit()
        return True
    except Exception as e:
        print("Error:" + str(e))
        return False
    finally:
        conn.close()
