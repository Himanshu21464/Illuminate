CREATE DATABASE  IF NOT EXISTS `Illuminate` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Illuminate`;
-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: Illuminate
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.10.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Brand`
--

DROP TABLE IF EXISTS `Brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Brand` (
  `ID` varchar(36) NOT NULL,
  `Brand_Name` varchar(50) NOT NULL,
  `Brand_Description` varchar(255) NOT NULL,
  `Brand_Logo` varchar(200) NOT NULL,
  `Founder` varchar(50) NOT NULL,
  `Country_Of_Origin` varchar(50) NOT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Brand_Logo` (`Brand_Logo`),
  KEY `idx_Brand_Name` (`Brand_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cart` (
  `ID` varchar(36) NOT NULL,
  `Quantity` int NOT NULL,
  `Discount` float DEFAULT NULL,
  `Product_ID` varchar(36) DEFAULT NULL,
  `Customer_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Product_ID` (`Product_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`ID`),
  CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Category`
--

DROP TABLE IF EXISTS `Category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Category` (
  `ID` varchar(36) NOT NULL,
  `CategoryName` varchar(45) NOT NULL,
  `CategoryDescription` varchar(255) NOT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `idx_Category_Name` (`CategoryName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Courier`
--

DROP TABLE IF EXISTS `Courier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Courier` (
  `Tracking_ID` varchar(36) NOT NULL,
  `Courier_Name` varchar(50) NOT NULL,
  `Tracking_URL` varchar(255) NOT NULL,
  `Order_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Tracking_ID`),
  KEY `Order_ID` (`Order_ID`),
  KEY `idx_Courier_Name` (`Courier_Name`),
  CONSTRAINT `Courier_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `ID` varchar(36) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Middle_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Login_Password` varchar(20) NOT NULL,
  `Date_of_Birth` date NOT NULL,
  `Gender` enum('Male','Female','Other') NOT NULL,
  `Age` int NOT NULL DEFAULT '0',
  `House_Number` int NOT NULL,
  `Locality` varchar(40) NOT NULL,
  `City` varchar(45) NOT NULL,
  `State_` varchar(45) NOT NULL,
  `Country` varchar(45) NOT NULL,
  `Pincode` varchar(18) NOT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `idx_Customer_First_name` (`First_Name`),
  KEY `idx_Customer_Last_name` (`Last_Name`),
  KEY `idx_Seller_First_name` (`First_Name`),
  KEY `idx_Seller_Last_name` (`Last_Name`),
  CONSTRAINT `Check_Customer_Email` CHECK (regexp_like(`Email`,_utf8mb3'^[a-zA-Z0-9][a-zA-Z0-9.!#$%&\'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `Customer_Details`
--

DROP TABLE IF EXISTS `Customer_Details`;
/*!50001 DROP VIEW IF EXISTS `Customer_Details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Customer_Details` AS SELECT 
 1 AS `ID`,
 1 AS `Name`,
 1 AS `Email`,
 1 AS `Date_of_Birth`,
 1 AS `Gender`,
 1 AS `Address`,
 1 AS `Last_update`,
 1 AS `Mobile_Number`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Customer_Mobile_Numbers`
--

DROP TABLE IF EXISTS `Customer_Mobile_Numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Mobile_Numbers` (
  `Customer_ID` varchar(36) NOT NULL,
  `Mobile_Number` bigint NOT NULL,
  PRIMARY KEY (`Customer_ID`,`Mobile_Number`),
  UNIQUE KEY `Mobile_Number` (`Mobile_Number`),
  CONSTRAINT `Customer_Mobile_Numbers_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `Check_Customer_Mobile_Number` CHECK (((`Mobile_Number` >= 1100000000) and (`Mobile_Number` <= 9999999999)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Customer_Transaction`
--

DROP TABLE IF EXISTS `Customer_Transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer_Transaction` (
  `ID` varchar(36) NOT NULL,
  `Transaction_Date` date NOT NULL,
  `Amount` float NOT NULL,
  `Transaction_Status` enum('Successful','Pending','Failed') DEFAULT NULL,
  `Payment_Method` enum('Credit/Debit Card','Netbanking','UPI','Cash On Delivery','Pay Later') DEFAULT NULL,
  `Order_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Order_ID` (`Order_ID`),
  KEY `idx_Transaction_Date` (`Transaction_Date`),
  CONSTRAINT `Customer_Transaction_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `Orders` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `ID` varchar(36) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Middle_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Login_Password` varchar(20) NOT NULL,
  `Date_of_Birth` date NOT NULL,
  `Gender` enum('Male','Female','Other') NOT NULL,
  `Age` int NOT NULL DEFAULT '0',
  `House_Number` int NOT NULL,
  `Locality` varchar(20) NOT NULL,
  `City` varchar(45) NOT NULL,
  `State_` varchar(45) NOT NULL,
  `Country` varchar(45) NOT NULL,
  `Pincode` varchar(18) NOT NULL,
  `Employee_Role` varchar(50) NOT NULL,
  `Date_of_Hiring` date NOT NULL,
  `Time_in_Company` int NOT NULL DEFAULT '0',
  `PAN` varchar(15) NOT NULL,
  `Blood_Group` enum('A+','B+','O+','AB+','A-','B-','O-','AB-') DEFAULT NULL,
  `Emergency_Contact_Number` bigint NOT NULL,
  `Emergency_Contact_Name` varchar(255) NOT NULL,
  `Salary` float NOT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `idx_Employee_First_name` (`First_Name`),
  KEY `idx_Employee_Last_name` (`Last_Name`),
  KEY `idx_Employee_Salary` (`Salary`),
  KEY `idx_Employee_Blood` (`Blood_Group`),
  CONSTRAINT `Check_Emergency_Contact_Number` CHECK (((`Emergency_Contact_Number` >= 1100000000) and (`Emergency_Contact_Number` <= 9999999999))),
  CONSTRAINT `Check_Employee_Email` CHECK (regexp_like(`Email`,_utf8mb3'^[a-zA-Z0-9][a-zA-Z0-9.!#$%&\'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `Employee_Details`
--

DROP TABLE IF EXISTS `Employee_Details`;
/*!50001 DROP VIEW IF EXISTS `Employee_Details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Employee_Details` AS SELECT 
 1 AS `ID`,
 1 AS `Name`,
 1 AS `Email`,
 1 AS `Date_of_Birth`,
 1 AS `Gender`,
 1 AS `Address`,
 1 AS `Employee_Role`,
 1 AS `Date_of_Hiring`,
 1 AS `PAN`,
 1 AS `Blood_Group`,
 1 AS `Emergency_Contact_Number`,
 1 AS `Emergency_Contact_Name`,
 1 AS `Salary`,
 1 AS `Last_update`,
 1 AS `Mobile_Number`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Employee_Mobile_Numbers`
--

DROP TABLE IF EXISTS `Employee_Mobile_Numbers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Mobile_Numbers` (
  `Employee_ID` varchar(36) NOT NULL,
  `Mobile_Number` bigint NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Mobile_Number`),
  UNIQUE KEY `Mobile_Number` (`Mobile_Number`),
  CONSTRAINT `Employee_Mobile_Numbers_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`ID`) ON DELETE CASCADE,
  CONSTRAINT `Check_Employee_Mobile_Number` CHECK (((`Mobile_Number` >= 1100000000) and (`Mobile_Number` <= 9999999999)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `ID` varchar(36) NOT NULL,
  `Order_Date` date NOT NULL,
  `Amount` float NOT NULL,
  `Order_Status` enum('Delivered','Under Process') DEFAULT NULL,
  `Delivery_Date` date NOT NULL,
  `Delivery_Fee` float NOT NULL,
  `Customer_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `idx_Customer_Order_Date` (`Order_Date`),
  KEY `idx_Order_Delivery_Date` (`Delivery_Date`),
  CONSTRAINT `Orders_ibfk_1` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Product` (
  `ID` varchar(36) NOT NULL,
  `Product_Name` varchar(100) NOT NULL,
  `Product_Description` varchar(255) NOT NULL,
  `Product_Price` float NOT NULL,
  `Product_Quantity` int NOT NULL,
  `Product_Images` varchar(150) NOT NULL,
  `Product_Ingredients` varchar(200) NOT NULL,
  `CATEGORY_ID` varchar(36) DEFAULT NULL,
  `BRAND_ID` varchar(36) DEFAULT NULL,
  `SELLER_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `BRAND_ID` (`BRAND_ID`),
  KEY `CATEGORY_ID` (`CATEGORY_ID`),
  KEY `SELLER_ID` (`SELLER_ID`),
  CONSTRAINT `Product_ibfk_1` FOREIGN KEY (`BRAND_ID`) REFERENCES `BRAND` (`ID`),
  CONSTRAINT `Product_ibfk_2` FOREIGN KEY (`CATEGORY_ID`) REFERENCES `CATEGORY` (`ID`),
  CONSTRAINT `Product_ibfk_3` FOREIGN KEY (`SELLER_ID`) REFERENCES `SELLER` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Review` (
  `ID` varchar(36) NOT NULL,
  `Review_Rating` int NOT NULL,
  `Review_Title` varchar(100) NOT NULL,
  `Comments` varchar(255) DEFAULT NULL,
  `Review_Date` date NOT NULL,
  `Product_ID` varchar(36) DEFAULT NULL,
  `Customer_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Product_ID` (`Product_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  KEY `idx_Order_Review_Rating` (`Review_Rating`),
  CONSTRAINT `Review_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`ID`),
  CONSTRAINT `Review_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,TRADITIONAL,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_review_insert` BEFORE INSERT ON `Review` FOR EACH ROW BEGIN
  SET NEW.Review_Date = CURDATE();
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `Seller`
--

DROP TABLE IF EXISTS `Seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Seller` (
  `ID` varchar(36) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Middle_Name` varchar(45) DEFAULT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Login_Password` varchar(20) NOT NULL,
  `Mobile_Number` bigint NOT NULL,
  `Company_Name` varchar(40) NOT NULL,
  `Property_Number` int NOT NULL,
  `Locality` varchar(20) NOT NULL,
  `City` varchar(45) NOT NULL,
  `State_` varchar(45) NOT NULL,
  `Country` varchar(45) NOT NULL,
  `Pincode` varchar(18) NOT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Email` (`Email`),
  CONSTRAINT `Check_Mobile_Number` CHECK (((`Mobile_Number` >= 1100000000) and (`Mobile_Number` <= 9999999999))),
  CONSTRAINT `Check_Seller_Email` CHECK (regexp_like(`Email`,_utf8mb4'^[a-zA-Z0-9][a-zA-Z0-9.!#$%&\'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `Seller_Details`
--

DROP TABLE IF EXISTS `Seller_Details`;
/*!50001 DROP VIEW IF EXISTS `Seller_Details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Seller_Details` AS SELECT 
 1 AS `ID`,
 1 AS `Name_`,
 1 AS `Email`,
 1 AS `Company_Name`,
 1 AS `Address_`,
 1 AS `Last_update`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Wishlist`
--

DROP TABLE IF EXISTS `Wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Wishlist` (
  `ID` varchar(36) NOT NULL,
  `Product_ID` varchar(36) DEFAULT NULL,
  `Customer_ID` varchar(36) DEFAULT NULL,
  `Last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  KEY `Product_ID` (`Product_ID`),
  KEY `Customer_ID` (`Customer_ID`),
  CONSTRAINT `Wishlist_ibfk_1` FOREIGN KEY (`Product_ID`) REFERENCES `Product` (`ID`),
  CONSTRAINT `Wishlist_ibfk_2` FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'Illuminate'
--

--
-- Dumping routines for database 'Illuminate'
--

--
-- Final view structure for view `Customer_Details`
--

/*!50001 DROP VIEW IF EXISTS `Customer_Details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `Customer_Details` AS select `c`.`ID` AS `ID`,concat(`c`.`First_Name`,' ',coalesce(`c`.`Middle_Name`,''),' ',`c`.`Last_Name`) AS `Name`,`c`.`Email` AS `Email`,`c`.`Date_of_Birth` AS `Date_of_Birth`,`c`.`Gender` AS `Gender`,concat(`c`.`House_Number`,', ',`c`.`Locality`,', ',`c`.`City`,', ',`c`.`State_`,', ',`c`.`Country`,', ',`c`.`Pincode`) AS `Address`,`c`.`Last_update` AS `Last_update`,`m`.`Mobile_Number` AS `Mobile_Number` from (`Customer` `c` join `Customer_Mobile_Numbers` `m` on((`c`.`ID` = `m`.`Customer_ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `Employee_Details`
--

/*!50001 DROP VIEW IF EXISTS `Employee_Details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `Employee_Details` AS select `e`.`ID` AS `ID`,concat(`e`.`First_Name`,' ',coalesce(`e`.`Middle_Name`,''),' ',`e`.`Last_Name`) AS `Name`,`e`.`Email` AS `Email`,`e`.`Date_of_Birth` AS `Date_of_Birth`,`e`.`Gender` AS `Gender`,concat(`e`.`House_Number`,', ',`e`.`Locality`,', ',`e`.`City`,', ',`e`.`State_`,', ',`e`.`Country`,', ',`e`.`Pincode`) AS `Address`,`e`.`Employee_Role` AS `Employee_Role`,`e`.`Date_of_Hiring` AS `Date_of_Hiring`,`e`.`PAN` AS `PAN`,`e`.`Blood_Group` AS `Blood_Group`,`e`.`Emergency_Contact_Number` AS `Emergency_Contact_Number`,`e`.`Emergency_Contact_Name` AS `Emergency_Contact_Name`,`e`.`Salary` AS `Salary`,`e`.`Last_update` AS `Last_update`,`m`.`Mobile_Number` AS `Mobile_Number` from (`Employee` `e` join `Employee_Mobile_Numbers` `m` on((`e`.`ID` = `m`.`Employee_ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `Seller_Details`
--

/*!50001 DROP VIEW IF EXISTS `Seller_Details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `Seller_Details` AS select `s`.`ID` AS `ID`,concat(`s`.`First_Name`,' ',coalesce(`s`.`Middle_Name`,''),' ',`s`.`Last_Name`) AS `Name_`,`s`.`Email` AS `Email`,`s`.`Company_Name` AS `Company_Name`,concat(`s`.`Property_Number`,', ',`s`.`Locality`,', ',`s`.`City`,', ',`s`.`State_`,', ',`s`.`Country`,', ',`s`.`Pincode`) AS `Address_`,`s`.`Last_update` AS `Last_update` from `Seller` `s` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-10 22:19:49
