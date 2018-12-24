#! /usr/bin/env python
# coding: utf-8

from constants import *
import mysql.connector

class Database:

    def connect_root(self):
        user_root = str(input("Entrer le nom d'utilisateur MySQL qui possède les droits de création d'un utilisateur (L'utilisateur root) \n"))
        password = str(input("Entrer le mot de passe qui correspond à l'utilisateur MySQL root. \n"))
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=user_root,
            passwd=password
        )
        self.mycursor = self.mydb.cursor()

    def create_user(self):
        sql_create = "CREATE USER 'projet5'@'localhost' IDENTIFIED BY 'projet5';"
        sql_grant = "GRANT ALL PRIVILEGES ON OFF . * TO 'projet5'@'localhost';"
        self.mycursor.execute(sql_create)
        self.mycursor.execute(sql_grant)
        self.mydb.commit()
    
    def create_database(self):
        self.mydb = mysql.connector.connect(
                        host=connect["host"],
                        user=connect["user"],
                        passwd=connect["passwd"]
        )
        self.mycursor = self.mydb.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS OFF"
        self.mycursor.execute(sql)
        self.mydb.commit()
        
        
def main():
    database = Database()
    database.connect_root()
    print("Création de l'utilisateur projet5...")
    database.create_user()
    print("Création de l'utilisateur terminée.")
    print("Création de la base de donnée OFF...")
    database.create_database()
    print("Création de la base de donnée terminée.")
    print("Connection à l'utilisateur projet5...")
    return mysql.connector.connect(
                host=connect["host"],
                user=connect["user"],
                passwd=connect["passwd"],
                database=connect["database"]
            )


if __name__ == "__main__":
    main()