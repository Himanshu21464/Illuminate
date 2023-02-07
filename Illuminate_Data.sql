

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

USE Illuminate;

--
-- Dumping data for table actor
--

SET AUTOCOMMIT=0;
INSERT INTO Employee (First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Date_Of_Birth, Gender, AGE, House_Number, Locality, City, State, Country, Pincode, Employee_Role, Date_of_Hiring, Time_in_company, PAN, Blood_Group, Emergency_Contact_Number, Emergency_Contact_Name, Salary)
VALUES 
('John', 'Doe', 'Smith', 'john.smith@email.com', 'password123', 1234567890, '1997-01-01', 'Male', 26, 123, 'XYZ', 'ABC', 'DEF', 'GHI', 123456, 'Manager', '2022-01-01', 2, 'ABC123456D', 'O+', 9876543210, 'Jane Doe', 50000),
('Jane', '', 'Doe', 'jane.doe@email.com', 'password456', 9876543210, '1998-02-02', 'Female', 25, 456, 'LMN', 'PQR', 'STU', 'JKL', 654321, 'Employee', '2021-12-31', 1, 'DEF654321E', 'A-', 1234567890, 'John Smith', 40000),
('Tom', 'J', 'Brown', 'tom.brown@email.com', 'password789', 1357986420, '1996-03-03', 'Male', 27, 789, 'RST', 'UVW', 'XYZ', 'MNO', 456789, 'Manager', '2021-01-01', 3, 'GHI456789G', 'B+', 9871234560, 'Jane Doe', 55000),
('Emma', '', 'Watson', 'emma.watson@email.com', 'password159', 9632587410, '1995-04-04', 'Female', 28, 159, 'OPQ', 'LKJ', 'FGH', 'IJK', 789123, 'Employee', '2022-02-02', 1, 'JKL789123J', 'AB-', 9638527410, 'Tom Brown', 45000),
('Harry', 'S', 'Potter', 'harry.potter@email.com', 'password753', 7531594820, '1994-05-05', 'Male', 29, 753, 'VBN', 'MNB', 'CDE', 'ABC', 159753, 'Manager', '2021-03-03', 2, 'MNO159753M', 'O-', 8521479638, 'Emma Watson', 60000),
('Megan', '', 'Fox', 'megan.fox@email.com', 'password369', 8521479638, '1993-06-06', 'Female', 30, 369, 'ZYX', 'WVU', 'TSR', 'RST', 951753, 'Employee', '2022-04-04', 1, 'PQR951753P', 'A+', 7531594820, 'Harry Potter', 50000);
COMMIT;


SET AUTOCOMMIT=0;
INSERT INTO Customer (First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Date_Of_Birth, Gender, AGE, House_Number, Locality, City, State, Country, Pincode)
VALUES
("John", "A", "Doe", "johndoe1@email.com", "password1", 1234567890, "1990-01-01", "Male", 33, 1234, "Some Locality", "Some City", "Some State", "Some Country", 123456),
("Jane", "B", "Doe", "janedoe1@email.com", "password2", 1234567891, "1991-02-01", "Female", 32, 1235, "Some Locality", "Some City", "Some State", "Some Country", 123457),
("Jim", "C", "Doe", "jimdoe1@email.com", "password3", 1234567892, "1992-03-01", "Male", 31, 1236, "Some Locality", "Some City", "Some State", "Some Country", 123458),
("Joan", "D", "Doe", "joandoe1@email.com", "password4", 1234567893, "1993-04-01", "Female", 30, 1237, "Some Locality", "Some City", "Some State", "Some Country", 123459),
("James", "E", "Doe", "jamesdoe1@email.com", "password5", 1234567894, "1994-05-01", "Male", 29, 1238, "Some Locality", "Some City", "Some State", "Some Country", 123460),
("Jessica", "F", "Doe", "jessicadoe1@email.com", "password6", 1234567895, "1995-06-01", "Female", 28, 1239, "Some Locality", "Some City", "Some State", "Some Country", 123461),
("Jack", "G", "Doe", "jackdoe1@email.com", "password7", 1234567896, "1996-07-01", "Male", 27, 1240, "Some Locality", "Some City", "Some State", "Some Country", 123462),
("Jill", "H", "Doe", "jilldoe1@email.com", "password8", 1234567897, "1997-08-01", "Female", 26, 1241, "Some Locality", "Some City", "Some State", "Some Country", 123463),
("Jeremy", "I", "Doe", "jeremydoe1@email.com", "password9", 1234567898, "1998-09-01", "Male", 25, 1242, "Some Locality", "Some City", "Some State", "Some Country", 123464),
("Julia", "J", "Doe", "juliadoe1@email.com", "password10", 1234567899, "1999-10-01", "Female", 24, 1243, "Some Locality", "Some City", "Some State", "Some Country", 123465);
COMMIT;

SET AUTOCOMMIT=0;
INSERT INTO Seller (First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Company_Name, Property_Number, Locality, City, State, Country, Pincode)
VALUES 
("John", "K", "Doe", "johndoe@beauty.com", "johndoe123", 1234567890, "Beauty Inc", 1001, "Central", "New York", "NY", "USA", 10001),
("Jane", "M", "Smith", "janesmith@beauty.com", "janesmith123", 1234567891, "Beauty Ltd", 1002, "West", "Los Angeles", "LA", "USA", 10002),
("Alex", "J", "Brown", "alexbrown@beauty.com", "alexbrown123", 1234567892, "Beauty Zone", 1003, "North", "Chicago", "IL", "USA", 10003),
("Mia", "R", "Johnson", "miajohnson@beauty.com", "miajohnson123", 1234567893, "Beauty World", 1004, "South", "Houston", "TX", "USA", 10004),
("Emma", "L", "Williams", "emmawilliams@beauty.com", "emmawilliams123", 1234567894, "Beauty House", 1005, "East", "Phoenix", "AZ", "USA", 10005);
COMMIT;


SET AUTOCOMMIT=0;
INSERT INTO Product (Product_Name, Product_Description, Product_Price, Product_Quantity, Product_Images, Product_Ingredients)
VALUES
("Matte Liquid Lipstick", "A long-lasting matte liquid lipstick that stays put for hours.", 9.99, 40, "https://www.example.com/matte_lipstick.jpg", "Liquid Lipstick Base, Pigments, Matte Powder"),
("Eyeliner Pen", "A precise and waterproof eyeliner pen for easy application.", 7.99, 50, "https://www.example.com/eyeliner_pen.jpg", "Eyeliner Ink, Waterproof Formula"),
("Blush Palette", "A blendable and buildable blush palette with 6 gorgeous shades.", 14.99, 30, "https://www.example.com/blush_palette.jpg", "Blush Powder, Pigments, Vitamin E"),
("Facial Cleanser", "A gentle and effective facial cleanser that removes impurities and leaves skin refreshed.", 11.99, 60, "https://www.example.com/facial_cleanser.jpg", "Water, Surfactant, Glycerin, Vitamin E, Essential Oils"),
("Shampoo and Conditioner Set", "A nourishing shampoo and conditioner set that helps repair damaged hair.", 19.99, 35, "https://www.example.com/shampoo_conditioner.jpg", "Water, Surfactant, Conditioning Agents, Essential Oils, Fragrance"),
("Foaming Hand Soap", "A luxurious foaming hand soap that leaves hands feeling clean and moisturized.", 6.99, 70, "https://www.example.com/foaming_hand_soap.jpg", "Water, Surfactant, Glycerin, Essential Oils, Fragrance"),
("Moisturizing Body Lotion", "A rich and nourishing body lotion that deeply moisturizes skin.", 14.99, 40, "https://www.example.com/body_lotion.jpg", "Water, Emulsifying Wax, Glycerin, Almond Oil, Vitamin E, Fragrance"),
("Bubble Bath", "A relaxing and rejuvenating bubble bath that soothes the skin and the senses.", 8.99, 50, "https://www.example.com/bubble_bath.jpg", "Water, Surfactant, Glycerin, Essential Oils, Fragrance"),
("Sugar Scrub", "A gentle and exfoliating sugar scrub that removes dead skin cells and leaves skin smooth and soft.", 12.99, 40, "https://www.example.com/sugar_scrub.jpg", "Sugar, Almond Oil, Vitamin E, Essential Oils"),
("Body Butter", "A rich and nourishing body butter that deeply moisturizes and soothes dry skin.", 16.99, 35, "https://www.example.com/body_butter.jpg", "Shea Butter, Coconut Oil, Almond Oil, Vitamin E, Essential Oils");
COMMIT;


SET AUTOCOMMIT=0;

COMMIT;


SET AUTOCOMMIT=0;

COMMIT;


SET AUTOCOMMIT=0;

COMMIT;


SET AUTOCOMMIT=0;

COMMIT;


SET AUTOCOMMIT=0;

COMMIT;


SET AUTOCOMMIT=0;

COMMIT;



SET AUTOCOMMIT=0;

COMMIT;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
