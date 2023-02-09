-- Handle Weak Entity


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
  ID VARCHAR(36) PRIMARY KEY,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number VARCHAR(550) NOT NULL ,
  Date_Of_Birth DATE NOT NULL,
  Gender ENUM("Male", "Female", "Other"),
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State_ VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Employee_Role VARCHAR(30) NOT NULL,
  Date_of_Hiring DATE NOT NULL,
  PAN VARCHAR(15) NOT NULL,
  Blood_Group ENUM("A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"),
  Emergency_Contact_Number BIGINT NOT NULL,
  Emergency_Contact_Name VARCHAR(20) NOT NULL,
  Salary FLOAT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- KEY idx_actor_last_name (last_name)
  -- Constraints
  CONSTRAINT Check_Mobile_Number CHECK (Mobile_Number like '^([7-9][0-9]{9},)*[7-9][0-9]{9}$'),
  CONSTRAINT Check_Email CHECK (Email like '^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9._-]*\\.[a-zA-Z]{2,4}$')
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Customer`
--

CREATE TABLE Customer (
  ID VARCHAR(36) PRIMARY KEY,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number VARCHAR(550) NOT NULL ,
  Date_Of_Birth DATE NOT NULL,
  Gender ENUM("Male", "Female", "Other"),
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State_ VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  CONSTRAINT Check_Mobile_Number CHECK (Mobile_Number like '^([7-9][0-9]{9},)*[7-9][0-9]{9}$'),
  CONSTRAINT Check_Email CHECK (Email like '^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9._-]*\\.[a-zA-Z]{2,4}$')
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Seller`
--

CREATE TABLE Seller (
  ID VARCHAR(36) PRIMARY KEY,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number VARCHAR(550) NOT NULL ,
  Company_Name VARCHAR(40) NOT NULL,
  Property_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State_ VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  CONSTRAINT Check_Mobile_Number CHECK (Mobile_Number like '^([7-9][0-9]{9},)*[7-9][0-9]{9}$'),
  CONSTRAINT Check_Email CHECK (Email like '^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9._-]*\\.[a-zA-Z]{2,4}$')
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Product`
--

CREATE TABLE Product (
  ID VARCHAR(36) PRIMARY KEY ,
  Product_Name VARCHAR(45) NOT NULL,
  Product_Description VARCHAR(100) NOT NULL,
  Product_Price FLOAT NOT NULL,
  Product_Quantity INT NOT NULL,
  Product_Images VARCHAR(150) NOT NULL,
  Product_Ingredients VARCHAR(100) NOT NULL,
  CATEGORY_ID VARCHAR(36),
  BRAND_ID VARCHAR(36),
  SELLER_ID VARCHAR(36),
  FOREIGN KEY (BRAND_ID) REFERENCES BRAND(ID),
  FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORY(ID),
  FOREIGN KEY (SELLER_ID) REFERENCES SELLER(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Product Category`
--

CREATE TABLE Category(
  ID VARCHAR(36) PRIMARY KEY,
  CategoryName VARCHAR(45) NOT NULL,
  CategoryDescription VARCHAR(100) NOT NULL,
 
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Review`
--

CREATE TABLE Review (
  ID VARCHAR(36) PRIMARY KEY,
  Review_Rating INT NOT NULL,
  Review_Title VARCHAR(100) NOT NULL,
  Comments VARCHAR(200),
  Review_Date DATE NOT NULL,
  Product_ID VARCHAR(36),
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Product_ID) REFERENCES Product(ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
  -- @TODO: Constraint for rating
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Brand`
--

CREATE TABLE Brand (
  ID VARCHAR(36) PRIMARY KEY,
  Brand_Name VARCHAR(50) NOT NULL,
  Brand_Description VARCHAR(200) NOT NULL,
  Brand_Logo VARCHAR(200) NOT NULL UNIQUE,
  Founder VARCHAR(50) NOT NULL,
  Country_Of_Origin VARCHAR(50) NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Cart`
--

CREATE TABLE Cart (
  ID VARCHAR(36) PRIMARY KEY,
  Quantity INT NOT NULL,
  Discount FLOAT,
  Product_ID VARCHAR(36),
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Product_ID) REFERENCES Product(ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Wishlist`
--

CREATE TABLE Wishlist (
  ID VARCHAR(36) PRIMARY KEY,
  Product_ID VARCHAR(36),
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Product_ID) REFERENCES Product(ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Order`
--

CREATE TABLE Orders (
  ID VARCHAR(36) PRIMARY KEY,
  Order_Date DATE NOT NULL,
  Amount FLOAT NOT NULL,
  Order_Status ENUM("Delivered","Under Process"),
  Delivery_Date DATE NOT NULL,
  Delivery_Fee FLOAT NOT NULL,  
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Courier`
--

CREATE TABLE Courier (
  Tracking_ID INT UNSIGNED NOT NULL UNIQUE,
  Courier_Name VARCHAR(50) NOT NULL,
  Tracking_URL VARCHAR(200) NOT NULL,
  Order_ID VARCHAR(36),
  FOREIGN KEY (Order_ID) REFERENCES Orders(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `Transaction`
--

CREATE TABLE Customer_Transaction (
  ID VARCHAR(36) PRIMARY KEY,
  Transaction_Date DATE NOT NULL,
  Amount FLOAT NOT NULL,
  Transaction_Status ENUM ("Successful", "Pending", "Failed"),
  Payment_Method ENUM ("Credit/Debit Card", "Netbanking", "UPI", "Cash On Delivery", "Pay Later"), 
  Order_ID VARCHAR(36),
  FOREIGN KEY (Order_ID) REFERENCES Orders(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


