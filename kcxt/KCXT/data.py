# -*- coding: utf-8 -*-
import os
import sqlite3
import wx
DBFILE = 'kcxt.db'

def get_create_db(db_filename):
    """打开本地数据库文件db_filename,并返回数据库连接con"""
    """如果本地数据库文件dbfilename,在创建数据库和UserInfo表"""
    if os.path.exists(db_filename):
        con = sqlite3.connect(db_filename)
    else:
        con = sqlite3.connect(db_filename)
        # 在该数据库下创建人员信息表（库存人员和销售人员）
        sql_create_admin_user = '''CREATE TABLE UserInfo(
                            USERID VARCHAR(20) PRIMARY KEY,
                            USERNAME VARCHAR(20) NOT NULL,
                            GENDER VARCHAR(2),
                            BIRTHDAY VARCHAR(11),                          
                            PHONE VARCHAR(20),
                            USERTYPE VARCHAR(2),
                            PASSWORD VARCHAR(20) NOT NULL);'''
        con.execute(sql_create_admin_user)
        sql_insert_admin_user2 = '''INSERT INTO UserInfo 
        VALUES("001","张小小","女","1998/4/6","010-8392082","店长","123456");'''
        con.execute(sql_insert_admin_user2)
        con.commit()
        
        # 在该数据库下创建商品信息表
        sql_create_good = '''CREATE TABLE GOOD( 
        GOODID VARCHAR(20) PRIMARY KEY,
        GOODNAME VARCHAR(20) NOT NULL,
        GOODPRICE INT,
        GOODDESCRIPTION VARCHAR(50),
        GOODVOLUME INT,
        GOODSHELF VARCHAR(10));'''
        con.execute(sql_create_good)
        con.commit()

        # 在该数据库下创建订单信息表
        sql1 = '''CREATE TABLE orders( 
        ORDERID VARCHAR(20) ,
        CUSTOMERID VARCHAR(20),
        GOODID VARCHAR(10),
        ORDERVOLUME INT,
        ORDERPRICE float);'''
        con.execute(sql1)
        con.commit()
        
        # 在该数据库下创建货架信息表
        sql_create_shelf = '''CREATE TABLE SHELF(
                        SHELFID VARCHAR(20)PRIMARY KEY,
                        SHELFPLACE VARCHAR(20) );'''
        con.execute(sql_create_shelf)
        con.commit()



    return con  # 返回数据库连接


def check_login(userid, password, usertype):
    """检查用户信息是否正确"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT USERNAME FROM UserInfo WHERE USERID="{0}"
        AND PASSWORD="{1}"AND USERTYPE="{2}"'''
        sql = sql_pattern.format(userid, password, usertype)
        cur = con.execute(sql)
        row = cur.fetchone()
        if row:
            r = tuple(row)
            return r[0]
        else:
            return False
    finally:
        con.close()


def change_password(userid, password):
    """修改用户密码"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''UPDATE UserInfo SET PASSWORD="{1}"
        WHERE USERID="{0}"'''
        sql = sql_pattern.format(userid, password)
        con.execute(sql)
        con.commit()
    finally:
        con.close()


# 用户管理
def check_user_id(userid):
    """检查UserInfo中是否存在userid"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT USERID,USERNAME FROM UserInfo WHERE USERID="{0}"'''
        sql = sql_pattern.format(userid)
        cr = con.execute(sql)
        row = cr.fetchone()
        if row:
            return row[1]  # 返回用户名
        else:
            return False
    finally:
        con.close()


def get_user_list(user_type):
    """查找数据库UserInfo表,获取类型为user_type的用户信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT USERID,USERNAME,GENDER,PHONE,BIRTHDAY
                    FROM UserInfo WHERE USERTYPE="{0}"'''
        sql = sql_pattern.format(user_type)
        results = con.execute(sql)
        users = results.fetchall()
        user_list = []
        for user in users:
            user_list.append(user)
        return user_list
    finally:
        con.close()


def insert_user(usertype, userid, username, gender, birthday, phone):
    """插入一条记录到UserInfo表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO UserInfo(USERID, USERNAME, GENDER,BIRTHDAY,
        PHONE,USERTYPE,PASSWORD)
        VALUES(?,?,?,?,?,?,?)'''
        con.execute(sql, (userid, username, gender, birthday,  phone, usertype, '123456'))
        con.commit()
    finally:
        con.close()


def update_user(username, gender, birthday, phone,userid):
    """更新一条记录到UserInfo表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE UserInfo
        SET USERNAME=?
        ,GENDER=?
        ,BIRTHDAY=?
        ,PHONE=?
        WHERE USERID=?'''
        con.execute(sql, (username, gender, birthday, phone, userid))
        con.commit()
    finally:
        con.close()


def delete_user(userid):
    """从UserInfo表中删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM UserInfo
        WHERE USERID=?'''
        con.execute(sql, (userid,))
        con.commit()
    finally:
        con.close()
#商品管理
def check_good_id(goodid):
    """检查good表中是否存在goodid"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT GOODID,GOODNAME FROM GOOD WHERE GOODID="{0}"'''
        sql = sql_pattern.format(goodid)
        cur = con.execute(sql)
        row = cur.fetchone()
        if row:
            return row[1]
        else:
            return False
    finally:
        con.close()
def check_good_volume(goodid):
    """检查该商品的库存量"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT GOODID,GOODvolume FROM GOOD WHERE GOODID="{0}"'''
        sql = sql_pattern.format(goodid)
        cur = con.execute(sql)
        row = cur.fetchone()
        print(row)
        if row[1]>0:
            return row[1]
        else:
            return False
    finally:
        con.close()


def get_good_list():
    """查找数据库good表,获取商品信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT GOODID,GOODNAME,GOODPRICE,GOODDESCRIPTION,GOODVOLUME,GOODSHELF FROM GOOD'''
        results = con.execute(sql)
        good = results.fetchall()
        good_list = []
        for i in good:
            good_list.append(i)
        return good_list
    finally:
        con.close()

def get_good_lookfor(goodid):
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT GOODID,GOODNAME,GOODPRICE,GOODDESCRIPTION,GOODVOLUME,GOODSHELF FROM GOOD where goodid=?'''
        results = con.execute(sql,(goodid,))
        good_lookfor = results.fetchall()
        return good_lookfor
    finally:
        con.close()


def insert_good(goodid, goodname, goodprice, gooddescription,goodvolume,goodshelf):
    """插入一条记录到good表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO GOOD(GOODID,GOODNAME,GOODPRICE,GOODDESCRIPTION,GOODVOLUME,GOODSHELF)
        VALUES(?,?,?,?,?,?)'''
        con.execute(sql, (goodid, goodname, goodprice, gooddescription,goodvolume,goodshelf))
        con.commit()
    finally:
        con.close()

#商品入库，数量改变
def addmore_good(goodid,goodvolume):
    con = get_create_db(DBFILE)
    cur = con.cursor()  # 创建游标
    try:
        sql1 = '''SELECT GOODID,GOODVOLUME FROM GOOD where goodid="{}"'''
        sql1_format=sql1.format(goodid)
        cur.execute(sql1_format)
        this_good = cur.fetchone()
        newvolume=this_good[1]+goodvolume
        sql2= '''UPDATE good
        SET GOODVOLUME=?     
        WHERE GOODID=?'''
        con.execute(sql2, (newvolume, goodid))
        con.commit()
    finally:
        con.close()

def out_good(goodid,goodvolume):
    con = get_create_db(DBFILE)
    cur = con.cursor()  # 创建游标
    try:
        sql1 = '''SELECT GOODID,GOODVOLUME FROM GOOD where goodid="{}"'''
        sql1_format=sql1.format(goodid)
        cur.execute(sql1_format)
        this_good = cur.fetchone()
        newvolume=this_good[1]-goodvolume
        sql2= '''UPDATE good
        SET GOODVOLUME=?     
        WHERE GOODID=?'''
        con.execute(sql2, (newvolume, goodid))
        con.commit()
    finally:
        con.close()


def update_good(goodname, goodprice, gooddescription,goodvolume,goodshelf,goodid,):
    """更新一条记录到CORE表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE good
        SET GOODNAME=?
        ,GOODPRICE=?
        ,GOODDESCRIPTION=?
        ,GOODVOLUME=?
        ,GOODSHELF=?
        WHERE GOODID=?'''
        con.execute(sql, (goodname, goodprice, gooddescription, goodvolume, goodshelf,goodid))
        con.commit()
    finally:
        con.close()


def delete_good(goodid):
    """从GOOD表中删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM GOOD
        WHERE GOODID=?'''
        con.execute(sql, (goodid,))
        con.commit()
    finally:
        con.close()


#订单信息
def check_order_id(orderid):
    """检查orders表中是否存在orderid"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT ORDERID,CUSTOMERID FROM ORDERs WHERE orderID="{0}"'''
        sql = sql_pattern.format(orderid)
        cur = con.execute(sql)
        row = cur.fetchone()
        if row:
            return True
        else:
            return False
    finally:
        con.close()


def get_order_list():
    """查找数据库orders,获取订单信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT ORDERID,CUSTOMERID, GOODID, ORDERVOLUME, ORDERPRICE FROM ORDERs'''
        results = con.execute(sql)
        orderss = results.fetchall()
        order_list = []
        for i in orderss:
            order_list.append(i)
        return order_list
    finally:
        con.close()


def insert_order(orderid,customerid,goodid,ordervolume,orderprice):
    """插入一条记录到order表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO ORDERs(ORDERID,CUSTOMERID,GOODID,ORDERVOLUME,ORDERPRICE)
        VALUES (?,?,?,?,?)'''
        con.execute(sql, (orderid,customerid,goodid,ordervolume,orderprice))
        con.commit()
    finally:
        con.close()

def get_order_lookfor(orderid):
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT orderID,customerid,goodid,ordervolume,orderprice FROM orders where orderid=?'''
        results = con.execute(sql,(orderid,))
        order_lookfor = results.fetchall()
        return order_lookfor
    finally:
        con.close()

def tuihuo_order(orderid,ordervolume):
    con = get_create_db(DBFILE)
    cur = con.cursor()  # 创建游标
    try:
        sql1 = '''SELECT orderid,ordervolume FROM orders where orderid="{}"'''
        sql1_format=sql1.format(orderid)
        cur.execute(sql1_format)
        this_good = cur.fetchone()
        newvolume=this_good[1]-ordervolume
        sql2= '''UPDATE orders
        SET orderVOLUME=?     
        WHERE orderID=?'''
        con.execute(sql2, (newvolume, orderid))
        con.commit()
    finally:
        con.close()

def update_order(orderid,customerid,goodid,ordervolume,orderprice):
    """更新一条信息到order表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE ORDERs
        SET CUSTOMERID=?
        ,GOODID=?
        ,ORDERVOLUME=?
        ,ORDERPRICE=?
        WHERE ORDERID=?'''
        con.execute(sql, (customerid,goodid,ordervolume,orderprice,orderid))
        con.commit()
    finally:
        con.close()


def delete_order(orderid):
    """从order表删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM ORDERs
        WHERE ORDERID=?'''
        con.execute(sql, (orderid,))
        con.commit()
    finally:
        con.close()
#货架信息
def check_shelf_id(shelfid):
    """检查shelf表中是否存在shelfid,"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT SHELFID FROM SHELF
        WHERE SHELFID=?'''
        cur = con.execute(sql, (shelfid,))
        row = cur.fetchone()
        if row:
            return True
        else:
            return False
    finally:
        con.close()


def get_shelf_list():
    """找数据库shelf表,获取shelf摆放信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT SHELFID,SHELFPLACE FROM SHELF;'''
        results = con.execute(sql)
        shelfs = results.fetchall()
        shelf_list = []
        for i in shelfs:
            shelf_list.append(i)
        return shelf_list
    finally:
        con.close()


def insert_shelf(shelfid,shelfplace):
    """插入一条信息到SHELF表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO SHELF(SHELFID,SHELFPLACE)
        VALUES(?,?)'''
        con.execute(sql, (shelfid,shelfplace))
        con.commit()
    finally:
        con.close()


def delete_shelf(shelfid):
    """从GRADE表删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM SHELF
        WHERE SHELFID=?'''
        con.execute(sql, (shelfid, ))
        con.commit()
    finally:
        con.close()
def update_shelf(shelfplace,shelfid):
    """更新一条信息到shelf表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE SHELF
        SET shelfplace=?
        WHERE SHELFID=?'''
        con.execute(sql, ( shelfplace,shelfid))
        con.commit()
    finally:
        con.close()

def  get_order_goodprice(goodid):
    con = get_create_db(DBFILE)
    try:
        sql = '''select goodprice from good where goodid=?'''
        results = con.execute(sql,(goodid,))
        goods = results.fetchone()
        return goods[0]
        print(goods[0])
    finally:
        con.close()