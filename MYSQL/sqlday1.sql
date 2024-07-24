-- comment
/* multi line comment */

-- Introduction to Mysql --

-- SQL - Structured Query Langauge --
/* 
	1. CREATE DATABASE databasename <-- name
    2. USE newdatabase <-- to actived the database
    3. CREATE TABLE tablename <---
*/
-- create database newdatabase;

-- USE newdatabase;

-- CREATE TABLE people (
--  ID int,
--  FirstName varchar(255),
--  LastName varchar(255),
--  Age int,
--  Information text
--  );

 -- SELECT FirstName, LastName FROM people;
--  SELECT * FROM people;
-- INSERT INTO people VALUES(1,'jamaal','mahamaed','5','webdeveloper and game designer');
-- INSERT INTO people VALUES(2,'mahamed','hassan','7','Doctor and 3d designer');
-- INSERT INTO people VALUES(3,'ahmed','salah','7','engineer and 3d designer');
-- SELECT * FROM people ORDER BY ID DESC LIMIT 2;
-- SELECT * FROM people ORDER BY ID ASC LIMIT 2;




-- creating constraints table--
-- create table members(
-- MemeberID int not null,
-- UserName varchar(255) unique,
-- FirstName varchar(255),
-- MemeberStatus varchar(255) default 'Basic',
-- age int check(age >=13)
-- );
-- insert data --
-- insert into members values(1,'jamaaldev','jamaal',default,120);
-- insert into members values(1,'hassandev','hassan',default,520);
-- insert into members(MemeberID,Username,age) values(3,'hussien',520);
-- insert into members(MemeberID,Username,age) values(4,'mahameddev',520);

-- update data --
-- update members set age = 18;
-- update members set  age = 1000 order by age desc ;
-- update members set  age = 1500 where Username = 'jamaaldev' ;
-- update members set  MemeberID = 2  where Username = 'hassandev' ;

-- delete data row --
-- delete from members where Username = 'hussien';

select * from members;