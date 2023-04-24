import random
import mysql.connector
from prettytable import PrettyTable
import time
#todo fix address
class Admin:
    
    def __init__(self,uid,connection):
        self.uid = uid
        self.isauthenticated = False
        self.connection = connection
    def authenticate(self):
        print('''|+++++Enter Password+++++|''')
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Login_password FROM Employee WHERE ID ={self.uid}')
        password = cursor.fetchone()[0]
        actual_pass = input()
        if password.strip() == actual_pass.strip():
            self.isauthenticated = True
            print('''|+++++Authenticated+++++|''')
            
        else:
            print('''|+++++Wrong Password+++++|''')
        cursor.close()
        return self.isauthenticated
    def __log_out__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        self.isauthenticated = False
        print('''|+++++Logged Out+++++|''')
    
    
    def unauthorized(self):
        print('''|+++++You are not authorized to view this page+++++|''')
        
        
    
    def __view_product__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------CATALOUGE-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT Product_Name, ID FROM Product')
        result = cursor.fetchall()
        print(result)
        table= PrettyTable()
        table.field_names = [desc[0] for desc in cursor.description]
        for row in result:
            table.add_row(row)
        print(table)
        print("|","_"*50,"|")
        cursor.close()
    def __add_category__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        pass
        CategoryName = input("Enter Category Name: ")
        CategoryDescription = input("Enter Category Description: ")
        
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO Category (CategoryName,CategoryDescription) VALUES ("{CategoryName}","{CategoryDescription}")')
        self.connection.commit()
        cursor.close()
        
    def __delete_category__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        id = int(input("Enter Category ID: "))
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM Category WHERE ID = {id}')
        self.connection.commit()
        cursor.close()
        print(f"Category {id} Deleted")
    def __view_category__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------CATEGORY-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT CategoryName FROM Category')
        result = cursor.fetchall()
        self.print_table(result,cursor)
        cursor.close()
        
    def print_table(self,result,cursor):
        table= PrettyTable()
        table.field_names = [desc[0] for desc in cursor.description]
        for row in result:
            table.add_row(row)
        print(table)
        print("|","-"*50,"|")
        
    def __view_brand__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------BRANDS-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT Brand_Name FROM Brand')
        result = cursor.fetchall()
        self.print_table(result,cursor)
        cursor.close()
    def __add_brand__(self):
        
        if not self.isauthenticated:
            self.unauthorized()
            return
        Brand_Name = input("Enter Brand Name: ")
        Brand_Description = input("Enter Brand Description: ")
        Brand_Logo = input("Enter Brand Logo URL: ")
        Founder = input("Enter Founder Name: ")
        Country_Of_Origin = input("Enter Country Of Origin: ")
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO Brand (Brand_Name,Brand_Description,Brand_Logo,Founder,Country_Of_Origin) VALUES ("{Brand_Name}","{Brand_Description}","{Brand_Logo}","{Founder}","{Country_Of_Origin}")')
        self.connection.commit()
        cursor.close()
        
    def __delete_brand__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        id = int(input("Enter Brand ID: "))
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM Brand WHERE ID = {id}')
        self.connection.commit()
        cursor.close()
        print(f"Brand {id} Deleted")
    def __view_customer__(self):
        
        
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------Customers-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Customer')
        result = cursor.fetchall()
        self.print_table(result,cursor)
        cursor.close()
        
    def __view_seller__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------Sellers-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Seller')
        result = cursor.fetchall()
        self.print_table(result,cursor)
        cursor.close()
    
    def __view_employee__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------Employee-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM Employee')
        result = cursor.fetchall()
        self.print_table(result,cursor)
        cursor.close()
    def __update__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        print('|__________________________UPDATE__________________________|')
        field = input('''Select The Field You Want To Update
                1. Address  
                2. Email
                3. Password
              ''')
        field = ["Address","Email","Password"][int(field)-1]
        cursor = self.connection.cursor()
        if self.authenticate():
            value = input(f'''Enter the new {field}''')
            cursor.execute(f'UPDATE Seller SET {field} = {value} WHERE ID = {self.uid}')
            self.connection.commit()
            print(f'''|+++++{field} Updated+++++|''')
        cursor.close()
    def menu(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        function_tuple_list = [
               
            (self.__view_product__,"View Product Catalogue"),
            (self.__view_category__,'View Category List'),
            (self.__add_category__,"Add Category"),
            (self.__delete_category__,"Delete Category"),
            (self.__view_brand__,'View Brand List'),
            (self.__add_brand__,"Add Brand"),
            (self.__delete_brand__,"Delete Brand"),
            (self.__view_customer__,"View Customer"),
            (self.__view_seller__,"View Seller"),
            (self.__view_employee__,"View Employee"),
            (self.__update__,"Update Personal Details"),
            (self.__log_out__,"Logout"),
            ]
        flag = 1
        while flag:
            print("|------------------------------Main Menu----------------------------|")
            for idx,val in enumerate(function_tuple_list):
                print(f"{idx+1}. {val[1]}")
            choice = int(input("Choose Your Action:"))-1
            func = function_tuple_list[choice][0]
            func()
            flag = int(input("Do you want to go back to main menu?\n 0<- No\n 1<- Yes\n"))
        if self.isauthenticated: self.__log_out__()
    
        
    #TODO: Show Statistical data (monthly, quarterly, yearly revenue, top selling products, etc)
    #TODO: Total no. of employees, customers 
    