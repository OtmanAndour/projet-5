#! /usr/bin/env python
# coding: utf-8

"""This file creates and fills the database using the OpenFoodFacts API"""

from copy import copy
from constants import *
import create_database
import threading
import requests
import json
import mysql.connector

class Main:
    """Main class that includes all methods to create and fill the database"""

    def connection(self):
        """Connects to mysql"""
        try:
            return mysql.connector.connect(
                host=connect["host"],
                user=connect["user"],
                passwd=connect["passwd"],
                database=connect["database"]
            )
        except mysql.connector.errors.ProgrammingError:
            print("La base de donnée n'existe pas. Il faut créer l'utilisateur et la base de donnée avant de pouvoir s'y connecter.")
            create_database.main()
            print("Connecté.")

    def fetch(self,i):
        """Fetches data from the API"""
        mydb = self.connection()
        mycursor = mydb.cursor()
        while True:
            i+= REQUEST_NUMBER
            products = requests.get("https://world.openfoodfacts.org/cgi/search.pl",{
            'action': 'process',
            'tagtype_0': 'categories', #categories selected
            'tag_contains_0': 'contains', #contains or not
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'json': 1,
            'page': i,
            'page_size' : 1000
            })
            response = json.loads(products.text)
            if len(response) == 0 or i == 1500 :
                break
            for product in response["products"]:
                temp = copy(product_data)
                str_key, str_value = "(", "("
                for key,value in temp.items():
                    temp[key] = product.get(value)
                    if temp[key] is not None :
                        if key == "id":
                            str_key += key+","
                            str_value += temp[key]+","
                        else:
                            str_key += key+","
                            str_value += '"' + temp[key] + '",'
                str_key = str_key[:-1] + ")"
                str_value = str_value[:-1] + ")"
                sql = "INSERT IGNORE INTO products " + str_key + " VALUES " + str_value + ";" 
                try:
                    mycursor.execute(sql)
                    mydb.commit()
                except mysql.connector.errors.ProgrammingError:
                    pass

    def create_table(self):
        """Creates table with mysql.connector"""
        mydb = self.connection()
        mycursor = mydb.cursor()
        mycursor.execute("""CREATE TABLE IF NOT EXISTS products (
                                    id INT,
                                    product_name TEXT(50) NOT NULL,
                                    url TEXT(50) NOT NULL,
                                    categories TEXT(50),
                                    nutriscore VARCHAR(50),
                                    stores TEXT(50),
                                    saved BOOLEAN DEFAULT FALSE,
                                    PRIMARY KEY(id))
                                    ENGINE=INNODB;""")

    def fill_table(self):
        """Fills the table with fetch function and a threading"""
        for k in range(REQUEST_NUMBER):
            thread=threading.Thread(target=self.fetch, args=(k,))
            thread.start()
                
    def clear_table(self):
        """Clears the data table from all elements without a product name or a nutriscore"""
        mydb = self.connection()
        mycursor = mydb.cursor()
        sql = 'DELETE FROM products WHERE product_name = "" OR nutriscore IS NULL ;'
        mycursor.execute(sql)
        mydb.commit()

def main():
    main = Main()
    main.connection()
    main.create_table()
    main.fill_table()
    main.clear_table()
   

if __name__ == "__main__":
    main()
