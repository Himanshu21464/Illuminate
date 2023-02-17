-- SET SQL_SAFE_UPDATES = 0;

-- Query 1 : Counting number of brands on website
SELECT COUNT(*) FROM Brand;

-- Query 2: Updating quantity of a product on website and adding a constraint to make sure its positive
UPDATE Product
SET Product_Quantity = 100
WHERE ID = 'acc3bdc8-a9b7-4f5e-949a-2589bfd062fb';
ALTER TABLE Product ADD CONSTRAINT Stock CHECK (Product_Quantity >= 0);

-- Query 3 : Fetch avg ratings of a product

SELECT AVG(Review_Rating) FROM Review WHERE Product_ID = 'ae298b50-bf90-4766-b75e-6ad7a54cf02e';

-- Query 4 : Filter feature for sorting, price highest to lowest

SELECT * FROM Product
WHERE Product_Price > 1000
ORDER BY Product_Price DESC;

-- Query 5 : Deleting orders that are of really less amount

DELETE FROM Orders
WHERE Amount < 100;

-- Query 6: To get top 5 spending customers

SELECT c.First_Name, SUM(o.Amount) AS `Money Spent`
FROM Orders o
JOIN Customer c ON o.Customer_ID = c.ID
GROUP BY o.Customer_ID
ORDER BY `Money Spent` DESC
LIMIT 5;

-- Query 7: To find customers who have made at least one order every month in the past 3 months
SELECT Customer.First_Name, Customer.Last_Name
FROM Customer
JOIN Orders ON Customer.ID = Orders.Customer_ID
WHERE Orders.Order_Date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY Customer.First_Name, Customer.Last_Name
HAVING COUNT(DISTINCT DATE_FORMAT(Orders.Order_Date, '%Y%m')) = 3;

-- Query 8: Placing an order

-- Get the sum of the items in the cart for a particular customer
INSERT INTO Orders (Customer_ID, Order_Date, Amount)
SELECT Customer_ID, CURRENT_DATE(), SUM(Quantity * Product_Price)
FROM Cart
JOIN Product ON Cart.Product_ID = Product.ID
WHERE Customer_ID = 'd9b1bd85-fbb7-4a6c-b013-ea399107e057'
GROUP BY Customer_ID;

-- Insert a new transaction record with the latest order details for a particular customer
INSERT INTO Customer_Transaction (Order_ID, Transaction_Date, Amount)
SELECT ID, CURRENT_DATE(), Amount
FROM Orders
WHERE Customer_ID = 'd9b1bd85-fbb7-4a6c-b013-ea399107e057'
ORDER BY Order_Date DESC
LIMIT 1;

-- Delete all items from the cart for a particular customer
DELETE FROM Cart
WHERE Customer_ID = 'd9b1bd85-fbb7-4a6c-b013-ea399107e057';



-- Query 9: Moving a Product from Wishlist to Cart

INSERT INTO Cart (Customer_ID, Product_ID, Quantity)
SELECT Customer_ID, Product_ID, 1
FROM Wishlist
WHERE Customer_ID = 'd9b1bd85-fbb7-4a6c-b013-ea399107e057' AND Product_ID = 'ae298b50-bf90-4766-b75e-6ad7a54cf02e' ;
DELETE FROM Wishlist
WHERE Customer_ID = 'd9b1bd85-fbb7-4a6c-b013-ea399107e057' AND Product_ID = 'ae298b50-bf90-4766-b75e-6ad7a54cf02e';

-- Query 10: Sort products by avg ratings highest to lowest

-- Given solution provide NULL value for avg rating 

SELECT Product.ID, AVG(Review.Review_Rating) AS avg_rating
FROM Product
LEFT JOIN Review ON Product.ID = Review.Product_ID
GROUP BY Product.ID
ORDER BY avg_rating DESC;


-- SELECT ID,'avg' FROM Product, ((SELECT AVG(Review_Rating) AS 'avg',Review.Product_ID AS 'prdct' FROM Review GROUP BY Review.Product_ID) AS Avg_Rating)
-- WHERE ID = 'prdct'
-- ORDER BY 'avg' DESC;



-- Queries to show Constraints

SELECT * FROM information_schema.table_constraints WHERE constraint_type = 'PRIMARY KEY' AND table_name = 'Employee';

SELECT * FROM information_schema.table_constraints WHERE constraint_type = 'FOREIGN KEY' AND table_name = 'Wishlist';



-- Nested query to get top 5 spending customers

SELECT c.First_Name, `Money Spent`
FROM Customer c
JOIN (
  SELECT o.Customer_ID, SUM(o.Amount) AS `Money Spent`
  FROM Orders o
  GROUP BY o.Customer_ID
  ORDER BY `Money Spent` DESC
  LIMIT 5
) m
ON c.ID = m.Customer_ID;










