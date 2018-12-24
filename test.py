# coding: utf-8

import requests
#from constants import *
import openfoodfacts
import json
#import mysql.connector
#
#var=requests.get("https://fr-en.openfoodfacts.org/category/pizzas/1.json")
#var=json.loads(var.text)
#for product in var["products"]:
#    print (json.dumps(product,indent=2))

products = requests.get("https://world.openfoodfacts.org/cgi/search.pl",{
            'action': 'process',
            'tagtype_0': 'categories', #which subject is selected (categories)
            'tag_contains_0': 'contains', #contains or not
            'sort_by': 'unique_scans_n',
            'countries': 'France',
            'json': 1,
            'page': 1
            })
response = json.loads(products.text)
for product in response["products"]:
    print(product.get("allergens"))
  
#products = openfoodfacts.products.get_by_country("France", page=5)
#print(json.dumps(products, indent=2))
#for product in products:
#    for key in product_data.keys():
#                try:
#                    return product[product_data[key]]
#                except KeyError:
#                    print("error!")

#mydb = mysql.connector.connect(
#  host=connect["host"],
#  user=connect["user"],
#  passwd=connect["passwd"],
#  database=connect["database"]
#)
#
#mycursor = mydb.cursor()
#
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#    print(x)