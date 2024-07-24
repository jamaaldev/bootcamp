-- create database database2;
-- use database2;


/*
intro relational Database
*/

-- create table people(
-- ID int not null,
-- FirstName varchar(25),
-- LastName varchar(25),
-- Age int,
-- Information text,
-- primary key (ID)
-- );

-- create table jobs(
-- JobID int not null,
-- JobTitle varchar(25),
-- JobSalary int,
-- PersonID int,
-- JobDescription text,
-- primary key (JobID),
-- foreign key (PersonID) references people(ID)
-- );

-- insert into people values 
-- (1,'jamaal','mahamed',5000,'very nice'),
-- (2,'hassan','hassan','6000','very handsome'),
-- (3,'hussien','hassan','6000','very handsome');



-- insert into jobs (JobID, JobTitle,  JobSalary, JobDescription, PersonID) values 
-- (1,'software engineer',5000,'full-stack webdeveloer',1),
-- (2,'Doctor',5000,'whateve',2),
-- (3,'Doctor',5000,'whateve',3);

-- select FirstName,Age,jobs.jobTitle from people join jobs;
-- select FirstName,Age,jobs.jobTitle from people join jobs on people.id = jobs.personID;

-- select member.memberid, member.mfname,title.tname,rental.datataken,rental.rental.id 
-- from member 
-- join rental on rental.memberid = memberid
-- join title on title.id = rental.titleid
-- ;
