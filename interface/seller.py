import random
import mysql.connector
from prettytable import PrettyTable
import time


class Seller:
    def __init__(self,uid,connection):
        self.uid = uid
        self.isauthenticated = False
        self.connection = connection
    def authenticate(self):
        print('''|+++++Enter Password+++++|''')
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Login_password FROM Seller WHERE ID ={self.uid}')
        password = cursor.fetchone()[0]
        actual_pass = input()
        if password.strip() == actual_pass.strip():
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
    
    
    def __delete__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM Seller WHERE ID = {self.uid}')
        self.connection.commit()
        self.__log_out__()
        print("Account Deleted")
    
    def unauthorized(self):
        print('''|+++++You are not authorized to view this page+++++|''')
        
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
        
        
    def __add_product__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        pass
        Product_Name = input("Enter Product Name: ")
        Product_Description = input("Enter Product Description: ")
        Product_Price = float(input("Enter Product Price: "))
        Product_Quantity = int(input("Enter Product Quantity: "))
        Product_Images = input("Enter Product Image url: ")
        CATEGORY_ID = int(input("Enter Category ID: "))
        BRAND_ID = int(input("Enter Brand ID: "))
        SELLER_ID = self.uid
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO Product (Product_Name,Product_Description,Product_Price,Product_Quantity,Product_Images,CATEGORY_ID,BRAND_ID,SELLER_ID) VALUES ("{Product_Name}","{Product_Description}",{Product_Price},{Product_Quantity},"{Product_Images}",{CATEGORY_ID},{BRAND_ID},{SELLER_ID})')
        self.connection.commit()
        cursor.close()
        
    def __delete_product__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        id = int(input("Enter Product ID: "))
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM Product WHERE ID = {id} AND SELLER_ID = {self.uid}')
        self.connection.commit()
        cursor.close()
        print(f"Product {id} Deleted")
        
    
    def menu(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        function_tuple_list = [
               
            (self.__view_product__,"View Product Catalogue"),
            (self.__add_product__,"Add Product"),
            (self.__delete_product__,"Delete Product"),
            (self.__update__,"Update Personal Details"),
            (self.__log_out__,"Logout"),
            (self.__delete__,"Delete the account")
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
        
        
    #TODO: Show customer profile/details (Couldn;t understand)