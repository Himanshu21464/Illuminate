from user import User
from seller import Seller
from admin import Admin
import mysql.connector

def main(connection):
    print("|---------------------------LOGIN-------------------------|")
    account_type =  int(input('''Enter the account type
          1. Employee
          2. Customer
          3. Seller
          '''))
    _class = [Admin,User,Seller][account_type-1]
    uid = int(input(f"Enter Account ID of your {['Employee','Customer','Seller'][account_type-1]} account"))
    _obj = _class(uid,connection)
    _obj.authenticate()
    _obj.menu()
    return input('''Do you want to exit? 
                 1<- Yes
                 0<- Don't exit
                 ''')
if __name__=='__main__':
    flag = 0
    # connection = mysql.connector.connect(user='root',
    #                             password='password',
    #                             host='localhost',
    #                             database='Illuminate')
    connection = mysql.connector.connect(user='root',
                                password='password',
                                host='10.212.133.2',
                                database='Illuminate')
    while flag==0:
        flag = int(main(connection))
    print("Thank you for using Illuminate!!!")