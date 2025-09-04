def welcome_message():
    print("Bienvenue dans le vérificateur de saison des recettes!\nLe calendrier des ingrédients est extrait de https://www.greenpeace.fr/guetteur/calendrier/, Merci à eux.")

#Fonction présentant les choix d'actions possibles à l'utilisateur
def menu():
    print("1. Vérifier la saisonalité d'une recette")
    print("2. Consulter la liste des ingrédients référencés")
    print("3. Extraire le calendrier des ingrédients au format CSV, classé par ingrédient")
    print("4. Extraire le calendrier des ingrédients au format CSV, classé par mois")
    print("5. Quitter")

    #Nous demandons à l'utilisateur de faire son choix dans le menu
    user_choice=input("Entrez votre choix (1-5) : ")

    #Nous vérifions que la valeur donnée par l'utilisateur fait bien partie des options possible et lui redemandons un choix si ce n'est pas le cas
    while user_choice not in ["1", "2", "3", "4", "5"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-5) : ")
    return user_choice

#fonction pour récupérer la liste des ingrédients de la recette de l'utilisateur et vérifier qu'elle pourra être comparée avec la liste du calendrier
def get_recipe(list_ingredient):
    #Nous demandons à l'utilisateur la liste des ingrédients qui composent sa recette et la stockons dans une liste
    user_recipe = input('Veuillez fournir la liste de vos ingrédients séparés par une virgule et sans espace (exemple: Potiron,Carotte,Brocoli) ')
    recipe_raw = user_recipe.split(',')
    recipe_standardized=[]
    for ingredient in recipe_raw:
        recipe_standardized.append(ingredient.casefold())
    recipe_clean=[]
    #Nous vérifions que la liste d'ingrédients fournie par l'utilisateur est bien présente dans la base de données GreenPeace (en respectant la casse)
    for ingredient in recipe_standardized:
        while ingredient not in list_ingredient:
            print(f"\033[31m{ingredient} n'est pas reconnu comme un ingrédient valide, veuillez l'écrire correctement.\033[0m")
            #Si l'ingrédient n'est pas présent dans la BD, c'est peut-être une erreur d'orthographe, nous proposons alors à l'utilisateur de consulter la liste des ingrédients de la BD
            display_list=input("Voulez-vous voir la liste des ingrédients valide?\n Tapez 'oui' ou 'non': \n")
            if display_list == "oui":
                for i in list_ingredient:
                    print(i)
                ingredient_not_found=input("Avez-vous trouvé votre ingrédient dans la liste?\n Tapez 'oui' ou 'non': \n")
                #Si l'ingrédient n'est pas présent dans la BD alors nous indiquons à l'utilisateur qu'il ne peut pas être pris en compte
                if ingredient_not_found == "non":
                    print("Votre ingrédient ne fait pas partie des aliments considérés dans le calendrier de GreenPeace, il ne sera pas pris en compte.\n Veuillez vous référer au site GreenPeace pour plus d'information.")
                    break
            ingredient = input("Votre ingrédient: ")
        if ingredient in list_ingredient:
            recipe_clean.append(ingredient)
    return recipe_clean
                