USE Illuminate;

-- Customers

insert into Customer ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, House_Number, Locality, City, State_, Country, Pincode) values ( 'Kyrstin', 'Sidnee', 'Lusted', 'slusted0@wix.com', 'VOcjPj054', '1996-09-18', 'Male', 9729, 'Doe Crossing', 'Kungsbacka', 'Halland', 'Sweden', '434 43');

insert into Customer_Mobile_Numbers (Customer_ID, Mobile_Number) values ( 1, 9357925749);
insert into Customer_Mobile_Numbers (Customer_ID, Mobile_Number) values ( 1, 4618992068);

-- Brand

insert into Brand ( Brand_Name, Brand_Description, Brand_Logo, Founder, Country_Of_Origin) values ( 'Tatcha', 'Luxury skincare inspired by Japanese beauty rituals', 'http://mapy.cz/nulla.json', 'Isaac Trevarthen', 'Indonesia');
insert into Brand ( Brand_Name, Brand_Description, Brand_Logo, Founder, Country_Of_Origin) values ( 'The Ordinary', 'Clinical formulations with integrity', 'https://blogger.com/lectus/vestibulum/quam.png', 'Harlen Fiddeman', 'Serbia');

-- Category

insert into Category ( CategoryName, CategoryDescription) values ( 'Makeup', 'Cosmetics for enhancing beauty');
insert into Category ( CategoryName, CategoryDescription) values ( 'Skincare', 'skincare for keeping skin healthy and youthful');


-- Seller

insert into Seller ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Company_Name, Property_Number, Locality, City, State_, Country, Pincode) values ( 'Ulberto', 'Alyss', 'Ibbotson', 'aibbotson0@phpbb.com', '0jekEUQ', 3157982690, 'Gusikowski and Sons', 5901, 'Tony', 'Ifanes', 'Bragança', 'Portugal', '5210-105');
insert into Seller ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Company_Name, Property_Number, Locality, City, State_, Country, Pincode) values ( 'Sid', 'Cass', 'Grigoroni', 'cgrigoroni1@posterous.com', 'xTQt3g', 3160468333, 'Schowalter-Hand', 7298, 'Sullivan', 'Augusta', 'Georgia', 'United States', '30905');


-- Products

insert into Product (Product_Name, Product_Description, Product_Price, Product_Quantity, Product_Images, CATEGORY_ID, BRAND_ID, SELLER_ID) values ('L''Oreal Paris Voluminous Lash Paradise Mascara', 'volumizing mascara for intense length and volume', 76671.79, 4142, 'http://tumblr.com/pede/justo/eu.xml', 1, 1, 1);
insert into Product (Product_Name, Product_Description, Product_Price, Product_Quantity, Product_Images, CATEGORY_ID, BRAND_ID, SELLER_ID) values ('Maybelline SuperStay Matte Ink Liquid Lipstick', 'long wear matte lipstick with vibrant color', 77981.51, 7553, 'http://google.com.au/varius.jsp', 1, 1, 1);

-- Cart

insert into Cart (Quantity, Discount, Product_ID, Customer_ID) values (126, 51.8, 1, 1);

insert into Orders (Order_Date, Amount, Order_Status, Delivery_Date, Delivery_Fee, Customer_ID) values ('2022-12-26', 788673.65, 'Under Process', '2022-02-22', 67.28, 1);

-- Review

insert into Review ( Review_Rating, Review_Title, Comments, Review_Date, Product_ID, Customer_ID) values ( 5, 'Amazing product!', 'This product has exceeded my expectations. It made my skin feel so smooth and soft. Highly recommended!', '2022-10-23', 1, 1);

-- Transaction
insert into Customer_Transaction (Transaction_Date, Amount, Transaction_Status, Payment_Method, Order_ID, Customer_ID) values ('1953-09-27', 52.88, 'Successful', 'Credit/Debit Card', 1, 1);




select Product_Quantity from Product where ID=1;
select Review_Date from Review where ID=1;
select * from Cart;