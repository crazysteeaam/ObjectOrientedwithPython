import pymysql
from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def check_roominlist(input_domname, input_domroom) -> bool:
    """
    检查寝室号是否存在
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    try:
        cur = conn.cursor()
        sql = "SELECT RoomName FROM Dormitory,Room WHERE Dormitory.DormID=Room.DormID and DormName = %s and RoomName=%s"
        cur.execute(sql, (input_domname, input_domroom))
        data = cur.fetchone()
        if data is None:
            return False
        else:
            return True
    finally:
        conn.close()


def get_domlist() -> list:
    """
    获取宿舍楼栋列表，显示在注册页面
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    try:
        cur = conn.cursor()
        sql = "SELECT count(DormName) FROM Dormitory ORDER BY DormID"
        cur.execute(sql)
        num = cur.fetchone()[0]
        sql = "SELECT DormName FROM Dormitory ORDER BY DormID"
        cur.execute(sql)
        domlist = []
        for i in range(num):
            data = cur.fetchone()
            domlist.append(data[0])
        return domlist
    finally:
        conn.close()


def start_regist(input_name, input_studentcode, input_password, input_domname,
                 input_domroom):
    """
    开始注册，调用存储过程将信息写入数据库
    """
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    try:
        cur = conn.cursor()
        sql = "CALL proc_createaccount(%s,%s,%s,%s,%s);"
        cur.execute(sql, (input_studentcode, input_name, input_password, input_domname, input_domroom))
        conn.commit()
        return True
    finally:
        conn.close()


class RSA_encrypt(object):
    # 前端加密数据
    def get_key(self, key_file):
        with open(key_file) as f:
            data = f.read()
            key = RSA.importKey(data)
        return key

    def encrypt_data(self, msg):
        public_key = self.get_key('./rsa_public_key.pem')
        cipher = PKCS1_cipher.new(public_key)
        encrypt_text = base64.b64encode(cipher.encrypt(bytes(msg.encode("utf8"))))
        return encrypt_text.decode('utf-8')


if __name__ == "__main__":
    get_domlist()
