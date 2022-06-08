create table Dormitory
(
    DormID   int auto_increment comment '楼栋ID'
        primary key,
    DormName varchar(20) not null comment '楼栋名',
    constraint Dormitory_DormName_uindex
        unique (DormName),
    constraint Dormitory_ID_uindex
        unique (DormID)
)
    comment '宿舍楼栋表';

create table RSA
(
    KeyType    varchar(20)   not null comment '密钥种类'
        primary key,
    KeyContent varchar(2500) not null comment '密钥内容',
    constraint RSA__KeyType_uindex
        unique (KeyType)
)
    comment 'RSA密钥';

create table Room
(
    RoomID   int auto_increment comment '寝室ID'
        primary key,
    DormID   int         not null comment '楼栋ID',
    RoomName varchar(10) not null comment '寝室名',
    Floor    int         null comment '楼层',
    constraint Room_RoomID_uindex
        unique (RoomID),
    constraint FK_Room_Dormitory
        foreign key (DormID) references Dormitory (DormID)
)
    comment '寝室表';

create table Students
(
    StudentCode varchar(20)          not null comment '学号'
        primary key,
    StudentName varchar(20)          not null comment '学生姓名',
    PassWord    varchar(500)         not null comment '账户密码',
    RoomID      int                  not null comment '寝室ID',
    isAdmin     tinyint(1) default 0 not null comment '是否为楼长',
    constraint table_name_StudentCode_uindex
        unique (StudentCode),
    constraint FK_Students_Room
        foreign key (RoomID) references Room (RoomID)
)
    comment '学生表';

create table Task
(
    TaskID        int auto_increment comment '任务ID'
        primary key,
    TaskContent   varchar(1000)        not null comment '任务内容',
    TaskDormID    int                  not null comment '任务发布楼栋',
    PublisherCode varchar(20)          null comment '发布人学号',
    TaskStatus    tinyint(1) default 1 not null comment '任务状态',
    PublishTime   datetime             not null comment '发布时间',
    constraint Task_TaskID_uindex
        unique (TaskID),
    constraint FK_Task_Dormitory
        foreign key (TaskDormID) references Dormitory (DormID),
    constraint FK_Task_Students
        foreign key (PublisherCode) references Students (StudentCode)
)
    comment '任务发布表';

create table PicURL
(
    StudentCode      varchar(20)          not null comment '上传人学号',
    TaskID           int                  not null comment '所属任务ID',
    AddTime          datetime             not null comment '上传时间戳',
    pictureurl       varchar(400)         not null comment '图片服务器地址',
    isConfirmed      tinyint(1) default 0 not null comment '是否审核通过',
    CheckStudentCode varchar(20)          null comment '审核人学号',
    primary key (StudentCode, TaskID, AddTime),
    constraint FK_PicURL_CheckStudents
        foreign key (CheckStudentCode) references Students (StudentCode),
    constraint FK_PicURL_Students
        foreign key (StudentCode) references Students (StudentCode),
    constraint FK_PicURL_Task
        foreign key (TaskID) references Task (TaskID)
)
    comment '上传图片链接表';

create definer = root@`%` view view_dormandroom as
select `R`.`DormID`                         AS `DormID`,
       `obj_bigwork`.`Dormitory`.`DormName` AS `DormName`,
       `R`.`RoomID`                         AS `RoomID`,
       `R`.`RoomName`                       AS `RoomName`,
       `R`.`Floor`                          AS `Floor`
from (`obj_bigwork`.`Dormitory` join `obj_bigwork`.`Room` `R` on ((`obj_bigwork`.`Dormitory`.`DormID` = `R`.`DormID`)));

-- comment on column view_dormandroom.DormID not supported: 楼栋ID

-- comment on column view_dormandroom.DormName not supported: 楼栋名

-- comment on column view_dormandroom.RoomID not supported: 寝室ID

-- comment on column view_dormandroom.RoomName not supported: 寝室名

-- comment on column view_dormandroom.Floor not supported: 楼层

create definer = root@`%` view view_uploaddetail as
select `obj_bigwork`.`PicURL`.`StudentCode`      AS `StudentCode`,
       `obj_bigwork`.`PicURL`.`TaskID`           AS `TaskID`,
       `obj_bigwork`.`PicURL`.`AddTime`          AS `AddTime`,
       `obj_bigwork`.`PicURL`.`pictureurl`       AS `pictureurl`,
       `obj_bigwork`.`PicURL`.`isConfirmed`      AS `isConfirmed`,
       `obj_bigwork`.`PicURL`.`CheckStudentCode` AS `CheckStudentCode`,
       `obj_bigwork`.`Students`.`StudentName`    AS `StudentName`,
       `obj_bigwork`.`Students`.`RoomID`         AS `RoomID`,
       `obj_bigwork`.`Task`.`TaskContent`        AS `TaskContent`,
       `obj_bigwork`.`Task`.`TaskDormID`         AS `TaskDormID`
from ((`obj_bigwork`.`PicURL` join `obj_bigwork`.`Students`) join `obj_bigwork`.`Task`)
where ((`obj_bigwork`.`PicURL`.`StudentCode` = `obj_bigwork`.`Students`.`StudentCode`) and
       (`obj_bigwork`.`PicURL`.`TaskID` = `obj_bigwork`.`Task`.`TaskID`));

-- comment on column view_uploaddetail.StudentCode not supported: 上传人学号

-- comment on column view_uploaddetail.TaskID not supported: 所属任务ID

-- comment on column view_uploaddetail.AddTime not supported: 上传时间戳

-- comment on column view_uploaddetail.pictureurl not supported: 图片服务器地址

-- comment on column view_uploaddetail.isConfirmed not supported: 是否审核通过

-- comment on column view_uploaddetail.CheckStudentCode not supported: 审核人学号

-- comment on column view_uploaddetail.StudentName not supported: 学生姓名

-- comment on column view_uploaddetail.RoomID not supported: 寝室ID

-- comment on column view_uploaddetail.TaskContent not supported: 任务内容

-- comment on column view_uploaddetail.TaskDormID not supported: 任务发布楼栋

create
    definer = root@`%` procedure get_roomcompletesitui_fromtask(IN tskid varchar(20))
begin
    declare taskdorm int;
    set taskdorm = (select TaskDormID from Task where TaskID = tskid);
    select distinct Room.RoomID,Room.RoomName,ifnull(t1.addtime,'/'),ifnull(t1.isConfirmed,0.5) as confirm
    from Room
             left join (select view_dormandroom.RoomID, max(addtime) as addtime,isConfirmed
                        from view_uploaddetail,
                             view_dormandroom
                        where view_dormandroom.RoomID = view_uploaddetail.RoomID
                          and TaskDormID = taskdorm
                          and TaskID = tskid
                        group by view_dormandroom.RoomID,
                                 view_dormandroom.RoomName,isConfirmed) t1 on Room.RoomID = t1.RoomID
    join view_dormandroom vd on Room.DormID = vd.DormID
    where vd.DormID = taskdorm
    order by confirm;
end;

create
    definer = root@`%` procedure proc_check_timerate_myrate(IN stcode varchar(20))
begin
    declare rmid int;
    declare dawncount int;
    declare morncount int;
    declare aftcount int;
    declare nightcount int;
    declare totalcount int;
    declare dawnmycount int;
    declare mornmycount int;
    declare aftmycount int;
    declare nightmycount int;
    set rmid = (select RoomID from Students where StudentCode = stcode);
    set dawncount =
            (select count(*) from view_uploaddetail where hour(AddTime) between '00' and '06' and RoomID = rmid);
    set morncount =
            (select count(*) from view_uploaddetail where hour(AddTime) between '07' and '12' and RoomID = rmid);
    set aftcount = (select count(*) from view_uploaddetail where hour(AddTime) between '13' and '18' and RoomID = rmid);
    set nightcount =
            (select count(*) from view_uploaddetail where hour(AddTime) between '19' and '23' and RoomID = rmid);
    set totalcount = (select count(*) from view_uploaddetail where RoomID = rmid);
    set dawnmycount = (select count(*)
                       from view_uploaddetail
                       where hour(AddTime) between '00' and '06' and RoomID = rmid and StudentCode = stcode);
    set mornmycount = (select count(*)
                       from view_uploaddetail
                       where hour(AddTime) between '07' and '12' and RoomID = rmid and StudentCode = stcode);
    set aftmycount = (select count(*)
                      from view_uploaddetail
                      where hour(AddTime) between '13' and '18' and RoomID = rmid and StudentCode = stcode);
    set nightmycount = (select count(*)
                        from view_uploaddetail
                        where hour(AddTime) between '19' and '23' and RoomID = rmid and StudentCode = stcode);
    select dawncount / totalcount,
           morncount / totalcount,
           aftcount / totalcount,
           nightcount / totalcount,
           dawnmycount / dawncount,
           mornmycount / morncount,
           aftmycount / aftcount,
           nightmycount / nightcount;
end;

create
    definer = root@`%` procedure proc_checkcompleterate(IN stcode varchar(20))
begin
    declare rmid int;
    declare dmid int;
    declare up int;
    declare down int;
    set rmid= (select RoomID from Students where StudentCode=stcode);
    set dmid = (select DormID from Room where RoomID=rmid);
    set up = (select count(*) from (SELECT count(*)
          FROM view_uploaddetail
          where RoomID=rmid
          GROUP BY RoomID,
                   TaskID) t1);
    set down=(select count(*) from Task where TaskDormID=dmid);
    select up/down;
end;

create
    definer = root@`%` procedure proc_countroomtaskstatus(IN studentid varchar(20), IN tskid int)
begin
    declare rid int;
    set rid = (select roomid from Students where StudentCode = studentid);
    select count(*) from view_uploaddetail where RoomID = rid and TaskID = tskid;
end;

create
    definer = root@`%` procedure proc_createaccount(IN stcode varchar(20), IN stname varchar(20), IN Pass varchar(500),
                                                    IN dmname varchar(20), IN dmroom varchar(10))
begin
    declare rmid int;
    set rmid = (select RoomID
                from Room,
                     Dormitory
                where Room.DormID = Dormitory.DormID
                  and Dormitory.DormName = dmname
                  and Room.RoomName = dmroom);
    insert into Students(StudentCode, StudentName, PassWord, RoomID)
    values (stcode, stname, Pass, rmid);
end;

create
    definer = root@`%` procedure proc_get_alltaskrate()
begin
    select Task.TaskID, ifnull(t1.rate, 0) as rate
    from Task
             left join (SELECT TaskID,
                               count(distinct RoomID) / (select distinct count(distinct Students.RoomID)
                                                         from view_dormandroom,
                                                              Students
                                                         where Students.RoomID = view_dormandroom.RoomID) as rate
                        FROM view_uploaddetail
                        GROUP BY TaskID) t1 on t1.TaskID = Task.TaskID
    order by Task.TaskID desc
    limit 10;
end;

create
    definer = root@`%` procedure proc_get_everytaskrate(IN dmid int)
begin
    select Task.TaskID, ifnull(t1.rate, 0) as rate
    from Task
             left join (SELECT TaskID,
                               count(distinct RoomID) / (select distinct count(distinct Students.RoomID)
                                                         from view_dormandroom,
                                                              Students
                                                         where Students.RoomID = view_dormandroom.RoomID
                                                           and view_dormandroom.DormID = dmid) as rate
                        FROM view_uploaddetail
                        where TaskDormID = dmid
                        GROUP BY TaskID) t1 on t1.TaskID = Task.TaskID
    where TaskDormID = dmid
    order by Task.TaskID desc
    limit 10;
end;

create
    definer = root@`%` procedure proc_getdormrate(IN dmid int)
begin
    declare up int;
    declare down int;
    declare roomnum int;
    set up = (select count(*) from (SELECT count(*)
          FROM view_uploaddetail
          where TaskDormID = dmid
          GROUP BY RoomID,
                   TaskID) t1);
    set down=(select count(*) from Task where TaskDormID=dmid);
    set roomnum=(select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid);
    select up/down/roomnum;
end;

create
    definer = root@`%` procedure proc_geteachtaskone(IN stcode varchar(20))
begin
    declare rmid int;
    set rmid= (select RoomID from Students where StudentCode=stcode);
    SELECT RoomID,
                 TaskID,
                 max(AddTime) time,
                 isConfirmed,
                 taskcontent
          FROM view_uploaddetail
          where RoomID = rmid
          GROUP BY RoomID,
                   TaskID,
                   isConfirmed
          order by max(AddTime) desc;
end;

create
    definer = root@`%` procedure proc_getfloor_room(IN dmid varchar(20))
begin
    declare roomnum1 int;
    declare roomnum2 int;
    declare roomnum3 int;
    declare roomnum4 int;
    declare roomnum5 int;
    declare roomnum6 int;
    declare roomnum7 int;
    declare roomnumother int;
    set roomnum1 = (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 1);
    set roomnum2= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 2);
    set roomnum3= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 3);
    set roomnum4= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 4);
    set roomnum5= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 5);
    set roomnum6= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 6);
    set roomnum7= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor = 7);
    set roomnumother= (select distinct count(distinct Students.RoomID)
                    from view_dormandroom,
                         Students
                    where Students.RoomID = view_dormandroom.RoomID
                      and view_dormandroom.DormID = dmid
                      and Floor not in (1,2,3,4,5,6,7));
    select roomnum1,roomnum2,roomnum3,roomnum4,roomnum5,roomnum6,roomnum7,roomnumother;
end;

create
    definer = root@`%` procedure proc_getfloordorminf(IN dmid int, IN flr int)
begin
    select t1.RoomName,
           t1.StudentName,
           ifnull(t2.comnum, 0) / (select count(*) from Task where TaskDormID = dmid) as rate
    from (select distinct view_dormandroom.RoomName               as RoomName,
                          group_concat(StudentName separator ',') as StudentName,
                          Students.RoomID
          from Students,
               view_dormandroom
          where Students.RoomID = view_dormandroom.RoomID
            and view_dormandroom.DormID = dmid
            and Floor = flr
          group by view_dormandroom.RoomName, Students.RoomID) t1
             left join (select RoomID, count(distinct TaskID) as comnum
                        from view_uploaddetail
                        where TaskDormID = dmid
                        group by RoomID) t2
                       on t1.RoomID = t2.RoomID;
end;

create
    definer = root@`%` procedure proc_getotherfloordorminf(IN dmid int)
begin
    select t1.RoomName,
           t1.StudentName,
           ifnull(t2.comnum, 0) / (select count(*) from Task where TaskDormID = dmid) as rate
    from (select distinct view_dormandroom.RoomName               as RoomName,
                          group_concat(StudentName separator ',') as StudentName,
                          Students.RoomID
          from Students,
               view_dormandroom
          where Students.RoomID = view_dormandroom.RoomID
            and view_dormandroom.DormID = dmid
            and Floor not in (1,2,3,4,5,6,7)
          group by view_dormandroom.RoomName, Students.RoomID) t1
             left join (select RoomID, count(distinct TaskID) as comnum
                        from view_uploaddetail
                        where TaskDormID = dmid
                        group by RoomID) t2
                       on t1.RoomID = t2.RoomID;
end;

create
    definer = root@`%` procedure proc_getroomtaskpic(IN studentid varchar(20), IN tskid int)
begin
    declare rid int;
    set rid = (select roomid from Students where StudentCode = studentid);
    select pictureurl,isConfirmed from view_uploaddetail where RoomID = rid and TaskID = tskid;
end;

create
    definer = root@`%` procedure proc_getstudentroom(IN stid int)
begin
    declare rmid int;
    set rmid=(select roomid from Students where studentcode = stid);
    select * from view_dormandroom where RoomID = rmid;
end;

create
    definer = root@`%` procedure proc_insertroomtaskpic(IN stid varchar(20), IN tskid int, IN internetpath varchar(1000))
begin
    insert into PicURL(StudentCode,TaskID,Addtime,pictureurl) values(stid,tskid,now(),internetpath);
end;


