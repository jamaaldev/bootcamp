/*
Create database database2;
use database2;

Intro to Relational Databases

Multiple Tables working/interacting together.

people: people and their details
jobs: list of jobs

Bob: Software Engineering
George: Software Developer
Oliver: Technician

Keys:
Primary Keys
Foreign Keys


CREATE TABLE people (
	ID int NOT NULL,
    FirstName varchar(255),
    LastName varchar(255),
    Age int,
    information text,
    PRIMARY KEY (ID)
);

-- FOREIGN KEY (internalColumn) REFERENCES ForeignTable(Key)

CREATE TABLE jobs (
	JobID int NOT NUll,
    JobTitle varchar(255),
    JobDescription text,
    JobSalary int,
    PersonID int,
    PRIMARY KEY (JobID),
    FOREIGN KEY (PersonID) REFERENCES people(ID)
);

insert into people values
	(1, "Bob", "Johnson", 25, "A Straight forward and effective man"),
	(2, "George", "Johnson", 24, "A laid back person"),
    (3, "Oliver", "Rimmington", 24, "Jolly good man");

*/

-- Join STATEMENT
/*
JOIN otherTableName ON 1stTable.keycolumn = 2ndTable.keycolumn
*/

Select * from people;

SELECT firstname, age, jobs.JobTitle
FROM people
JOIN jobs ON people.id = jobs.personID;


-- Rental Example

select title.tname, rental.datetaken
from title
JOIN rental on rental.titleid = title.titleid;

select title.tname, rental.datereturned
from title
JOIN rental on rental.titleid = title.titleid;

-- Find out the names of the members along with the film they've taken and date

SELECT member.memberid, member.mfname, title.tname, rental.datetaken, rental.rentalid
FROM member
JOIN rental on rental.memberid = member.memberid
JOIN title on title.titleid = rental.titleid

Where member.memberid = 2
Order by memberid asc;

-- Excercise Solutions

/*
SELECT member.mfname, title.tname, rental.datetaken 
FROM member
JOIN title
JOIN rental
ORDER BY rental.rentalID DESC
LIMIT 5;

Select member.memberid, member.mfname, title.tname, rental.datetaken
from member
JOIN rental on rental.memberid = member.memberid
JOIN title on title.titleid = rental.titleid
Where member.memberid <= 5;
*/
-- 1.) Return the first 5 Rentals, Including the FilmTitle and Persons name

-- Select the columns we want
SELECT rental.rentalid, rental.datetaken, member.mfname, title.tname
FROM Rental
-- Join the Other tables (JOIN otherTable ON condition)
JOIN Member ON member.memberid = rental.memberid
JOIN Title ON title.titleid = rental.titleid
-- Order and limit to 5 results
Order by rental.rentalid
LIMIT 5;

-- 2.) Find the rentals that involve only the people from manchester
SELECT rental.rentalid, rental.datetaken, member.mfname, member.maddress, title.tname
FROM Rental
JOIN member on member.memberid = rental.memberid
JOIN title on title.titleid = rental.titleid
WHERE maddress = "Manchester";

-- 3.) Create a new Title called Fast and Furious
Insert into title Values (6, "Fast and Furious 1", "13");
Select * from title;

-- 4.) Tim Rented fast and furious, returned a week later. would be due a month from when he rented it.
/*

INSERT INTO rental
VALUES (11, 2, 6, str_to_date('06-02-2023', '%d-%m-%Y'), str_to_date('06-03-2023', '%d-%m-%Y'), NULL);

INSERT INTO rental
VALUES (11, 2, 6, DATE("2023-02-06"), DATE("2023-03-06"), NULL);
*/

UPDATE Rental
Set datereturned = DATE("2023-02-13")
WHERE rentalid = 11;

