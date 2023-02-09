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
  Employee_ID INT NOT NULL AUTO_INCREMENT,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Date_of_Birth DATE NOT NULL,
  Gender ENUM('Male', 'Female','Other') NOT NULL,
  Age INT NOT NULL DEFAULT 0,
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Employee_Role VARCHAR(30) NOT NULL,
  Date_of_Hiring DATE NOT NULL,
  Time_in_Company INT NOT NULL DEFAULT 0,
  PAN VARCHAR(15) NOT NULL UNIQUE,
  Blood_Group ENUM("A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"),
  Emergency_Contact_Number BIGINT NOT NULL,
  Emergency_Contact_Name VARCHAR(20) NOT NULL,
  Salary FLOAT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- CONSTRAINT Check_Employee_Email CHECK (Email like '^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9._-]*\\.[a-zA-Z]{2,4}$'),
  PRIMARY KEY  (Employee_ID)
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Employee_Mobile_Numbers (
  Employee_ID INT,
  Mobile_Number VARCHAR(20) UNIQUE,
  PRIMARY KEY (Employee_ID, Mobile_Number),
  CONSTRAINT Check_Employee_Mobile_Number CHECK (Mobile_Number like '^([7-9][0-9]{9},)*[7-9][0-9]{9}$'),
  FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID) ON DELETE CASCADE
  
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

UPDATE Employee
SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;

UPDATE Employee
SET Time_in_Company = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Hiring)), '%Y') + 0;
--
-- View table for Employee.
--

CREATE VIEW Employee_Details AS
SELECT e.Employee_ID, CONCAT(e.First_Name, ' ', COALESCE(e.Middle_Name, ''), ' ', e.Last_Name) AS Name, e.Email, e.Date_of_Birth, e.Gender, e.Age, CONCAT(e.House_Number, ', ', e.Locality, ', ', e.City, ', ', e.State, ', ', e.Country, ', ', e.Pincode) AS Address, e.Employee_Role, e.Date_of_Hiring,e.Time_in_Company, e.PAN, e.Blood_Group, e.Emergency_Contact_Number, e.Emergency_Contact_Name, e.Salary, e.Last_update, m.Mobile_Number
FROM Employee e
JOIN Employee_Mobile_Numbers m
ON e.Employee_ID = m.Employee_ID;


--
-- Table structure for table `Customer`
--

CREATE TABLE Customer (
  Customer_ID VARCHAR(36),
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Date_of_Birth DATE NOT NULL,
  Gender ENUM('Male', 'Female','Other') NOT NULL,
  Age INT NOT NULL DEFAULT 0,
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Customer_ID)
  -- CONSTRAINT Check_Customer_Email CHECK (Email like '^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9._-]*\\.[a-zA-Z]{2,4}$')
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Customer_Mobile_Numbers (
  Customer_ID VARCHAR(36),
  Mobile_Number VARCHAR(20) UNIQUE,
  PRIMARY KEY (Customer_ID, Mobile_Number),
  FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID) ON DELETE CASCADE,
  CONSTRAINT Check_Customer_Mobile_Number CHECK (Mobile_Number like '^([7-9][0-9]{9},)*[7-9][0-9]{9}$')
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


UPDATE Customer
SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;
--
-- View for Customer_Details
--

CREATE VIEW Customer_Details AS
SELECT c.Customer_ID, CONCAT(c.First_Name, ' ', COALESCE(c.Middle_Name, ''), ' ', c.Last_Name) AS Name, c.Email, c.Date_of_Birth, c.Gender, c.Age, CONCAT(c.House_Number, ', ', c.Locality, ', ', c.City, ', ', c.State, ', ', c.Country, ', ', c.Pincode) AS Address, c.Last_update, m.Mobile_Number
FROM Customer c
JOIN Customer_Mobile_Numbers m
ON c.Customer_ID = c.Customer_ID;
 
--
-- Table structure for table `Seller`
--

CREATE TABLE Seller (
  Seller_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
  First_Name VARCHAR(45) NOT NULL,
  Middle_Name VARCHAR(45),
  Last_Name VARCHAR(45) NOT NULL,
  Email VARCHAR(45) UNIQUE,
  Login_Password VARCHAR(20) NOT NULL,
  Mobile_Number VARCHAR(20) UNIQUE NOT NULL,
  Company_Name VARCHAR(40) NOT NULL,
  Property_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(15) NOT NULL,
  State VARCHAR(15) NOT NULL,
  Country VARCHAR(15) NOT NULL,
  Pincode INT NOT NULL,
 
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Seller_ID),
  CONSTRAINT Check_Seller_Mobile_Number CHECK (Mobile_Number like '^([7-9][0-9]{9},)*[7-9][0-9]{9}$')
  -- CONSTRAINT Check_Seller_Email CHECK (Email like '^[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9][a-zA-Z0-9._-]*\\.[a-zA-Z]{2,4}$')
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- View for Seller_Details
--

CREATE VIEW Seller_Details AS
SELECT s.Seller_ID, CONCAT(s.First_Name, ' ', COALESCE(s.Middle_Name, ''), ' ', s.Last_Name) AS Name, s.Email, s.Company_Name, CONCAT(s.Property_Number, ', ', s.Locality, ', ', s.City, ', ', s.State, ', ', s.Country, ', ', s.Pincode) AS Address, s.Last_update
FROM Seller s;


--
-- Table structure for table `Product`
--

CREATE TABLE Product (
  Product_ID VARCHAR(36) PRIMARY KEY ,
  Product_Name VARCHAR(45) NOT NULL,
  Product_Description VARCHAR(100) NOT NULL,
  Product_Price FLOAT NOT NULL,
  Product_Quantity INT NOT NULL,
  Product_Images VARCHAR(150) NOT NULL,
  Product_Ingredients VARCHAR(100) NOT NULL,
  CATEGORY_ID VARCHAR(36),
  BRAND_ID VARCHAR(36),
  SELLER_ID VARCHAR(36),
  FOREIGN KEY (BRAND_ID) REFERENCES BRAND(Brand_ID),
  FOREIGN KEY (CATEGORY_ID) REFERENCES CATEGORY(Category_ID),
  FOREIGN KEY (SELLER_ID) REFERENCES SELLER(Seller_ID),
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
  FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
  -- @TODO: Constraint for rating
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DELIMITER $$

CREATE TRIGGER tr_review_insert
BEFORE INSERT ON Review
FOR EACH ROW
BEGIN
  SET NEW.Review_Date = CURDATE();
END$$

DELIMITER ;


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
  Product_ID VARCHAR(36),
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
  
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Cart_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Wishlist`
--

CREATE TABLE Wishlist (
  Wishlist_ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  Product_ID VARCHAR(36),
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
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
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
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
  Order_ID VARCHAR(36),
  FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
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
  Transaction_Status ENUM ("Successful", "Pending", "Failed") NOT NULL,
  Payment_Method ENUM ("Credit/Debit Card", "Netbanking", "UPI", "Cash On Delivery", "Pay Later") NOT NULL, 
  Order_ID VARCHAR(36),
  FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY  (Transaction_ID)
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE INDEX idx_Employee_First_name ON Employee (First_Name);
CREATE INDEX idx_Employee_Last_name ON Employee (Last_Name);
CREATE INDEX idx_Employee_Salary ON Employee (Salary);
CREATE INDEX idx_Employee_Age ON Employee (Age);
CREATE INDEX idx_Employee_Experience ON Employee (Time_in_Company);
CREATE INDEX idx_Employee_Blood ON Employee (Blood_Group);

CREATE INDEX idx_Customer_First_name ON Customer (First_Name);
CREATE INDEX idx_Customer_Last_name ON Customer (Last_Name);
CREATE INDEX idx_Customer_Age ON Customer (Age);

CREATE INDEX idx_Seller_First_name ON Customer (First_Name);
CREATE INDEX idx_Seller_Last_name ON Customer (Last_Name);

CREATE INDEX idx_Brand_Name ON Brand (Brand_Name);

CREATE INDEX idx_Courier_Name ON Courier (Courier_Name);

CREATE INDEX idx_Category_Name ON Category (CategoryName);

CREATE INDEX idx_Transaction_Date ON Customer_Transaction (Transaction_Date);

CREATE INDEX idx_Customer_Order_Date ON Customer_Orders (Order_Date);

CREATE INDEX idx_Order_Delivery_Date ON Customer_Orders (Delivery_Date);

CREATE INDEX idx_Order_Review_Rating ON Review (Review_Rating);






