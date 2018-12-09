#! /usr/bin/env python
# coding: utf-8

from copy import copy
from constants import *
import threading
import openfoodfacts
import json
import mysql.connector

class Main:

    def connection(self):
        #Connects to mysql
        self.mydb = mysql.connector.connect(
            host=connect["host"],
            user=connect["user"],
            passwd=connect["passwd"],
            database=connect["database"]
        )

    def fetch(self,i):
        while True:
            i+= REQUEST_NUMBER
            products = openfoodfacts.products.get_by_country("France", page=i)
            if len(products) == 0:
                break
            for product in products:
                temp = copy(product_data)
                str_key, str_value = "(", "("
                for key,value in temp.items():
                    temp[key] = product.get(value)
                    if temp[key] is not None:
                        str_key += key+","
                        str_value += temp[key]+","
                str_key += ")"
                str_value += ")"
                sql = "INSERT IGNORE INTO product " + str_key + " VALUES " + str_value + ";" 
                self.mycursor.execute(sql)

    def create_table(self):
        #Creates table with mysql.connector
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS products (
                                    id INT,
                                    product_name TEXT NOT NULL,
                                    url TEXT NOT NULL,
                                    categories TEXT,
                                    nutriscore VARCHAR,
                                    stores TEXT,
                                    PRIMARY KEY (id))
                                    ENGINE=INNODB;""")

    def fill_table(self):
        #Fills the table with fetch function and a threading
        for k in range(REQUEST_NUMBER):
            thread=threading.Thread(target=self.fetch, args=(k,))
            thread.start()
                
def main():
    main = Main()
    main.connection()
    main.create_table()
    main.fill_table()

if __name__ == "__main__":
    main()
