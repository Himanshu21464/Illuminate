-- SQL Script to create Database Schema for Illuminate

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=1;
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
  Date_of_Birth DATE NOT NULL,
  Gender ENUM('Male', 'Female','Other') NOT NULL,
  Age INT NOT NULL DEFAULT 0,
  House_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(45) NOT NULL,
  State_ VARCHAR(45) NOT NULL,
  Country VARCHAR(45) NOT NULL,
  Pincode VARCHAR(18) NOT NULL,
  Employee_Role VARCHAR(50) NOT NULL,
  Date_of_Hiring DATE NOT NULL,
  Time_in_Company INT NOT NULL DEFAULT 0,
  PAN VARCHAR(15) NOT NULL,
  -- Blood_Group VARCHAR(20) NOT NULL,
  Blood_Group ENUM("A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"),
  Emergency_Contact_Number VARCHAR(20) NOT NULL,
  Emergency_Contact_Name VARCHAR(255) NOT NULL,
  Salary FLOAT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- KEY idx_actor_last_name (last_name)
  -- Constraints
  CONSTRAINT Check_Employee_Password_Length CHECK (LENGTH(Login_Password) >=6),
  CONSTRAINT Check_Emergency_Contact_Number CHECK (Emergency_Contact_Number >= 1100000000 AND Emergency_Contact_Number <= 9999999999),
  CONSTRAINT Check_Employee_Email CHECK (`Email` REGEXP "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$")
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Employee_Mobile_Numbers (
  Employee_ID VARCHAR(36),
  Mobile_Number BIGINT,
  PRIMARY KEY (Employee_ID, Mobile_Number),
  CONSTRAINT Check_Employee_Mobile_Number CHECK (Mobile_Number >= 1100000000 AND Mobile_Number <= 9999999999),
  FOREIGN KEY (Employee_ID) REFERENCES Employee (ID) ON DELETE CASCADE
  
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- UPDATE Employee
-- SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;

-- UPDATE Employee
-- SET Time_in_Company = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Hiring)), '%Y') + 0;
--
-- View table for Employee.
--

CREATE VIEW Employee_Details AS
SELECT e.ID, CONCAT(e.First_Name, ' ', COALESCE(e.Middle_Name, ''), ' ', e.Last_Name) AS Name, e.Email, e.Date_of_Birth, e.Gender, CONCAT(e.House_Number, ', ', e.Locality, ', ', e.City, ', ', e.State_, ', ', e.Country, ', ', e.Pincode) AS Address, e.Employee_Role, e.Date_of_Hiring, e.PAN, e.Blood_Group, e.Emergency_Contact_Number, e.Emergency_Contact_Name, e.Salary, e.Last_update, m.Mobile_Number
FROM Employee e
JOIN Employee_Mobile_Numbers m
ON e.ID = m.Employee_ID;


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
  Date_of_Birth DATE NOT NULL,
  Gender ENUM('Male', 'Female','Other') NOT NULL,
  Age INT NOT NULL DEFAULT 0,
  House_Number INT NOT NULL,
  Locality VARCHAR(40) NOT NULL,
  City VARCHAR(45) NOT NULL,
  State_ VARCHAR(45) NOT NULL,
  Country VARCHAR(45) NOT NULL,
  Pincode VARCHAR(18) NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT Check_Customer_Password_Length CHECK (LENGTH(Login_Password) >=6),
  CONSTRAINT Check_Customer_Email CHECK (`Email` REGEXP "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$")
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Customer_Mobile_Numbers (
  Customer_ID VARCHAR(36),
  Mobile_Number BIGINT,
  PRIMARY KEY (Mobile_Number),
  FOREIGN KEY (Customer_ID) REFERENCES Customer (ID) ON DELETE CASCADE,
  CONSTRAINT Check_Customer_Mobile_Number CHECK (Mobile_Number >= 1100000000 AND Mobile_Number <= 9999999999)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- UPDATE Customer
-- SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;
--
-- View for Customer_Details
--

CREATE VIEW Customer_Details AS
SELECT c.ID, CONCAT(c.First_Name, ' ', COALESCE(c.Middle_Name, ''), ' ', c.Last_Name) AS Name, c.Email, c.Date_of_Birth, c.Gender, CONCAT(c.House_Number, ', ', c.Locality, ', ', c.City, ', ', c.State_, ', ', c.Country, ', ', c.Pincode) AS Address, c.Last_update, m.Mobile_Number
FROM Customer c
JOIN Customer_Mobile_Numbers m
ON c.ID = m.Customer_ID;
 
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
  Mobile_Number BIGINT NOT NULL ,
  Company_Name VARCHAR(40) NOT NULL,
  Property_Number INT NOT NULL,
  Locality VARCHAR(20) NOT NULL,
  City VARCHAR(45) NOT NULL,
  State_ VARCHAR(45) NOT NULL,
  Country VARCHAR(45) NOT NULL,
  Pincode VARCHAR(18) NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT Check_Mobile_Number CHECK (Mobile_Number > 1100000000 AND Mobile_Number < 9999999999),
  CONSTRAINT Check_Seller_Password_Length CHECK (LENGTH(Login_Password) >=6),
  CONSTRAINT Check_Seller_Email CHECK (`Email` REGEXP "^[a-zA-Z0-9][a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]*?[a-zA-Z0-9._-]?@[a-zA-Z0-9][a-zA-Z0-9._-]*?[a-zA-Z0-9]?\\.[a-zA-Z]{2,63}$")
  -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- CREATE TABLE Seller_Mobile_Numbers (
--  Seller_ID VARCHAR(36),
--  Mobile_Number VARCHAR(20) UNIQUE,
--  PRIMARY KEY (Seller_ID, Mobile_Number),
--  CONSTRAINT Check_Seller_Mobile_Number CHECK (Mobile_Number like '^[7-9][0-9]{9}$'),
--  FOREIGN KEY (Seller_ID) REFERENCES Seller (ID) ON DELETE CASCADE
--  
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- View for Seller_Details
--

CREATE VIEW Seller_Details AS
SELECT s.ID, CONCAT(s.First_Name, ' ', COALESCE(s.Middle_Name, ''), ' ', s.Last_Name) AS Name_, s.Email, s.Company_Name, CONCAT(s.Property_Number, ', ', s.Locality, ', ', s.City, ', ', s.State_, ', ', s.Country, ', ', s.Pincode) AS Address_, s.Last_update
FROM Seller s;



--
-- Table structure for table `Product Category`
--

CREATE TABLE Category(
  ID VARCHAR(36) PRIMARY KEY,
  CategoryName VARCHAR(45) NOT NULL,
  CategoryDescription TINYTEXT NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;



--
-- Table structure for table `Brand`
--
CREATE TABLE Brand (
  ID VARCHAR(36) PRIMARY KEY,
  Brand_Name VARCHAR(50) NOT NULL,
  Brand_Description TINYTEXT NOT NULL,
  Brand_Logo TEXT(500) NOT NULL,
  Founder VARCHAR(100) NOT NULL,
  Country_Of_Origin VARCHAR(50) NOT NULL,
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Product`
--


CREATE TABLE Product (
  ID VARCHAR(36) PRIMARY KEY ,
  Product_Name VARCHAR(100) NOT NULL,
  Product_Description TINYTEXT NOT NULL,
  Product_Price FLOAT NOT NULL,
  Product_Quantity INT NOT NULL,
  Product_Images TINYTEXT NOT NULL,
  -- Product_Ingredients TINYTEXT NOT NULL,
  CATEGORY_ID VARCHAR(36),
  BRAND_ID VARCHAR(36),
  SELLER_ID VARCHAR(36),
  FOREIGN KEY (BRAND_ID) REFERENCES Brand(ID),
  FOREIGN KEY (CATEGORY_ID) REFERENCES Category(ID),
  FOREIGN KEY (SELLER_ID) REFERENCES Seller(ID),
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
  Comments TINYTEXT,
  Review_Date DATE NOT NULL,
  Product_ID VARCHAR(36),
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Product_ID) REFERENCES Product(ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
  
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;




--  TRIGGER-1 to update the review date;   ///   Working fine for Sample test cases.
DELIMITER $$

CREATE TRIGGER tr_review_insert
BEFORE INSERT ON Review
FOR EACH ROW
BEGIN
  SET NEW.Review_Date = CURDATE();
END$$

DELIMITER ;


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
  Tracking_ID VARCHAR(36) PRIMARY KEY,
  Courier_Name VARCHAR(100) NOT NULL,
  Tracking_URL VARCHAR(2040) NOT NULL,
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
  Customer_ID VARCHAR(36),
  FOREIGN KEY (Order_ID) REFERENCES Orders(ID),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(ID),
  Last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
 -- KEY idx_actor_last_name (last_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- TRIGGER-2 [Empty customer cart after placing order]   ///   Working fine for Sample test cases.

DELIMITER //
CREATE TRIGGER empty_cart AFTER INSERT ON Customer_Transaction
FOR EACH ROW
BEGIN
    IF NEW.Transaction_Status = 'Successful' THEN
        DELETE FROM Cart WHERE Customer_ID = NEW.Customer_ID;
    END IF;
END //
DELIMITER ;



-- TRIGGER-3 To Decrease the product stock after successful order by customer      /// Not working properly 
DELIMITER $$
CREATE TRIGGER decrease_product_quantity
AFTER INSERT ON Customer_Transaction
FOR EACH ROW
BEGIN
    IF NEW.Transaction_Status = 'Successful' THEN
        UPDATE Product
        SET Quantity = Quantity - (
            SELECT Quantity
            FROM Cart
            WHERE Customer_ID = NEW.Customer_ID
            AND Cart.ID = NEW.Order_ID
            AND Cart.Product_ID = Product.ID
        )
        WHERE EXISTS (
            SELECT 1
            FROM Cart
            WHERE Customer_ID = NEW.Customer_ID
            AND Cart.ID = NEW.Order_ID
            AND Cart.Product_ID = Product.ID
        );
    END IF;
END$$
DELIMITER ;




CREATE INDEX idx_Employee_First_name ON Employee (First_Name);
CREATE INDEX idx_Employee_Last_name ON Employee (Last_Name);
CREATE INDEX idx_Employee_Salary ON Employee (Salary);
-- CREATE INDEX idx_Employee_Age ON Employee (Age);
-- CREATE INDEX idx_Employee_Experience ON Employee (Time_in_Company);
CREATE INDEX idx_Employee_Blood ON Employee (Blood_Group);

CREATE INDEX idx_Customer_First_name ON Customer (First_Name);
CREATE INDEX idx_Customer_Last_name ON Customer (Last_Name);
-- CREATE INDEX idx_Customer_Age ON Customer (Age);

CREATE INDEX idx_Seller_First_name ON Customer (First_Name);
CREATE INDEX idx_Seller_Last_name ON Customer (Last_Name);

CREATE INDEX idx_Brand_Name ON Brand (Brand_Name);

CREATE INDEX idx_Courier_Name ON Courier (Courier_Name);

CREATE INDEX idx_Category_Name ON Category (CategoryName);

CREATE INDEX idx_Transaction_Date ON Customer_Transaction (Transaction_Date);

CREATE INDEX idx_Customer_Order_Date ON Orders (Order_Date);

CREATE INDEX idx_Order_Delivery_Date ON Orders (Delivery_Date);

CREATE INDEX idx_Order_Review_Rating ON Review (Review_Rating);


