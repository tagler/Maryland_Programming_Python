import sqlite3
import string

con = sqlite3.connect("database_example.sqlite3")
cursor = con.cursor()

sql_cmd_1 = "create table if not exists customers (firstname TEXT, lastname TEXT, address TEXT, city TEXT, state TEXT, zipcode TEXT)"
cursor.execute(sql_cmd_1)

with open("customers.txt","r") as data_file:
    for each_line in data_file:
        line = each_line.strip().split(",")
        sql_cmd_2 = "insert into customers values (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_cmd_2, line)

state_input = input("please enter a state: ")
state_input_upper = state_input.upper()
sql_cmd_3 = "select * from customers where state ='"+state_input_upper+"'"
cursor.execute(sql_cmd_3)
for each_customer in cursor.fetchall():
    print(each_customer)

con.commit()
con.close()
