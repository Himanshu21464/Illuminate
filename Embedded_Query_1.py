#------------------------------------------------- Embedded Queries---------------------------------------------------

def EMBEDDED_QUERY_1():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute("SELECT First_Name, Middle_Name, Last_Name FROM Employee where Age <=60 and Age >= 18")

    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def EMBEDDED_QUERY_2():
        # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute("SELECT First_Name, Middle_Name, Last_Name,Employee_Role, Email, Gender, Age, Blood_Group FROM Employee WHERE Blood_Group='O+'")

    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def EMBEDDED_QUERY_3():

     # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute("SELECT First_Name, Middle_Name, Last_Name,Employee_Role, Email, Gender, Age, Salary, Time_in_Company FROM Employee WHERE Time_in_Company > 4")
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def EMBEDDED_QUERY_4():

     # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute("SELECT * FROM Product ORDER BY Product_Price")
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()
    
def EMBEDDED_QUERY_5():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute("SELECT * FROM Category ORDER BY CategoryName")
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def EMBEDDED_QUERY_6():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
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


    # define an SQL query to insert data into the table
    query = "insert into Customer ( First_Name, Middle_Name, Last_Name, Email, Login_Password, Date_of_Birth, Gender, House_Number, Locality, City, State_, Country, Pincode) values ( %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s);"

    # create a cursor object to execute the query
    cursor = connection.cursor()

    # execute the query with user input values as parameters
    cursor.execute(query, (fname, mname,lname, email,password,dob,gender,house,locality,city,state,country,pincode))

    # commit the changes to the database
    connection.commit()

    # print a message to indicate the successful insertion of data
    print("Customer Registered successfully!!!\n")

    cursor.execute("UPDATE Customer SET Age = DATE_FORMAT(FROM_DAYS(DATEDIFF(NOW(), Date_of_Birth)), '%Y') + 0;")
    connection.commit()

    cursor.close()
    connection.close()

#----------------------------------------------------OLAPS Queries ---------------------------------------------------

def OLAPS_QUERY_1():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute("SELECT Gender, Age, AVG(Salary) AS Average_Salary FROM Employee GROUP BY Gender, Age WITH ROLLUP")
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def OLAPS_QUERY_2():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute('''SELECT Employee_Role, Age, AVG(Salary) AS Average_Salary 
                      FROM Employee 
                      GROUP BY Employee_Role, Age WITH ROLLUP
                      ORDER BY Average_Salary 
                      DESC LIMIT 5;
                      ''')
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def OLAPS_QUERY_3():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute('''SELECT DISTINCT City, COUNT(*) AS Customer_Count 
                      FROM Customer 
                      GROUP BY City, Age WITH ROLLUP
                      ORDER BY Customer_Count;
                      ''')
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

def OLAPS_QUERY_4():
    # mySQL Embedded Queries 

    import mysql.connector
    from prettytable import PrettyTable

    # establish a connection to the MySQL server
    connection = mysql.connector.connect(user='root',
                                password='Himanshu@2022',
                                host='localhost',
                                database='Illuminate')

    # create a cursor object to interact with the database
    cursor = connection.cursor()

    # execute a query
    cursor.execute('''SELECT Blood_Group, 
       SUM(CASE WHEN Age < 25 THEN 1 ELSE 0 END) AS "<25", 
       SUM(CASE WHEN Age BETWEEN 25 AND 35 THEN 1 ELSE 0 END) AS "25-35", 
       SUM(CASE WHEN Age BETWEEN 36 AND 45 THEN 1 ELSE 0 END) AS "36-45", 
       SUM(CASE WHEN Age > 45 THEN 1 ELSE 0 END) AS ">45"
    FROM Employee
    GROUP BY Blood_Group;''')
   
    # fetch all Result
    Result = cursor.fetchall()

    table= PrettyTable()
    table.field_names = [desc[0] for desc in cursor.description]

    for row in Result:
        table.add_row(row)


    print(table)

    cursor.close()
    connection.close()

# ----------------------------------------------------Interface-------------------------------------------------------

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
    print("|                        3. Exit                                             |")
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
            exit
        else:
            print("Wrong option!! Please select the option you want:")

MAIN_INTERFACE()