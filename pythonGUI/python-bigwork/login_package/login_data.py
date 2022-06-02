import pymysql
from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def validate_login(inputcode: str, inputpassword: str) -> int:
    """
    This function is used to validate the user's login information.
    """
    # print(inputcode)
    # print(inputpassword)
    conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root', password='Qqhh11191911',
                           database='obj_bigwork', charset='utf8')
    try:
        cur = conn.cursor()
        sql = "SELECT Password FROM Students WHERE StudentCode=%s"
        cur.execute(sql, inputcode)
        data = cur.fetchone()
        # print(data)
        if not data:
            return 0
        rsaobject = RSA_decrypt()
        password_decrypt = rsaobject.decrypt_data(inputpassword)
        password_right = rsaobject.decrypt_data(data[0])
        # print(password_decrypt, password_right)
        if password_decrypt == password_right:
            # print("对了！")
            return 2
        else:
            return 1
    finally:
        conn.close()


class RSA_decrypt(object):
    def __init__(self):
        conn = pymysql.connect(host='sh-cdb-3chov2j0.sql.tencentcdb.com', port=58932, user='root',
                               password='Qqhh11191911',
                               database='obj_bigwork', charset='utf8')
        cur = conn.cursor()
        sql = "SELECT KeyContent FROM RSA WHERE KeyType='PrivateKey'"
        cur.execute(sql)
        self.data = cur.fetchone()
        conn.close()

    def get_key(self):
        key = RSA.importKey(self.data[0])
        return key

    def decrypt_data(self, encrypt_msg):
        private_key = self.get_key()
        cipher = PKCS1_cipher.new(private_key)
        back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
        return back_text.decode('utf-8')
