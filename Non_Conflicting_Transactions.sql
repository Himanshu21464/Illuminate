-- Transaction 1: Transfer employee to a new department
START TRANSACTION;

-- Get the current department of the employee
SELECT Employee_Role FROM Employee WHERE ID = 1 FOR UPDATE;

-- Update the employee's department to the new department
UPDATE Employee SET Employee_Role = 'Inventory manager' WHERE ID = 1;

COMMIT;



-- Transaction 2: Add a new customer and mobile number
START TRANSACTION;

-- Insert the new customer
INSERT INTO Customer (Membership, First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, House_Number, Locality, City, State_, Country, Pincode) 
VALUES ('Elite','John', NULL, 'Doe', 'johndoe@example.com', 'password123', '1980-01-01', 'Male', 123, 'Main Street', 'New York', 'NY', 'USA', '12345');

-- Get the ID of the new customer
SELECT LAST_INSERT_ID() INTO @CustomerID;

-- Insert the new mobile number for the customer
INSERT INTO Customer_Mobile_Numbers (Customer_ID, Mobile_Number) VALUES (@CustomerID, 9234567890);

COMMIT;



-- Transaction 3: Remove an employee's mobile number
START TRANSACTION;

-- Get the employee's mobile number
SELECT Mobile_Number FROM Employee_Mobile_Numbers WHERE Employee_ID = 1 FOR UPDATE;

-- Remove the mobile number from the employee's record
DELETE FROM Employee_Mobile_Numbers WHERE Employee_ID = 1;


COMMIT;




-- Transaction 4: Calculate employee bonus based on performance


START TRANSACTION;

SET SQL_SAFE_UPDATES = 0;

SELECT AVG(Salary) FROM Employee WHERE Employee_Role = 'Brand manager' FOR UPDATE;

UPDATE Employee SET Salary = Salary + 500 WHERE Employee_Role = 'Brand manager';

COMMIT;






-- Transaction 5: to change Membership of customer and deducting the amount from wallet
START TRANSACTION;
-- Get Customer's wallet balance where ID =10
SELECT Wallet INTO @wallet_balance FROM Customer WHERE ID = 10 FOR UPDATE;

-- set the new membership and deduct the amount from wallet
UPDATE Customer SET Wallet = Wallet - 200, Membership = 'Elite' WHERE ID = 10;

COMMIT;

