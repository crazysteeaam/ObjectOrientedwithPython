import pymysql


def get_picurl(taskid: str, roomid: str) -> tuple:
    """
    获取图片url列表
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    cursor = conn.cursor()
    sql = "select pictureurl from view_uploaddetail where taskid=%s and roomid=%s"
    try:
        cursor.execute(sql, (taskid, roomid))
        results = cursor.fetchall()
        return results
    except Exception as e:
        print("Error:" + str(e))
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    print(get_picurl("1", "1")[1][0])
