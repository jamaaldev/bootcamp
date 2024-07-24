-- CREATE TABLE mock_data3 (
-- 	id INT,
--     first_name varchar(255) NOT NULL,
--     last_name varchar(255),
--     email varchar(255) UNIQUE,
--     Age INT,
--     workStatus varchar(255),
--     PRIMARY KEY (ID)
-- );

-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (1, 'Raynor', 'Conningham', 'rconningham0@dagondesign.com', 32, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (2, 'Tobe', 'Rudolf', 'trudolf1@linkedin.com', 23, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (3, 'Pip', 'Tallach', 'ptallach2@engadget.com', 29, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (4, 'Ingaborg', 'McLeod', 'imcleod3@google.com', 62, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (5, 'Riobard', 'Leith-Harvey', 'rleithharvey4@com.com', 43, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (6, 'Helena', 'Spoole', 'hspoole5@yale.edu', 41, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (7, 'Alikee', 'Hartford', 'ahartford6@myspace.com', 46, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (8, 'Findley', 'Sylvester', 'fsylvester7@google.fr', 62, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (9, 'Dorie', 'Bezzant', 'dbezzant8@virginia.edu', 46, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (10, 'Silvia', 'Down', 'sdown9@google.co.jp', 48, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (11, 'Haydon', 'Macartney', 'hmacartneya@posterous.com', 36, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (12, 'Tully', 'Drohun', 'tdrohunb@home.pl', 34, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (13, 'Armstrong', 'Joyson', 'ajoysonc@chicagotribune.com', 68, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (14, 'Corina', 'Harder', 'charderd@stumbleupon.com', 58, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (15, 'Hillier', 'Itzkovwitch', 'hitzkovwitche@japanpost.jp', 40, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (16, 'Berkley', 'Ayer', 'bayerf@barnesandnoble.com', 69, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (17, 'Noreen', 'Whitfeld', 'nwhitfeldg@auda.org.au', 82, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (18, 'Mehetabel', 'Tomaskunas', 'mtomaskunash@mediafire.com', 35, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (19, 'Adriana', 'Gillies', 'agilliesi@wp.com', 62, null);
-- insert into mock_data3 (id, first_name, last_name, email, age, workStatus) values (20, 'Kinna', 'Beves', 'kbevesj@163.com', 95, null);

-- My Task Done --

-- update mock_data3 set age = 43 where first_name = 'tully';
-- update mock_data3 set email = 'kinnabeves@fakemail.com'  where first_name = 'Kinna';
-- delete  from mock_data3 where age = 62;
-- update mock_data3 set workStatus = 'Working';
-- update mock_data3 set workStatus = 'Retired' where age > 60;

-- alter table add --
/* 
alter table tablename 
add newNameColumn dataType 
delete row
drop column column name dataType
modify column column_name dataType
Rename column oldColumn to newColumn
 */
-- alter table mock_data3 add newColuam text;
-- alter table mock_data3 drop newColuam; 
-- alter table mock_data3 modify Age decimal(10,5);
-- alter table mock_data3 modify Age int;
-- alter table mock_data3 rename column Age to age;
select * from mock_data3;

/*
# Excercise (20 mins)
- Update Tullys Age to 43
- Update Kinna's Email to "kinnabeves@fakemail.com"
- Delete people age 62
- Set Everyones Job Status to Working
- Update the working status of people over 60 to "Retired"

*/