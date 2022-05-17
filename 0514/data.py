# -*- coding: utf-8 -*-
import os
import sqlite3

DBFILE = 'jwxt.db'  # 数据库,全局变量


def get_create_db(db_filename):
    """A打开本地数据库文件d_filename,并返回数据库连接con"""
    """如果本地数据库文件dbfilename,在创建数据库和UserInfo表"""
    if os.path.exists(db_filename):
        con = sqlite3.connect(db_filename)
    else:
        con = sqlite3.connect(db_filename)
        # 在该数据库下创建用户信息表
        sql_create_UserInfo = '''CREATE TABLE UserInfo(
                            USERID VARCHAR(20) PRIMARY KEY,
                            USERNAME VARCHAR(20) NOT NULL,
                            GENDER VARCHAR(2),
                            BIRTHDAY VARCHAR(11),
                            DEPARTMENT VARCHAR(50),
                            PHONE VARCHAR(20),
                            USERTYPE VARCHAR(2),
                            PASSWORD VARCHAR(20) NOT NULL);'''
        con.execute(sql_create_UserInfo)
        sql_insert_UserInfo = '''INSERT INTO UserInfo VALUES
                                ('J001','张教务','女','1988/5/2','物理系','13912345678','教务','123456');'''
        con.execute(sql_insert_UserInfo)
        con.commit()
        # 在该数据库下创建课程信息表
        sql_create_COURSE = '''CREATE TABLE Course( 
        COURSEID VARCHAR(20) PRIMARY KEY,
        COURSENAME VARCHAR(20) NOT NULL,
        CREDIT INT,
        DESCRIPTION VARCHAR(100));'''
        con.execute(sql_create_COURSE)
        con.commit()
        # 在该数据库下创建教学班号表
        sql_create_JXB = '''CREATE TABLE JXB(
        JXBID VARCHAR(20)PRIMARY KEY,
        COURSEID VARCHAR(20) NOT NULL,
        USERID VARCHAR(20) NOT NULL,
        DESCRIPTION VARCHAR(100));'''
        con.execute(sql_create_JXB)
        con.commit()
        # 在该数据库下创建学生成绩表
        sql_create_JXB = '''CREATE TABLE Grades(
        JXBID VARCHAR (20),
        USERID VARCHAR (20),
        SCORE INT,
        PRIMARY KEY(
        JXBID,
        USERID));'''
        con.execute(sql_create_JXB)
        con.commit()
    return con  # 返回数据库连接


def check_login(userid, password, usertype):
    """检查用户录信息是否下确"""
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


# 课程管理
def check_user_id(userid):
    """4A检查UserInfo中是否存在userid"""
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
        sql_pattern = '''SELECT USERID,USERNAME,GENDER,DEPARTMENT,PHONE,BIRTHDAY
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


def insert_user(usertype, userid, username, gender, birthday, department, phone):
    """插入一条记录到UserInfo表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO UserInfo(USERID, USERNAME, GENDER,BIRTHDAY,DEPARTMENT,
        PHONE,USERTYPE,PASSWORD)
        VALUES(?,?,?,?,?,?,?,?)'''
        con.execute(sql, (userid, username, gender, birthday, department, phone, usertype, '123456'))
        con.commit()
    finally:
        con.close()


def update_user(userid, username, gender, birthday, department, phone):
    """A更新一条记录到UserInfo表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE UserInfo
        SET USERNAME=?
        ,GENDER=?
        ,BIRTHDAY=?
        ,DEPARTMENT=?
        ,PHONE=?
        WHERE USERID=?'''
        con.execute(sql, (username, gender, birthday, department, phone, userid))
        con.commit()
    finally:
        con.close()


def delete_user(userid):
    """从User Info表中删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM UserInfo
        WHERE USERID=?'''
        con.execute(sql, (userid,))
        con.commit()
    finally:
        con.close()


def check_course_id(courseid):
    """*A检查Course表中是否存在courseid"""
    con = get_create_db(DBFILE)
    try:
        sql_pattern = '''SELECT COURSEID,COURSENAME FROM COURSE WHERE COURSEID="{0}"'''
        sql = sql_pattern.format(courseid)
        cur = con.execute(sql)
        row = cur.fetchone()
        if row:
            return row[1]  # 返回课程名称
        else:
            return False
    finally:
        con.close()


def get_course_list():
    """0查找数据库Course表,获取课程信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT COURSEID,COURSENAME,CREDIT,DESCRIPTION FROM Course'''
        results = con.execute(sql)
        courses = results.fetchall()
        course_list = []
        for course in courses:
            course_list.append(course)
        return course_list
    finally:
        con.close()


def insert_course(courseid, coursename, credit, description):
    """插入一条记录到Course表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO COURSE(COURSEID,COURSENAME,CREDIT,DESCRIPTION)
        VALUES(?,?,?,?)'''
        con.execute(sql, (courseid, coursename, credit, description))
        con.commit()
    finally:
        con.close()


def update_course(courseid, coursename, credit, description):
    """更新一条记录到CORE表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE COURSE
        SET COURSENAME=?
        ,CREDIT=?
        ,DESCRIPTION=?
        WHERE COURSEID=?'''
        con.execute(sql, (coursename, credit, description, courseid))
        con.commit()
    finally:
        con.close()


def delete_course(courseid):
    """从CORE表中删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM COURSE
        WHERE COURSEID=?'''
        con.execute(sql, (courseid))
        con.commit()
    finally:
        con.close()
    ###开课计划#################333


def check_jxb_id(jxbid):
    """格查T区B中是否存在jxbid"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT j.COURSEID,C.COURSENAME,j.USERID,u.USERNAME,j.DESCRIPTION
        FROM JXB j,Course c,UserInfo u
        WHERE j.COURSEID=C.COURSEID
        AND j.USERID=u.USERID
        AND j.JXBID=?;'''
        cur = con.execute(sql, (jxbid,))
        row = cur.fetchone()
        if row:
            return row
        else:
            return False
    finally:
        con.close()


def get_jxb_list():
    """查找数据库JXB,获取课程安排教学班号信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT j.JXBID,j.COURSEID,C.COURSENAME,j.USERID,u.USERNAME,
        j.DESCRIPTION
        FROM JXB j,Course c,UserInfo u
        WHERE j.COURSEID=C.COURSEID
        AND j.USERID=u.USERID;'''
        results = con.execute(sql)
        jxbs = results.fetchall()
        jxb_list = []
        for jxb in jxbs:
            jxb_list.append(jxb)
        return jxb_list
    finally:
        con.close()


def insert_jxb(jxbid, courseid, userid, description):
    """插入一条记录到xB表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO JXB(JXBID,COURSEID,USERID,DESCRIPTION)
        VALUES (?,?,?,?)'''
        con.execute(sql, (jxbid, courseid, userid, description))
        con.commit()
    finally:
        con.close()


def update_jxb(jxbid, courseid, userid, description):
    """更新一条信息到KB表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE JXB
        SET COURSEID=?
        ,USERID=?
        ,DESCRIPTION=?
        WHERE JXBID=?'''
        con.execute(sql, (courseid, userid, description, jxbid))
        con.commit()
    finally:
        con.close()


def delete_jxb(jxbid, e):
    """从JXB表删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM JXB
        WHERE JXBID=?'''
        con.execute(sql, (jxbid,))
        con.commit()
    finally:
        con.close()
    ####学生选课################


def check_grade_id(jxbid, userid):
    """检查Grade表中是否存在jxbid、userid,即userid是否已经选jxbid"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT jxbid FROM Grades
        WHERE JXBID=?
        AND USERID=?'''
        cur = con.execute(sql, (jxbid, userid))
        row = cur.fetchone()
        if row:
            return True
        else:
            return False
    finally:
        con.close()


def get_grade_list_by_student(userid):
    """找数据库Grade表,获取学生userid选课信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT g.JXBID,j.COURSEID,C.COURSENAME,j.USERID,u.USERNAME,
        j.DESCRIPTION,g.SCORE
        FROM Grades g,JXB j,Course c,UserInfo u
        WHERE g.JXBID=j.JXBID
        AND j.COURSEID=C.COURSEID
        AND j.USERID=u.USERID
        AND g.USERID=?;'''
        results = con.execute(sql, (userid,))
        grades = results.fetchall()
        grade_list = []
        for grade in grades:
            grade_list.append(grade)
        return grade_list
    finally:
        con.close()


def insert_grade(jxbid, userid):
    """插入一条信息到GRADE表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''INSERT INTO Grades(JXBID,USERID)
        VALUES(?,?)'''
        con.execute(sql, (jxbid, userid))
        con.commit()
    finally:
        con.close()


def delete_grade(jxbid, userid):
    """从GRADE表删除一条记录"""
    con = get_create_db(DBFILE)
    try:
        sql = '''DELETE FROM Grades
        WHERE JXBID=?
        AND USERID=?'''
        con.execute(sql, (jxbid, userid))
        con.commit()
    finally:
        con.close()


# 教师成绩登录
def get_jxbid_list_by_user(userid):
    """查找数据库JXB表,获取指定教师userid授课课程信息JXBID列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT j.JXBID
        FROM JXB j
        WHERE j.USERID=?;'''
        results = con.execute(sql, (userid,))
        jxbs = results.fetchall()
        jxbIdlist = []
        for jxb in jxbs:
            jxbIdlist.append(jxb[0])
        return jxbIdlist
    finally:
        con.close()


def get_grade_list_by_jxbid(jxbid):
    """查找数据库GRADE表,获取指定课程的学生选课信息列表"""
    con = get_create_db(DBFILE)
    try:
        sql = '''SELECT g.USERID,u.USERNAME,u.GENDER,u.DEPARTMENT,g.SCORE
        FROM Grades g,UserInfo u
        WHERE g.USERID=u.USERID
        AND g.JXBID=?;'''
        results = con.execute(sql, (jxbid,))
        grades = results.fetchall()
        grade_list = []
        for grade in grades:
            grade_list.append(grade)
        return grade_list
    finally:
        con.close()


def update_grade_score(grades_list):
    """更新学生成绩信息列表到数据库Grade"""
    con = get_create_db(DBFILE)
    try:
        sql = '''UPDATE Grades
        SET SCORE=?
        WHERE JXBID=?
        AND USERID=?;'''
        for grade in grades_list:
            con.execute(sql, grade)
        con.commit()
    finally:
        con.close()
