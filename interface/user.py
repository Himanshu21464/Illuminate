import random
import mysql.connector
from prettytable import PrettyTable
import time
class User:
    def __init__(self,uid,connection):
        self.uid = uid
        self.isauthenticated = False
        self.connection = connection
    def authenticate(self):
        print('''|+++++Enter Password+++++|''')
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Login_password FROM Customer WHERE ID ={self.uid}')
        password = cursor.fetchone()[0]
        actual_pass = input()
        if password.strip() == actual_pass.strip():
            self.isauthenticated = True
            print('''|+++++Authenticated+++++|''')
            
        else:
            print('''|+++++Wrong Password+++++|''')
        cursor.close()
        return self.isauthenticated
    
    def __view_product__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------CATALOUGE-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT Product_Name, ID FROM Product')
        result = cursor.fetchall()
        table= PrettyTable()
        table.field_names = [desc[0] for desc in cursor.description]
        for row in result:
            table.add_row(row)
        print(table)
        print("|","_"*50,"|")
        cursor.close()
    def __view_category__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------CATEGORY-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute('SELECT "Category Name" FROM Category')
        result = cursor.fetchall()
        self.print_table(result, cursor)
        cursor.close()
        
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
    
    def __upgrade__(self,):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|-------------------------UPGRADE-----------------------|')
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Membership FROM Customer WHERE ID = {self.uid}')
        level = cursor.fetchone()[0]
        cursor.close()
        print(f'''|+++++You are currently a level {level} user+++++|''')
        desired_level=input(f'''|++++++++++Enter the level to upgrade to+++++++++|
                  1. Normal
                  2. Elite
                  3. Prime              
              ''')
        desired_level = ["Normal","Elite","Prime"][int(desired_level)-1]
        cursor = self.connection.cursor()
        if desired_level!=level:
            cursor.execute(f'UPDATE Customer SET Membership = "{desired_level}" WHERE ID = {self.uid}')
            self.connection.commit()
            print(f'''|+++++You are now a {desired_level} user+++++|''')
        else:
            print(f'''|+++++You are already a {level} user+++++|''')
        cursor.close()
    
    def __add_money__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        cursor  = self.connection.cursor()
        cursor.execute(f'UPDATE Customer SET Wallet = Wallet + {input("Enter amount to add: ")} WHERE ID = {self.uid}')
        self.connection.commit()
        cursor.close()
        print("|+++++Money Added+++++|")
        
    def do_transaction(self, amount):
        print("|-------------------------TRANSACTION-----------------------|")
        print(f"For amount: {amount}, Select your payment method")
        method = int(input('''
              1. Credit/Debit Card
              2. Netbanking
              3. UPI
              4. Cash On Delivery
              5. Pay Later
              '''))
        method = ["Credit/Debit Card","Netbanking","UPI","Cash On Delivery","Pay Later"][method-1]
        transaction_status = "Successful"
        transaction_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return method,transaction_status,transaction_date
    def __place_order__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        #TODO: add transaction
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Cart.Product_ID,Cart.Discount,Cart.Quantity,Product.Product_Price FROM Cart,Product WHERE Cart.Customer_ID = {self.uid} AND Cart.Product_ID = Product.ID')
        result = cursor.fetchall()
        amount = self.calculate_price(result)
        method, transaction_status, transaction_date = self.do_transaction(amount)
        order_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        order_status = "Under Process"
        delivery_date =   time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time() + 7*24*60*60))
        delivery_fee = random.randint(0,100)
        customer_id = self.uid
        cursor.close()
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO Orders (Order_Date,Amount,Status,Delivery_Date,Delivery_Fee,Customer_ID) VALUES ({order_date},{amount},{order_status},{delivery_date},{delivery_fee},{customer_id})')
        self.connection.commit()
        print("__Order Placed__")
        self.__clear_cart__()
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT ID FROM Orders WHERE Customer_ID = {self.uid} ORDER BY ID DESC LIMIT 1')
        id = cursor.fetchone()
        cursor.close()
        cursor = self.connection.cursor()
        cursor.execute(f'Insert into Customer_Transaction Values ({transaction_date},{amount},{transaction_status},{method},{id},{self.uid})')      
    
    def calculate_price(self,table):
        # table = [(pid,discount,quantity,price),...]
        #TODO: calculate price
        #total_Price = sum(price*quantity*(1-discount))
        #return -> total_price
        
        pass
        return 0
        
    
    def __view_orders__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print("|-------------------------ORDERS-----------------------|")
        cursor = self.connection.cursor()
        cursor.execute('SELECT ID, Order_Date, Amount, Status FROM Orders WHERE Customer_ID = {self.uid}')
        result = cursor.fetchall()
        result = cursor.fetchall()        
        cursor.close()
        
    def __view_cart__(self):
        
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        cursor = self.connection.cursor()
        input('''|-------------Cart------------|''')
        cursor.execute(f'SELECT Product_Name, ID FROM Product WHERE ID IN (SELECT Product_ID FROM Cart WHERE Customer_ID = {self.uid})')
        result = cursor.fetchall()
        result = cursor.fetchall()
        cursor.close()
        
    def print_table(self,result,cursor):
        table= PrettyTable()
        table.field_names = [desc[0] for desc in cursor.description]
        for row in result:
            table.add_row(row)
        print(table)
        print("|","-"*50,"|")
        
    def __view_wishlist__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        cursor = self.connection.cursor()
        input('''|-------------Cart------------|''')
        cursor.execute(f'SELECT Product_Name, ID FROM Product WHERE Product_ID IN (SELECT Product_ID FROM Wishlist WHERE Customer_ID = {self.uid})')
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
            cursor.execute(f'UPDATE Customer SET {field} = {value} WHERE ID = {self.uid}')
            self.connection.commit()
            print(f'''|+++++{field} Updated+++++|''')
        cursor.close()
    
    def __add_product_to_wishlist__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        print('|__________________________ADD TO WISHLIST__________________________|')
        product_id = input('''Enter the product ID''')
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO Wishlist VALUES ({product_id},{self.uid})')
        self.connection.commit()
        print(f'{product_id} added to wishlist')
        cursor.close()
        
    def __add_product_to_cart__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        print('|__________________________ADD TO CART__________________________|')
        product_id = input('''Enter the product ID:''')
        quantity = int(input('''Enter the quantity:'''))
        
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Membership FROM Customer WHERE ID = {self.uid}')
        level = cursor.fetchone()
        discount = 0 if level=='Normal' else 0.1 if level=='Elite' else 0.2
        cursor.execute(f'INSERT INTO Cart VALUES ({quantity},{discount},{product_id},{self.uid})')
        self.connection.commit()
        print(f'{product_id} added to cart')
        cursor.close()
        
    def __review__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        print('|__________________________ADD TO REVIEW__________________________|')
        product_id = input('''Enter the product ID''')
        rating = int(input('''Enter the rating (1-5)'''))
        title = input('''Enter the review title''')
        comment = input('''Enter the review''')
        current = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        cursor = self.connection.cursor()
        cursor.execute(f'INSERT INTO Review VALUES ({rating},"{title}","{comment}",{current},{product_id},{self.uid})')
        self.connection.commit()
        print(f'review added to product {product_id}')
        cursor.close()
    
    def __empty_cart__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        print('|__________________________EMPTY CART__________________________|')
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM Cart WHERE Customer_ID = {self.uid}')
        self.connection.commit()
        print(f'cart emptied')
        cursor.close()
    
    def __empty_wishlist__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        
        print('|__________________________EMPTY Wishlist__________________________|')
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM Wishlist WHERE Customer_ID = {self.uid}')
        self.connection.commit()
        print(f'Wishlist emptied')
        cursor.close()
    
    def trace_order(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        self.__view_orders__()
        order_id = int(input('''Enter the order ID to be trace'''))
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT Tracking_URL FROM Courier WHERE Order_ID = {order_id}')
        url = cursor.fetchone()
        print(f'''|+++++Tracking URL: {url}+++++|''')
        cursor.close()
    def __view_transactions__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        cursor = self.cursor.connection()
        cursor.execute(f'SELECT * FROM Customer_Transaction WHERE Customer_ID = {self.uid}')
        result = cursor.fetchall()
        self.print_table(result,cursor)
        cursor.close()
    def __view_profile__(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        cursor = self.cursor.connection()
        cursor.execute(f'SELECT * FROM Customer WHERE ID = {self.uid}')
        result = cursor.fetchone()
        self.print_table(result,cursor)
        cursor.close()
    
        
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
        cursor.execute(f'DELETE FROM Customer WHERE ID = {self.uid}')
        self.connection.commit()
        self.__log_out__()
        print("Account Deleted")
    
    def unauthorized(self):
        print('''|+++++You are not authorized to view this page+++++|''')

    def menu(self):
        if not self.isauthenticated:
            self.unauthorized()
            return
        function_tuple_list = [
            (self.__view_product__,"View Product Catalogue"),
            (self.__view_category__,'View Category List'),
            (self.__view_brand__,'View Brand List'),
            (self.__upgrade__,"Upgrade account type"),
            (self.__add_money__,"Add Money to wallet"),
            (self.__place_order__,"Place Order"),
            (self.__view_orders__,"View Previous Orders"),
            (self.__view_cart__,"View Current Cart"),
            (self.__view_wishlist__,"View Wishlist"),
            (self.__update__,"Update Personal Details"),
            (self.__add_product_to_wishlist__,"Add Product to Wishlist"),
            (self.__add_product_to_cart__,"Add product to cart"),
            (self.__review__,"Add review"),
            (self.__empty_cart__,"Discard Cart"),
            (self.__empty_wishlist__,"Delete Wishlists"),
            (self.trace_order,"Trace Order"),
            (self.__view_transactions__,"View Previous Transactions"),
            (self.__view_profile__,"Display Profile"),
            (self.__log_out__,"Logout"),
            (self.__delete__,"Delete Account"),
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
        
        