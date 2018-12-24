Projet 5 OC

Fichier script.py:

  Fonction connection: Se connecte à la base de donnée OFF (OpenFoodFacts) avec l'utilisateur 'projet5' afin de la remplir. Si la base de donnée ou l'utilisateur n'existe pas, appelle le mode create_database pour les créer.

  Fonction fecth : Récupère les données de l'API d'OpenFoodFacts. Récupère les produits francais, et les insère dans la table products de la base de donnée.

  Fonction create_table : Créer la table products dans la base de donnée OFF si elle n'existe pas.

  Fonction fill_table : Utilise un threading sur la fonction fetch pour lancer plusieurs requetes à la fois et accélerer le remplissage de la table.

  Fonction clear_table : Retire tout les produits ne possédant pas de nom ni de score nutritionnel.

Fichier Interface:
  
   Fonction menu :  Affiche le menu à l'utilisateur ou il pourra choisir soit de rechercher un aliment, soit de consulter la liste des aliments sauvegardés, en appuyant sur 1 ou 2.
   
   Fonction saved_researched : Affiche les aliments sauvegardés.
   
   Fonction select_category : Demande à l'utilisateur de choisir une catégorie parmi une liste de 9 catégories possibles.
   
   Fonction select_product : Demande à l'utilisateur d'entrer le nom de son produit.
   
   Fonction save : Sauvegarde la recherche de l'utilisateur si il le souhaite.
   
   Fonction display_results : Affiche le résultat de la recherche, ou la liste des produits sauvegardés.
   
Fichier create_database:

   Fonction connect_root : Demande à l'utilisateur de se connecter à l'utilisateur MySQL ayant les droits de créations de base de données et d'utilisateurs (L'utilisateur root par défaut)
   
   Fonction create_user : Crée l'utilisateur projet5 qui se connectera à la base de donnée OFF pour l'utiliser.
   
   Fonction create_database : Crée la base de donnée OFF (OpenFoodFacts) utilisé par le programme.
