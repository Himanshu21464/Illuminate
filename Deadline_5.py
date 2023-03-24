#------------------------------------------------- Embedded Queries---------------------------------------------------

def EMBEDDED_QUERY_1():

    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT First_Name, Middle_Name, Last_Name FROM Employee where Age <=60 and Age >= 18")

    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def EMBEDDED_QUERY_2():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT First_Name, Middle_Name, Last_Name,Employee_Role, Email, Gender, Age, Blood_Group FROM Employee WHERE Blood_Group='O+'")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def EMBEDDED_QUERY_3():

     # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT First_Name, Middle_Name, Last_Name,Employee_Role, Email, Gender, Age, Salary, Time_in_Company FROM Employee WHERE Time_in_Company > 4")
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def EMBEDDED_QUERY_4():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT * FROM Product ORDER BY Product_Price")
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()
    
def EMBEDDED_QUERY_5():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT * FROM Category ORDER BY CategoryName")
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def EMBEDDED_QUERY_6():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
# Cursor object
    cursor = connection.cursor()
    # get user input data
    fname =   input("Enter your First Name     : ")
    mname =   input("Enter your Middle Name    : ")
    lname =   input("Enter your Last Name      : ")
    dob=     input("Enter your Date of Birth  : ")
    gender=  input("Enter your gender         : ")
    email =  input("Enter your Email          : ")
    password=input("Set a login password      : ")
    house=   int(input("Enter your house no.      : "))
    locality=input("Enter your Locality       : ")
    city=    input("Enter your City           : ")
    state=   input("Enter your State          : ")
    country= input("Enter your Country        : ")
    pincode= input("Enter your pincode        : ")


    query = "insert into Customer ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, House_Number, Locality, City, State_, Country, Pincode) values ( %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);"

    cursor = connection.cursor()

    cursor.execute(query, (fname, mname,lname, email,password,dob,gender,house,locality,city,state,country,pincode))

    connection.commit()

    print("Customer Registered successfully!!!\n")

    cursor.execute("UPDATE Customer SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;")
    connection.commit()

    cursor.close()
    connection.close()

#----------------------------------------------------OLAPS Queries ---------------------------------------------------

def OLAPS_QUERY_1():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT Gender, Age, AVG(Salary) AS Average_Salary FROM Employee GROUP BY Gender, Age WITH ROLLUP")
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def OLAPS_QUERY_2():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute('''SELECT Employee_Role, Age, AVG(Salary) AS Average_Salary 
                      FROM Employee 
                      GROUP BY Employee_Role, Age WITH ROLLUP
                      ORDER BY Average_Salary 
                      DESC LIMIT 5;
                      ''')
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def OLAPS_QUERY_3():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute('''SELECT DISTINCT City, COUNT(*) AS Customer_Count 
                      FROM Customer 
                      GROUP BY City, Age WITH ROLLUP
                      ORDER BY Customer_Count;
                      ''')
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def OLAPS_QUERY_4():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute('''SELECT Blood_Group, 
       SUM(CASE WHEN Age < 25 THEN 1 ELSE 0 END) AS "<25", 
       SUM(CASE WHEN Age BETWEEN 25 AND 35 THEN 1 ELSE 0 END) AS "25-35", 
       SUM(CASE WHEN Age BETWEEN 36 AND 45 THEN 1 ELSE 0 END) AS "36-45", 
       SUM(CASE WHEN Age > 45 THEN 1 ELSE 0 END) AS ">45"
    FROM Employee
    GROUP BY Blood_Group;''')
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

#------------------------------------------------------TRIGGERS-------------------------------------------------------
def TRIGGERS_1():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
# Cursor object
    cursor = connection.cursor()

    # execute the query with user input values as parameters
    cursor.execute("insert into Customer ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, House_Number, Locality, City, State_, Country, Pincode) values ( 'Kyrstin', 'Sidnee', 'Lusted', 'slusted0@wix.com', 'VOcjPj054', '1996-09-18', 'Male', 9729, 'Doe Crossing', 'Kungsbacka', 'Halland', 'Sweden', '434 43');")
    connection.commit()
    cursor.execute("insert into Customer_Mobile_Numbers (Customer_ID, Mobile_Number) values ( 1, 9357925749);")
    connection.commit()
    cursor.execute("insert into Customer_Mobile_Numbers (Customer_ID, Mobile_Number) values ( 1, 4618992068);")  
    connection.commit()
    cursor.execute("insert into Brand ( Brand_Name, Brand_Description, Brand_Logo, Founder, Country_Of_Origin) values ( 'Tatcha', 'Luxury skincare inspired by Japanese beauty rituals', 'http://mapy.cz/nulla.json', 'Isaac Trevarthen', 'Indonesia');")
    connection.commit()
    cursor.execute("insert into Brand ( Brand_Name, Brand_Description, Brand_Logo, Founder, Country_Of_Origin) values ( 'The Ordinary', 'Clinical formulations with integrity', 'https://blogger.com/lectus/vestibulum/quam.png', 'Harlen Fiddeman', 'Serbia');  ")
    connection.commit()
    cursor.execute("insert into Category ( CategoryName, CategoryDescription) values ( 'Makeup', 'Cosmetics for enhancing beauty');")
    connection.commit()
    cursor.execute("insert into Category ( CategoryName, CategoryDescription) values ( 'Skincare', 'skincare for keeping skin healthy and youthful');  ")
    connection.commit()
    cursor.execute("insert into Seller ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Company_Name, Property_Number, Locality, City, State_, Country, Pincode) values ( 'Ulberto', 'Alyss', 'Ibbotson', 'aibbotson0@phpbb.com', '0jekEUQ', 3157982690, 'Gusikowski and Sons', 5901, 'Tony', 'Ifanes', 'Bragança', 'Portugal', '5210-105');")
    connection.commit()
    cursor.execute("insert into Seller ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Mobile_Number, Company_Name, Property_Number, Locality, City, State_, Country, Pincode) values ( 'Sid', 'Cass', 'Grigoroni', 'cgrigoroni1@posterous.com', 'xTQt3g', 3160468333, 'Schowalter-Hand', 7298, 'Sullivan', 'Augusta', 'Georgia', 'United States', '30905');  ")
    connection.commit()
    cursor.execute("insert into Product (Product_Name, Product_Description, Product_Price, Product_Quantity, Product_Images, CATEGORY_ID, BRAND_ID, SELLER_ID) values ('L''Oreal Paris Voluminous Lash Paradise Mascara', 'volumizing mascara for intense length and volume', 76671.79, 4142, 'http://tumblr.com/pede/justo/eu.xml', 1, 1, 1);")
    connection.commit()
    cursor.execute("insert into Product (Product_Name, Product_Description, Product_Price, Product_Quantity, Product_Images, CATEGORY_ID, BRAND_ID, SELLER_ID) values ('Maybelline SuperStay Matte Ink Liquid Lipstick', 'long wear matte lipstick with vibrant color', 77981.51, 7553, 'http://google.com.au/varius.jsp', 1, 1, 1);  ")
    connection.commit()
    cursor.execute("insert into Cart (Quantity, Discount, Product_ID, Customer_ID) values (126, 51.8, 1, 1);  ")
    connection.commit()
    cursor.execute("insert into Orders (Order_Date, Amount, Order_Status, Delivery_Date, Delivery_Fee, Customer_ID) values ('2022-12-26', 788673.65, 'Under Process', '2022-02-22', 67.28, 1);  ")
    connection.commit()
    cursor.execute("insert into Review ( Review_Rating, Review_Title, Comments, Review_Date, Product_ID, Customer_ID) values ( 5, 'Amazing product!', 'This product has exceeded my expectations. It made my skin feel so smooth and soft. Highly recommended!', '2022-10-23', 1, 1);")
    # commit the changes to the database
    connection.commit()

    # print a message to indicate the successful insertion of data
    # print("Data inserted into Review table!!\n")
    
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    cursor.execute("SELECT Review_Date FROM Review WHERE ID = 1;")

    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    #print("Customer's Cart is empty after successful transaction!!!")

    print(table)
    cursor.close()
    connection.close()

def TRIGGERS_2():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    cursor = connection.cursor()

    print("------------Quantity of Product before successful transaction---------- \n")
    
    cursor.execute("SELECT Product_Quantity FROM Product WHERE ID=1;")

    # Data Retrieval
    Result1 = cursor.fetchall()

    table1= PrettyTable()
    table1.field_names = [desc[0] for desc in cursor.description]

    for row in Result1:
        table1.add_row(row)

    print("Customer's Cart is empty after successful transaction!!!\n")

    print(table1)

    print("----------This query is to verify the before and after Data_Retrieved for trigger 3---------------\n")
    print("          Cart of customer before transaction:- \n\n")
    cursor.execute("SELECT * FROM Cart WHERE Customer_ID=1;")

    # Data Retrieval
    Result2 = cursor.fetchall()

    table2= PrettyTable()
    table2.field_names = [desc[0] for desc in cursor.description]

    for row in Result2:
        table2.add_row(row)

    print("Customer's Cart is empty after successful transaction!!!\n")

    print(table2)

    cursor.execute("insert into Customer_Transaction (Transaction_Date, Amount, Transaction_Status, Payment_Method, Order_ID, Customer_ID) values ('1953-09-27', 52.88, 'Successful', 'Credit/Debit Card', 1, 1);")

    # commit the changes to the database
    connection.commit()

    print("Quantity of Product after successful transaction: \n")
    cursor.execute("SELECT Product_Quantity FROM Product WHERE ID=1;")

     # Data Retrieval
    Result3 = cursor.fetchall()

    table3= PrettyTable()
    table3.field_names = [desc[0] for desc in cursor.description]

    for row in Result3:
        table3.add_row(row)

    print("Customer's Cart is empty after successful transaction!!!\n")

    print(table3)
    cursor.close()
    connection.close()

def TRIGGERS_3():
    import mysql.connector
    from prettytable import PrettyTable

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT * FROM Cart;")
   
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print("Customer's Cart is empty after successful transaction!!!")

    print(table)
    cursor.close()
    connection.close()

# ----------------------------------------------------Interface-------------------------------------------------------

def TRIGGERS_QUERIES():
    print("|-------------------------------------Triggers-------------------------------------------|")
    print("|                                                                                        |")
    print("| 1. Update reviews date                                                                 |")
    print("| 2. Reduce Product_Quantity after Successful Transaction                                |")
    print("| 3. Empty Customer's Cart after placing order                                           |")
    print("| 4. Return to main menu                                                                 |")
    print("|----------------------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=5:
        #print("|----------------------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|----------------------------------------------------------------------------------------|")
        temp=option
        if option==1:
            TRIGGERS_1()
        elif option==2:
            TRIGGERS_2()
        elif option==3:
            TRIGGERS_3()
        elif option==4:
            MAIN_INTERFACE()
        else:
            print("Wrong option!! Please select the option you want:")

def OLAPS_QUERIES():
    print("|-----------------------OLAPS Queries supported------------------------------------------|")
    print("|                                                                                        |")
    print("| 1. Average salary of Male and Female employees group by gender and age                 |")
    print("| 2. Top 5 Employee roles with highest average salary group by Employee role and age     |")
    print("| 3. Number of Customer in each city group by city and age                               |")
    print("| 4. Age distribution of employees by blood group  (Pivot Table Query)                   |")
    print("| 5. Return to main menu                                                                 |")
    print("|----------------------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=5:
        #print("|----------------------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|----------------------------------------------------------------------------------------|")
        temp=option
        if option==1:
            OLAPS_QUERY_1()
        elif option==2:
            OLAPS_QUERY_2()
        elif option==3:
            OLAPS_QUERY_3()
        elif option==4:
            OLAPS_QUERY_4()
        elif option==5:
            MAIN_INTERFACE()
        else:
            print("Wrong option!! Please select the option you want:")

def EMBEDDED_QUERIES():
    print("|-----------------------Embedded Queries supported--------------------------------------|")
    print("|                                                                                       |")
    print("| 1. Name of Customers whose age is between 18 and 60                                   |")
    print("| 2. Employees details whose blood group is 'O+'                                        |")
    print("| 3. Employees details with work experience more than 4 years                           |")
    print("| 4. Show products sorted by their price                                                |")
    print("| 5. List all category names available in the database in ascending order               |")
    print("| 6. Customer Signup                                                                    |")
    print("| 7. Return to main menu                                                                |")
    print("|---------------------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=7:
        #print("|---------------------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|---------------------------------------------------------------------------------------|")
        temp=option
        if option==1:
            EMBEDDED_QUERY_1()
        elif option==2:
            EMBEDDED_QUERY_2()
        elif option==3:
            EMBEDDED_QUERY_3()
        elif option==4:
            EMBEDDED_QUERY_4()
        elif option==5:
            EMBEDDED_QUERY_5()
        elif option==6:
            EMBEDDED_QUERY_6()
        elif option==7:
            MAIN_INTERFACE()
        else:
            print("Wrong option!! Please select the option you want:")

def MAIN_INTERFACE():
    print("|------------------------Queries supported-----------------------------------|")
    print("|                                                                            |")
    print("|                        1. Embedded Queries                                 |")
    print("|                        2. OLAPS Queries                                    |")
    print("|                        3. Triggers                                         |")
    print("|                        4. Exit                                             |")
    print("|----------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=3:
        #print("|----------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|----------------------------------------------------------------------------|")
        temp=option
        if option==1:
            EMBEDDED_QUERIES()
        elif option==2:
            OLAPS_QUERIES()
        elif option==3:
            TRIGGERS_QUERIES()
        elif option==4:
            exit
        else:
            print("Wrong option!! Please select the option you want:")

MAIN_INTERFACE()