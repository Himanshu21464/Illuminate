-- OLAPS Queries


-- Rollup queries

-- 1. Average salary of Male and Female employees
SELECT Gender, Age, AVG(Salary) AS Average_Salary 
FROM Employee 
GROUP BY Gender, Age WITH ROLLUP


-- 2. Top 5 Employee roles with highest average salary
SELECT Employee_Role, Age, AVG(Salary) AS Average_Salary 
FROM Employee 
GROUP BY Employee_Role, Age WITH ROLLUP
ORDER BY Average_Salary 
DESC LIMIT 5;

-- 3. Number of Customer in each city

SELECT DISTINCT City, COUNT(*) AS Customer_Count 
FROM Customer 
GROUP BY City, Age WITH ROLLUP
ORDER BY Customer_Count;


-- 4. Age distribution of employees by blood group  (Pivot Table Query)

SELECT Blood_Group, 
       SUM(CASE WHEN Age < 25 THEN 1 ELSE 0 END) AS "<25", 
       SUM(CASE WHEN Age BETWEEN 25 AND 35 THEN 1 ELSE 0 END) AS "25-35", 
       SUM(CASE WHEN Age BETWEEN 36 AND 45 THEN 1 ELSE 0 END) AS "36-45", 
       SUM(CASE WHEN Age > 45 THEN 1 ELSE 0 END) AS ">45"
FROM Employee
GROUP BY Blood_Group;



-- 5. Total Salary paid to employees by blood group
SELECT Blood_Group, SUM(Salary) AS Total_Salary 
FROM Employee 
GROUP BY Blood_Group;
 

-- 6. Average Salary paid to employees by blood group
SELECT Blood_Group, AVG(Salary) AS Average_Salary
FROM Employee
GROUP BY Blood_Group;


-- 7. Number of Employees hired each year
SELECT YEAR(Date_of_Hiring) AS Year, COUNT(*) AS Number_of_Employees
FROM Employee
GROUP BY YEAR(Date_of_Hiring);


-- 8.  Total salary paid to male and female employees by their job role
SELECT Employee_Role, Gender, SUM(Salary) AS Total_Salary
FROM Employee
GROUP BY Employee_Role, Gender;


