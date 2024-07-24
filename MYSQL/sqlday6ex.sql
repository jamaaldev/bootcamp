-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: dvdrentals
-- ------------------------------------------------------
-- Server version	8.0.31

-- /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
-- /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
-- /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
-- /*!50503 SET NAMES utf8 */;
-- /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
-- /*!40103 SET TIME_ZONE='+00:00' */;
-- /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
-- /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
-- /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
-- /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- --
-- -- Table structure for table `member`
-- --

-- DROP TABLE IF EXISTS `member`;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE `member` (
--   `MemberID` int NOT NULL,
--   `MFname` varchar(20) NOT NULL,
--   `MLname` varchar(20) NOT NULL,
--   `MAddress` varchar(20) NOT NULL,
--   `DOB` date DEFAULT NULL,
--   PRIMARY KEY (`MemberID`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- /*!40101 SET character_set_client = @saved_cs_client */;

-- --
-- -- Dumping data for table `member`
-- --

-- LOCK TABLES `member` WRITE;
-- /*!40000 ALTER TABLE `member` DISABLE KEYS */;
-- INSERT INTO `member` VALUES (1,'John','Smith','Manchester','1980-06-01'),(2,'Tim','Jones','Dubai','1980-12-02'),(3,'Narayan','Khosla','New York','1980-11-02'),(4,'Abdul','Jalloh','Paris','1980-10-02'),(5,'Christian','Perry','Sydney','1980-10-10'),(6,'Zak','Pardis','LA','1980-12-01'),(7,'Waqas','Ahmad','Manchester','1980-03-02');
-- /*!40000 ALTER TABLE `member` ENABLE KEYS */;
-- UNLOCK TABLES;

-- --
-- -- Table structure for table `rental`
-- --

-- DROP TABLE IF EXISTS `rental`;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE `rental` (
--   `RentalID` int NOT NULL,
--   `MemberID` int NOT NULL,
--   `TitleID` int NOT NULL,
--   `DateTaken` date DEFAULT NULL,
--   `DateDueBack` date DEFAULT NULL,
--   `DateReturned` date DEFAULT NULL,
--   PRIMARY KEY (`RentalID`),
--   KEY `MemberID` (`MemberID`),
--   KEY `TitleID` (`TitleID`),
--   CONSTRAINT `rental_ibfk_1` FOREIGN KEY (`MemberID`) REFERENCES `member` (`MemberID`),
--   CONSTRAINT `rental_ibfk_2` FOREIGN KEY (`TitleID`) REFERENCES `title` (`TitleID`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- /*!40101 SET character_set_client = @saved_cs_client */;

-- --
-- -- Dumping data for table `rental`
-- --

-- LOCK TABLES `rental` WRITE;
-- /*!40000 ALTER TABLE `rental` DISABLE KEYS */;
-- INSERT INTO `rental` VALUES (1,1,1,'2022-09-01','2022-09-03','2022-09-03'),(2,2,2,'2022-09-02','2022-09-04','2022-09-04'),(3,3,3,'2022-09-02','2022-09-04','2022-09-04'),(4,4,4,'2022-09-04','2022-09-05','2022-09-05'),(5,5,5,'2022-09-05','2022-09-06','2022-09-06'),(6,1,5,'2022-10-01','2022-10-03','2022-10-03'),(7,2,4,'2022-10-02','2022-10-04','2022-10-04'),(8,3,5,'2022-10-02','2022-10-04','2022-10-04'),(9,1,1,'2022-10-04','2022-10-05','2022-10-05'),(10,2,2,'2022-10-05','2022-10-06','2022-10-06');
-- /*!40000 ALTER TABLE `rental` ENABLE KEYS */;
-- UNLOCK TABLES;

-- --
-- -- Table structure for table `title`
-- --

-- DROP TABLE IF EXISTS `title`;
-- /*!40101 SET @saved_cs_client     = @@character_set_client */;
-- /*!50503 SET character_set_client = utf8mb4 */;
-- CREATE TABLE `title` (
--   `TitleID` int NOT NULL,
--   `TName` varchar(20) NOT NULL,
--   `TRating` varchar(3) NOT NULL,
--   PRIMARY KEY (`TitleID`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
-- /*!40101 SET character_set_client = @saved_cs_client */;

-- --
-- -- Dumping data for table `title`
-- --

-- LOCK TABLES `title` WRITE;
-- /*!40000 ALTER TABLE `title` DISABLE KEYS */;
-- INSERT INTO `title` VALUES (1,'Karate Kid','PG'),(2,'Superman','12A'),(3,'Cool Runnings','U'),(4,'Happy Gilmore','12'),(5,'Iron Man','15');
-- /*!40000 ALTER TABLE `title` ENABLE KEYS */;
-- UNLOCK TABLES;
-- /*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

-- /*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
-- /*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
-- /*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
-- /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
-- /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
-- /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
-- /*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-08 22:34:08

-- 20 Minute Excercise DVD Rental 
-- - Return the first 5 Rentals, Including the FilmTitle and Persons name
-- - Find all the rentals that involve only people from Manchester
-- - Create a New Title called "Fast and Furious"
-- - Tim has made a new rental Today: It would be due next month-today, but he returned it early, a week later. He rented Fast and Furious. Update the database to reflect that.

-- select title.tname, rental.datetaken
-- from title
-- JOIN rental on rental.titleid = title.titleid; select title.tname, rental.datereturned
-- from title
-- JOIN rental on rental.titleid = title.titleid;

-- Done Task 1
-- select member.MFname, title.TName, rental.DateTaken
-- from member
-- join title
-- join rental
-- order by rental.RentalID desc limit 5;

-- Done Task 2
-- select member.MFname ,  member.MAddress, rental.DateTaken from member
-- join rental on member.MemberID = rental.MemberID 
-- where member.MAddress = 'Manchester';

-- Done Task 3
-- insert into title values(6,'Fast and Furious','16');

-- Done Task 4
-- insert into rental values(11,2,6,STR_TO_DATE('01-02-2023', '%d-%m-%Y'),STR_TO_DATE('01-03-2023', '%d-%m-%Y'),null);
select MFname, MemberID,rental.DateReturned,title.TName from member 
join rental on member.MemberID = rental.MemberID
join title
where member.MemberID = '2'
;
select * from rental;