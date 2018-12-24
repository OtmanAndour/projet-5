#! /usr/bin/env python
# coding: utf-8

"""This function serves as the interface between the user and the database to search for any product"""

import mysql.connector
from constants import *

class Interface:
    """Main class containing all the methods to run the program"""
    
    def connection(self):
        """Connects to mysql"""
        self.mydb = mysql.connector.connect(
            host=connect["host"],
            user=connect["user"],
            passwd=connect["passwd"],
            database=connect["database"]
        )
        self.mycursor = self.mydb.cursor()
        
    def menu(self):
        """Display the menu with the 2 choices"""
        self.choice = None
        while self.choice is None:
            self.choice = input("""1 - Quel aliment voulez-vous remplacer? \n2 - Retrouver mes aliments sauvegardés \n"""  )
            try:
                self.choice = int(self.choice)
            except ValueError:
                print ("{} n'est pas un choix valide. Choissisez soit 1 ou 2.".format(self.choice))
        return self.choice

    def saved_researches(self):
        """Displays saved researches"""
        print("Voici les recherches sauvegardées. Si rien ne s'affiche, c'est que vous n'avez pas de recherches sauvegardées. ")
        sql = "SELECT * FROM products WHERE saved = 1 ;"
        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchall()
        display_result(self.myresult)
        self.mydb.commit()

    def select_category(self):
        """Select a category amongst 9"""
        self.category = None
        while self.category is None:
            self.category = input(category_text)
            try:
                self.category = int(self.category)
            except ValueError:
                print ("{} n'est pas un choix valide. Reessayez".format(self.category))
        return self.category

    def select_product(self, choice):
        """Select the product name that belongs in the chosen category"""
        self.product = None
        while self.product is None:
            self.product = input("""Entrer le nom du produit.\n""")
            try:
                self.product = str(self.product)
            except ValueError:
                print ("{} n'est pas un choix valide. Reessayez".format(self.product))
        sql = 'SELECT * FROM products WHERE categories LIKE "%' + choice + '%" AND product_name LIKE "%' + self.product +'%" ORDER BY nutriscore LIMIT 1 ;'
        self.mycursor.execute(sql)
        self.myresult = self.mycursor.fetchall()

    def save(self):
        """Save the results of the research"""
        for x in self.myresult:
            sql = 'UPDATE products SET saved = 1 WHERE id = ' + str(x[0]) + ';'
            self.mycursor.execute(sql)
            self.mydb.commit()

def display_result(result):
    """Function that displays the results of the different methods called"""
    for x in result:
        print("""Nom du produit : {} 
                 Lien url : {}
                 Catégories : {} 
                 Score nutritionnel : {} 
                 Magasins où le produit est en vente : {} 
        """.format(x[1],x[2],x[3],x[4],x[5]))


def main ():
    """Main function"""
    interface = Interface()
    interface.connection()
    menu_choice = interface.menu()
    if menu_choice == 1:
        category = interface.select_category()
        category = categories[str(category)]
        interface.select_product(category)
        if len(interface.myresult) == 0:
            print("Aucun résultat")
        else:
            display_result(interface.myresult)
            interface.mydb.commit()
            save_choice = None 
            while save_choice is None :
                save_choice = input("""Voulez-vous sauvegarder votre recherche? 
                                        1- Oui
                                        2- Non\n""")
                try:
                    save_choice = int(save_choice)
                except ValueError:
                    print ("{} n'est pas un choix valide. Reessayez".format(save_choice))
            if save_choice == 1:
                interface.save()
    else:
        interface.saved_researches()
        interface.mydb.commit()
        

if __name__ == "__main__":
    main()