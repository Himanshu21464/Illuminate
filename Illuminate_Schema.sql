-- SQL Script to create Database Schema for Illuminate

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS Illuminate;
CREATE SCHEMA Illuminate;
USE Illuminate;

--
-- Table structure for table `Employee`
--

CREATE TABLE Employee (
  Employee_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number INT NOT NULL UNIQUE,
  Date_Of_Birth DATE NOT NULL,
  Gender VARCHAR(6) CHECK (Gender = "Male" OR Gender = "Female" OR "Gender"),
  AGE INT NOT NULL,
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Employee_Role VARCHAR(30) NOT NULL,
  Date_of_Hiring DATE NOT NULL,
  Time_in_company INT,
  PAN VARCHAR(15) NOT NULL,
  Blood_Group VARCHAR(3),
  Emergency_Contact_Number INT NOT NULL,
  Emergency_Contact_Name VARCHAR(20) NOT NULL,
  Salary FLOAT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Employee_ID)
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Customer`
--

CREATE TABLE Customer (
  Customer_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number INT NOT NULL UNIQUE,
  Date_Of_Birth DATE NOT NULL,
  Gender VARCHAR(6) CHECK (Gender = "Male" OR Gender = "Female" OR "Gender"),
  AGE INT NOT NULL,
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Customer_ID)
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Seller`
--

CREATE TABLE Seller (
  Seller_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number INT NOT NULL UNIQUE,
  Company_Name VARCHAR(40) NOT NULL,
  Property_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
 
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Seller_ID)
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Product`
--

CREATE TABLE Product (
  Product_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Product_Name VARCHAR(45) NOT NULL,
  Product_Description VARCHAR(100) NOT NULL,
  Product_Price FLOAT NOT NULL,
  Product_Quantity INT NOT NULL,
  Product_Images VARCHAR(150) NOT NULL,
  Product_Ingredients VARCHAR(100) NOT NULL,
  
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Product_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Product Category`
--

CREATE TABLE Product_Category (
  Category_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Category_Name VARCHAR(45) NOT NULL,
  Category_Description VARCHAR(100) NOT NULL,
 
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Category_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Review`
--

CREATE TABLE Review (
  Review_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Review_Rating INT NOT NULL,
  Review_Title VARCHAR(100) NOT NULL,
  Comments VARCHAR(200),
  Review_Date DATE NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Review_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Brand`
--

CREATE TABLE Brand (
  Brand_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Brand_Name VARCHAR(50) NOT NULL,
  Brand_Description VARCHAR(200) NOT NULL,
  Brand_Logo VARCHAR(200) NOT NULL UNIQUE,
  Founder VARCHAR(50) NOT NULL,
  Country_Of_Origin VARCHAR(50) NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Brand_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Cart`
--

CREATE TABLE Cart (
  Cart_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Quantity INT NOT NULL,
  Total_Amount FLOAT NOT NULL,
  Discount FLOAT, 
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Cart_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Wishlist`
--

CREATE TABLE Wishlist (
  Wishlist_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Wishlist_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Order`
--

CREATE TABLE Customer_Orders (
  Order_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Order_Date DATE NOT NULL,
  Amount FLOAT NOT NULL,
  Order_Status VARCHAR(20) CHECK (Order_Status = "Delivered" OR Order_Status = "Under Process" ),
  Delivery_Date DATE NOT NULL,
  Delivery_Fee FLOAT NOT NULL,  
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Order_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Courier`
--

CREATE TABLE Courier (
  Tracking_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Courier_Name VARCHAR(50) NOT NULL,
  Tracking_URL VARCHAR(200) NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Tracking_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Transaction`
--

CREATE TABLE Customer_Transaction (
  Transaction_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Transaction_Date DATE NOT NULL,
  Amount FLOAT NOT NULL,
  Transaction_Status VARCHAR(20) CHECK (Transaction_Status = "Successful" OR Transaction_Status = "Pending" OR Transaction_Status = "Failed"),
  Payment_Offers VARCHAR(50),
  Payment_Method VARCHAR(30) CHECK (Payment_Method = "Credit/Debit Card" OR Payment_Method = "Netbanking" OR Payment_Method = "UPI" OR Payment_Method = "Cash On Delivery" OR Payment_Method = "Pay Later"), 
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Transaction_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


