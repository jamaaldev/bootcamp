
/*
min()
max()
count()
sum()
avg()
--------

-- select min(age) from mock_data4;
-- select max(age) from mock_data4;
-- select count(age) from mock_data4;
-- select sum(age) from mock_data4;
-- select avg(age) from mock_data4;
-- SELECT CONCAT(UCASE(MID(email,1,1)),MID(email,2)) AS email FROM mock_data4;

------------
upper()
lower()
length()
reverse()
concat()

-------------
now()
date_format()
year()
month()
day()
---dateformat---
%d
%m
%y
%t
------------
database()
user()
version()

------------
wildcards
%a
%a%
g%e

C___ any latter start from c only has 4 latter after
_
where column
like pateern
*/


/*
Excercises (30 Mins)Mock_data4:
- Delete the First Record
- Deletes records of those with First_names ending with A
- Find the Minimum Salary Value 
- Delete records of those aged under 18
- Find the Average salary of those over 35
- Find the number of salaries over 150 000
- Find the Average salary with those with second names that begin with C
- Update the salary of those with "e" as the second letter of in their name to 100 000
*/
/*
Done Task 1
first checking the first_name to see which person we want to update--  
-- select * from mock_data4 where first_name like '%a';
-- delete from mock_data4 where first_name like '%a';
*/

/*
Done Task 2
-- select min(salary) from mock_data4;
*/

/*
Done Task 3
first checking  
select * from mock_data4 where age < 18;
-- delete from mock_data4 where age < 18;
*/
/*
Done Task 4
select avg(salary) from mock_data4 where age > 35;
*/

/*
Done Task 5
select * from mock_data4 where salary > '150000';
*/

/*
Done Task 6
select avg(salary) from mock_data4 where last_name like 'c%';
*/
/*
Done Task 7
 update and check if updated.
-- update mock_data4  set salary = '100000'  where first_name like '_e%';
-- select * from mock_data4  where first_name like '_e%';



*/

select * from mock_data4



