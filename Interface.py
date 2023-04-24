#------------------------------------------------- Embedded Queries---------------------------------------------------

def STATISTICAL_DATA():



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
    cursor.execute("SELECT COUNT(ID) as Total_Customers FROM Customer;")

    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()


    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT COUNT(ID) as Total_Employee FROM Employee;")

    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT COUNT(ID) as Total_Brands FROM Brand;")

    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()


    #Connecting to Database
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')
    # Cursor object
    cursor = connection.cursor()

    # Query Execution
    cursor.execute("SELECT COUNT(ID) as Total_Transactions FROM Customer_Transaction;")

    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def EMPLOYEE_DETAILS():
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
    cursor.execute("SELECT * FROM Employee WHERE ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_DETAILS():
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
    cursor.execute("SELECT * FROM Customer")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def PRODUCT_DETAILS():
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
    cursor.execute("SELECT * FROM Product")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_CART_DETAILS():
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
    cursor.execute("SELECT * FROM Cart WHERE Customer_ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_WISHLIST_DETAILS():
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
    cursor.execute("SELECT * FROM WISHLIST WHERE Customer_ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_ORDERS_DETAILS():
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
    cursor.execute("SELECT * FROM Orders WHERE Customer_ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_TRANSACTIONS_DETAILS():
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
    cursor.execute("SELECT * FROM Customer_Transaction WHERE Customer_ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def SELLER_DETAILS():
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
    cursor.execute("SELECT * FROM Seller")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def BRAND_DETAILS():
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
    cursor.execute("SELECT * FROM Brand")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CATEGORY_DETAILS():
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
    cursor.execute("SELECT * FROM Category")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def DELETE_CUSTOMER():
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
    cursor.execute("DELETE FROM Customer WHERE ID=1")
    
    print("Deleted Successfully!!")

    cursor.close()
    connection.close()

def DELETE_PRODUCT():
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
    cursor.execute("DELETE FROM Product WHERE ID=1")
    
    print("Deleted Successfully!!")

    cursor.close()
    connection.close()

def DELETE_CATEGORY():
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
    cursor.execute("DELETE FROM Category WHERE ID=1")
    
    print("Deleted Successfully!!")

    cursor.close()
    connection.close()

def DELETE_BRAND():
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
    cursor.execute("DELETE FROM Brand WHERE ID=1")
    
    print("Deleted Successfully!!")

    cursor.close()
    connection.close()

def DELETE_SELLER():
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
    cursor.execute("DELETE FROM Seller WHERE ID=1")
    
    print("Deleted Successfully!!")

    cursor.close()
    connection.close()

def DELETE_EMPLOYEE():
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
    cursor.execute("DELETE FROM Employee WHERE ID=1")
    
    print("Deleted Successfully!!")

    cursor.close()
    connection.close()

def CUSTOMER_SIGNUP():
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

def EMPLOYEE_SIGNUP():
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
    fname = input("Enter your First Name : ")
    mname = input("Enter your Middle Name : ")
    lname = input("Enter your Last Name : ")
    email = input("Enter your Email : ")
    password=input("Set a login password : ")
    dob= input("Enter your Date of Birth : ")
    gender= input("Enter your gender : ")
    age= int(input("Enter your Age : "))
    house= int(input("Enter your house no. : "))
    locality=input("Enter your Locality : ")
    city= input("Enter your City : ")
    state= input("Enter your State : ")
    country= input("Enter your Country : ")
    pincode= input("Enter your pincode : ")
    role= input("Enter your Role : ")
    doj= input("Enter your Date of Joining: ")
    company_time= int(input("Enter your Time in Company: "))
    pan= input("Enter your PAN : ")
    blood_group= input("Enter your Blood Group : ")
    emergency_contact_number= input("Enter your Emergency Contact Number: ")
    emergency_contact_name= input("Enter your Emergency Contact Name : ")
    salary= float(input("Enter your Salary : "))
    mobile_numbers= input("Enter your Mobile Numbers (separated by commas): ")
    mobile_numbers_list= mobile_numbers.split(",")



    query_employee = """INSERT INTO Employee (First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, Age, House_Number, Locality, City, State_, Country, Pincode, Employee_Role, Date_of_Hiring, Time_in_Company, PAN, Blood_Group, Emergency_Contact_Number, Emergency_Contact_Name, Salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    data_employee = (fname, mname, lname, email, password, dob, gender, age, house, locality, city, state, country, pincode, role, doj, company_time, pan, blood_group, emergency_contact_number, emergency_contact_name, salary)

    cursor = connection.cursor()
    cursor.execute(query_employee, data_employee)
    employee_id = cursor.lastrowid  

    query_mobile_numbers = """INSERT INTO Employee_Mobile_Numbers (Employee_ID, Mobile_Number) VALUES (%s, %s)"""
    data_mobile_numbers = [(employee_id, mobile_number.strip()) for mobile_number in mobile_numbers_list]

    cursor.executemany(query_mobile_numbers, data_mobile_numbers)
    connection.commit()


    print("Employee Registered successfully!!!\n")

    cursor.execute("UPDATE Employee SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;")
    connection.commit()


    cursor.close()
    connection.close()

def SELLER_SIGNUP():
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
    dob=     input("Enter your mobile no.     : ")
    gender=  input("Enter your gender         : ")
    email =  input("Enter your Email          : ")
    password=input("Set a login password      : ")
    house=   int(input("Enter your Property no.      : "))
    locality=input("Enter your Locality       : ")
    city=    input("Enter your City           : ")
    state=   input("Enter your State          : ")
    country= input("Enter your Country        : ")
    pincode= input("Enter your pincode        : ")


    query = "insert into Customer ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, Property_Number, Locality, City, State_, Country, Pincode) values ( %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);"

    cursor = connection.cursor()

    cursor.execute(query, (fname, mname,lname, email,password,dob,gender,house,locality,city,state,country,pincode))

    connection.commit()

    print("Customer Registered successfully!!!\n")

    cursor.execute("UPDATE Customer SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;")
    connection.commit()

    cursor.close()
    connection.close()

def ADD_PRODUCT():
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
    fname =   input("Enter Product Name     : ")
    mname =   input("Enter Description    : ")
    lname =   input("Enter Price      : ")
    dob=     input("Enter Quantity     : ")
    gender=  input("Enter Images         : ")
    house =   input("Enter Category ID      : ")
    locality=     input("Enter Brand ID     : ")
    city=  input("Enter Seller ID         : ")


    query = "insert into Product (Product_Name, Product_Description, Product_Price, Product_Quantity, Product_Images, CATEGORY_ID, BRAND_ID, SELLER_ID) values ( %s, %s, %s, %s, %s, %s, %s,%s);"

    cursor = connection.cursor()

    cursor.execute(query, (fname, mname,lname,dob,gender,house,locality,city))

    connection.commit()

    print("Product added successfully!!!\n")

    cursor.close()
    connection.close()

def ADD_CATEGORY():
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
    fname =   input("Enter Category Name     : ")
    mname =   input("Enter Description    : ")
    

    query = "insert into Category ( CategoryName, CategoryDescription) values ( %s, %s);"

    cursor = connection.cursor()

    cursor.execute(query, (fname, mname,lname,dob,gender,house,locality,city))

    connection.commit()

    print("Category added successfully!!!\n")

    cursor.close()
    connection.close()

def SELLER_PROFILE():
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
    cursor.execute("SELECT * FROM Seller WHERE ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_PROFILE():
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
    cursor.execute("SELECT * FROM Customer WHERE ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def EMPLOYEE_PROFILE():
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
    cursor.execute("SELECT * FROM Employee WHERE ID=1")
    
    # Data Retrieval
    Data_Retrieved = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Data_Retrieved:
        table.add_row(row)

    print(table)
    cursor.close()
    connection.close()

def CUSTOMER_PROFILE():
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
    cursor.execute("SELECT * FROM Customer WHERE ID=1")
    
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

def CUSTOMER_SIGNUP():
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

def OLAPS_QUERY_5():
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
    cursor.execute('''SELECT 
                            YEAR(Date_of_Hiring) AS Year, 
                            QUARTER(Date_of_Hiring) AS Quarter, 
                            COUNT(*) AS Number_of_Employees 
                        FROM 
                            Employee 
                        GROUP BY 
                            YEAR(Date_of_Hiring), 
                            QUARTER(Date_of_Hiring)
                            WITH ROLLUP;

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






def SELLER_PORTAL():
    print("--------Enter your credentials to login------\n")
    id=(input(print("Enter Login ID (Email): ")))
    password=(input(print("Enter Login password: ")))

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
    cursor.execute("SELECT ID from Seller WHERE Email= %s",(id))
    data=cursor.fetchall()
    cursor.execute("SELECT ID from Seller WHERE Login_Password= %s",(password))
    data2=cursor.fetchall()

    if(data==data2):
        print("Login Successfully!!")
    else:
        print("Wrong Password!!")
        op=input(print("Enter 1 for exit and 2 to try again: "))
        if(op==1):
            MAIN_INTERFACE()
        elif(op==2):
            ADMIN_PORTAL()
    

    cursor.close()
    connection.close()



    print("|-------------------------------------Seller Portal-------------------------------------------|")
    print("|                                                                                             |")
    print("| 1. View Profile                                                                             |")
    print("| 2. Update details                                                                           |")
    print("| 3. Return to main menu                                                                      |")
    print("|---------------------------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=4:
        #print("|----------------------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|----------------------------------------------------------------------------------------|")
        temp=option
        if option==1:
            SELLER_PROFILE()
        elif option==2:
            UPDATE_SELLER()
        elif option==3:
            TRIGGERS_3()
        elif option==4:
            MAIN_INTERFACE()
        else:
            print("Wrong option!! Please select the option you want:")

def CUSTOMER_PORTAL():
    print("--------Enter your credentials to login------\n")
    id=(input(print("Enter Login ID (Email): ")))
    password=(input(print("Enter Login password: ")))

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
    cursor.execute("SELECT ID from Customer WHERE Email= %s",(id))
    data=cursor.fetchall()
    cursor.execute("SELECT ID from Customer WHERE Login_Password= %s",(password))
    data2=cursor.fetchall()

    if(data==data2):
        print("Login Successfully!!")
    else:
        print("Wrong Password!!")
        op=input(print("Enter 1 for exit and 2 to try again: "))
        if(op==1):
            MAIN_INTERFACE()
        elif(op==2):
            ADMIN_PORTAL()
    

    cursor.close()
    connection.close()

    print("|--------------------------------CUSTOMER PORTAL-----------------------------------------|")
    print("|                                                                                        |")
    print("|  1. Explore Products                                                                   |")
    print("|  2. View Category                                                                      |")
    print("|  3. View Brands                                                                        |")
    print("|  4. Upgrade Membership                                                                 |")
    print("|  5. Add money to the wallet                                                            |")
    print("|  6. Place an Order                                                                     |")
    print("|  7. Add products to cart                                                               |")
    print("|  8. View Cart                                                                          |")
    print("|  9. View wishlist                                                                      |")
    print("| 10. Add Product to wishlist                                                            |")
    #print("| 11. Change password                                                                    |")
    print("| 11. Add a review on product                                                            |")
    print("| 12. Empty Cart                                                                         |")
    print("| 13. Empty Wishlist                                                                     |")
    print("| 14. View All Transactions                                                              |")
    print("| 15. Show profile                                                                       |")
    print("| 16. Delete Account                                                                     |")
    print("| 17. Return to main menu                                                                |")
    print("|----------------------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=18:
        #print("|----------------------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|----------------------------------------------------------------------------------------|")
        temp=option
        if option==1:
            PRODUCT_DETAILS()
        elif option==2:
            CATEGORY_DETAILS()
        elif option==3:
            BRAND_DETAILS()
        elif option==4:
            UPGRADE_MEMBERSHIP()
        elif option==5:
            ADD_MONEY()
        elif option==6:
            ORDER()
        elif option==7:
            BRAND_DETAILS()
        elif option==8:
            ADD_PRODUCT_TO_CART()
        elif option==9:
            ADD_MONEY()
        elif option==5:
            ADD_MONEY()
        elif option==6:
            CATEGORY_DETAILS()
        elif option==7:
            BRAND_DETAILS()
        elif option==8:
            UPGRADE_MEMBERSHIP()
        elif option==9:
            ADD_MONEY()
        elif option==17:
            MAIN_INTERFACE()
        else:
            print("Wrong option!! Please select the option you want:")

def ADMIN_PORTAL():

    print("--------Enter your credentials to login------\n")
    id=(input(print("Enter Login ID (Email): ")))
    password=(input(print("Enter Login password: ")))

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
    cursor.execute("SELECT ID from Employee WHERE Email= %s",(id))
    data=cursor.fetchall()
    cursor.execute("SELECT ID from Employee WHERE Login_Password= %s",(password))
    data2=cursor.fetchall()

    if(data==data2):
        print("Login Successfully!!")
    else:
        print("Wrong Password!!")
        op=input(print("Enter 1 for exit and 2 to try again: "))
        if(op==1):
            MAIN_INTERFACE()
        elif(op==2):
            ADMIN_PORTAL()
    

    cursor.close()
    connection.close()

    

    print("|--------------------------ADMINISTRATION PORTAL-----------------------------------------|")
    print("|                                                                                        |")
    print("|  1. Add an Employee                                                                    |")
    print("|  2. View Employee Details                                                              |")
    print("|  3. View Customer Details                                                              |")
    print("|  4. View Seller Details                                                                |")
    print("|  5. View Brand Details                                                                 |")
    print("|  6. Update Employee Details                                                            |")
    print("|  7. View Category Details                                                              |")
    print("|  8. Add products                                                                       |")
    print("|  9. Add category                                                                       |")
    print("| 10. Explore Products                                                                   |")
    print("| 11. Delete Product                                                                     |")
    print("| 12. Delete Category                                                                    |")
    print("| 13. Statistical Data                                                                   |")
    print("| 14. Delete Customer                                                                    |")
    print("| 15. Delete Brand                                                                       |")
    print("| 16. Delete seller                                                                      |")
    print("| 17. Delete Employee                                                                    |")
    print("| 18. Return to main menu                                                                |")
    print("|----------------------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=19:
        #print("|---------------------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|---------------------------------------------------------------------------------------|")
        temp=option
        if option==1:
            EMPLOYEE_SIGNUP()
        elif option==2:
            EMPLOYEE_DETAILS()
        elif option==3:
            CUSTOMER_DETAILS()
        elif option==4:
            SELLER_DETAILS()
        elif option==5:
            BRAND_DETAILS()
        elif option==6:
            EMPLOYEE_PROFILE()
        elif option==7:
            CATEGORY_DETAILS()
        elif option==8:
            ADD_PRODUCT()
        elif option==9:
            ADD_CATEGORY()
        elif option==10:
            PRODUCT_DETAILS()
        elif option==11:
            DELETE_PRODUCT()
        elif option==12:
            DELETE_CATEGORY()
        elif option==13:
            STATISTICAL_DATA()
        elif option==14:
            DELETE_CUSTOMER()
        elif option==15:
            DELETE_BRAND()
        elif option==16:
            DELETE_SELLER()
        elif option==17:
            DELETE_EMPLOYEE()
        elif option==18:
            MAIN_INTERFACE()
    
        
        else:
            print("Wrong option!! Please select the option you want:")





def MAIN_INTERFACE():
    print("|------------------------Welcome to Illuminate-------------------------------|")
    print("|                                                                            |")
    print("|                        1. Administration Portal                            |")
    print("|                        2. Customer Portal                                  |")
    print("|                        3. Seller Portal                                    |")
    print("|                        4. Exit                                             |")
    print("|----------------------------------------------------------------------------|\n")

    temp=0
    while True and temp !=4:
        #print("|----------------------------------------------------------------------------|")
        option=int(input("Choose any of the above options: "))
        #print("|----------------------------------------------------------------------------|")
        temp=option
        if option==1:
            ADMIN_PORTAL()
        elif option==2:
            CUSTOMER_PORTAL()
        elif option==3:
            SELLER_PORTAL()
        elif option==4:
            exit
        else:
            print("Wrong option!! Please select the option you want:")

MAIN_INTERFACE()



