import Extraction_Calendrier_et_ingredients
import user_interaction
import Creation_csv

#Cette fonction va permettre de donner la liste des mois pour lesquels tous les ingrédients de la recette de l'utilisateur sont disponibles
def check_recipe_feasability(calendar, recipe_clean):
    list_of_month=[]
    for ingredient in recipe_clean:
        ingredient_month=[]
        #Avec cette boucle nous créons une liste des mois de disponibilité pour chaque ingrédient
        for couple in calendar:
            if ingredient == couple.ingredient:
                ingredient_month.append(couple.month)
        list_of_month.append(ingredient_month)
    #Une fois que nous avons la liste des mois de chaque ingrédient, nous pouvons en extraire les valeurs présentes dans toutes les listes
    valid_month=set(list_of_month[0]).intersection(*list_of_month)
    return valid_month

#Cette fonction permet d'exécuter l'action choisie par l'utilisateur dans le menu
def Action_user_choice(user_choice, calendar, list_ingredient, column1, column2):
    match user_choice:
        case '1':
            recipe_clean=user_interaction.get_recipe(list_ingredient)
            valid_month=check_recipe_feasability(calendar, recipe_clean)
            #S'il n'y a pas de mois pour lequel l'ensemble des ingrédients est disponible alors la liste sera vide, ce qui nous permet d'indiquer à l'utilisateur qu'il n'y a pas de bonne saison pour cette recette en France
            if not valid_month:
                print("Les ingrédients de votre recette n'ont aucune saison en commun.")
            #Sinon nous fournissons la liste des mois à l'utilisateur
            else:
                print("Voici les mois durant lesquels votre recette est réalisable:")
                for month in valid_month:
                    print(month)
        case '2':
            #le choix 2 permet d'afficher la liste des ingrédients de la BD
            Extraction_Calendrier_et_ingredients.display_ingredient_list(list_ingredient)
        #les choix 3 et 4 permettent de créer un fichier CSV contenant le calendrier soit classé par mois, soit par ingrédient. L'inversion des colonnes permet de choisir la clefs d'entrée de cette "base de données"
        case '3':
            calendar_dict=Extraction_Calendrier_et_ingredients.class_to_dict(calendar, column1, column2)
            Creation_csv.create_csv_calendar(calendar_dict, column1, column2)
        case '4':
            calendar_dict=Extraction_Calendrier_et_ingredients.class_to_dict(calendar, column1, column2)
            column1_reverse = column2
            column2_reverse = column1
            Creation_csv.create_csv_calendar(calendar_dict, column1_reverse, column2_reverse)
        case '5':
            exit()