CREATE TABLE STUDENT(
    STUDENT_ID int primary key,
    STUDENT_NAME varchar(255) not null,
    COURSE_ID int not null
);

INSERT INTO STUDENT VALUES (1,'大原　太郎',1);
INSERT INTO STUDENT VALUES (2,'大原　次郎',2);
INSERT INTO STUDENT VALUES (3,'大原　花子',1);

CREATE TABLE COURSE(
    COURSE_ID int primary key,
    COURSE_NAME varchar(255) not null
);

INSERT INTO COURSE VALUES (1,'システム開発');
INSERT INTO COURSE VALUES (2,'AIシステム・データサイエンス');
